#!/usr/bin/env python3
"""
Calibración triple: BOVINOS solo + PORCINOS solo + AMBOS (joint).
Genera 3 archivos de parámetros y 3 gráficos de diagnóstico.
"""

from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS as PARAMETROS_BASE
from src.simulacion.simulador import ejecutar_simulacion


# ============================================================
# CONFIG
# ============================================================

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO_DATOS = RAIZ / "serie_mensual_analisis.csv"

ESTADO_INICIAL = np.array([1000, 500, 200, 1000, 1000, 0, 0], dtype=float)
DIAS_SIMULACION = 730
DIAS_POR_MES = 365.25 / 12

NOMBRES_PARAMS = ["b", "mu_f", "c"]
LIMITES_INF = [0.02, 0.02, 0.1]
LIMITES_SUP = [0.5, 0.3, 1.0]
X0 = [PARAMETROS_BASE["b"], PARAMETROS_BASE["mu_f"], PARAMETROS_BASE["c"]]

np.random.seed(12345)


# ============================================================
# FUNCIONES BASE
# ============================================================

def cargar_series():
    df = pd.read_csv(ARCHIVO_DATOS)
    df["periodo"] = pd.to_datetime(df["periodo"].astype(str), format="%Y-%m", errors="coerce")
    df = df.dropna(subset=["periodo"]).sort_values("periodo").reset_index(drop=True)

    series = {}
    for hosp in ("bovinos", "porcinos"):
        col_comp = f"{hosp}_completo"
        comp = df[col_comp].astype(str).str.strip().str.lower().eq("si")
        casos = pd.to_numeric(df[hosp], errors="coerce")
        val = casos.notna() & comp
        dfv = df.loc[val].copy()
        dfv["casos"] = casos.loc[val].values
        if len(dfv) >= 5:
            series[hosp] = {
                "df": dfv, "casos": dfv["casos"].to_numpy(float),
                "n_meses": len(dfv), "periodo_ini": dfv["periodo"].min(),
                "periodo_fin": dfv["periodo"].max(),
            }
            print(f"  {hosp}: {len(dfv)} meses ({dfv['periodo'].min().strftime('%Y-%m')}–{dfv['periodo'].max().strftime('%Y-%m')}), casos={dfv['casos'].sum():.0f}")
    return series


def simular_hembras(parametros, n_meses):
    dias = int(np.ceil((n_meses - 1) * DIAS_POR_MES))
    t = np.arange(0, DIAS_SIMULACION + 1, 7, dtype=float)
    res = ejecutar_simulacion(parametros, ESTADO_INICIAL.copy(), t, "etapas")
    if not res.success:
        raise RuntimeError(res.message)
    return np.interp(np.arange(n_meses) * DIAS_POR_MES, t, res.y[4])


def build_params(x):
    p = deepcopy(PARAMETROS_BASE)
    p["b"], p["mu_f"], p["c"] = float(x[0]), float(x[1]), float(x[2])
    return p


def residuos_series(x, series_dict):
    p = build_params(x)
    all_r = []
    for data in series_dict.values():
        h = simular_hembras(p, data["n_meses"])
        esc = max(data["casos"].mean() / max(h.mean(), 1e-6), 1e-6)
        all_r.append(np.log1p(esc * h) - np.log1p(data["casos"]))
    return np.concatenate(all_r)


def calibrar(series_dict, label):
    print(f"\n--- Calibrando {label} ---")
    res = least_squares(
        lambda x: residuos_series(x, series_dict), X0,
        bounds=(LIMITES_INF, LIMITES_SUP), loss="soft_l1", f_scale=0.5,
        max_nfev=300, verbose=0
    )
    print(f"  Costo: {res.cost:.4f}, ok: {res.success}, nfev: {res.nfev}")
    return res


def covarianza(res, series_dict):
    n = sum(d["n_meses"] for d in series_dict.values())
    p = len(NOMBRES_PARAMS)
    jac = res.jac
    if jac is None:
        from scipy.optimize import approx_derivative
        jac = approx_derivative(lambda x: residuos_series(x, series_dict), res.x)
    rss = 2 * res.cost
    sig2 = rss / max(n - p, 1)
    jtj = jac.T @ jac
    if np.linalg.cond(jtj) > 1e12:
        jtj += 1e-6 * np.eye(p)
    try:
        cov = sig2 * np.linalg.inv(jtj)
    except np.linalg.LinAlgError:
        cov = sig2 * np.linalg.pinv(jtj)
    se = np.sqrt(np.diag(cov))
    z = 1.96
    return cov, se, res.x - z*se, res.x + z*se, sig2


def metricas_por_especie(x, series_dict):
    p = build_params(x)
    out = {}
    for hosp, data in series_dict.items():
        h = simular_hembras(p, data["n_meses"])
        esc = max(data["casos"].mean() / max(h.mean(), 1e-6), 1e-6)
        pred = esc * h
        out[hosp] = {
            "escala": esc, "pred": pred, "h": h,
            "rmse_log": float(np.sqrt(np.mean((np.log1p(pred) - np.log1p(data["casos"]))**2))),
            "mae": float(np.mean(np.abs(pred - data["casos"]))),
        }
    return out


def guardar_csv(res, se, ic_l, ic_u, sig2, metricas, series_dict, sufijo):
    """Guarda CSV con params + IC + métricas."""
    rows = []
    for i, n in enumerate(NOMBRES_PARAMS):
        rows.append({
            "parametro": n, "valor_optimo": res.x[i],
            "error_estandar": se[i], "ic_2.5": ic_l[i], "ic_97.5": ic_u[i],
            "base_literatura": PARAMETROS_BASE[n],
        })
    for hosp, m in metricas.items():
        rows.append({"parametro": f"escala_empirica_{hosp}", "valor_optimo": m["escala"],
                     "error_estandar": np.nan, "ic_2.5": np.nan, "ic_97.5": np.nan, "base_literatura": np.nan})
        rows.append({"parametro": f"rmse_log_{hosp}", "valor_optimo": m["rmse_log"],
                     "error_estandar": np.nan, "ic_2.5": np.nan, "ic_97.5": np.nan, "base_literatura": np.nan})
        rows.append({"parametro": f"mae_{hosp}", "valor_optimo": m["mae"],
                     "error_estandar": np.nan, "ic_2.5": np.nan, "ic_97.5": np.nan, "base_literatura": np.nan})
    rows.append({"parametro": "sigma2_residual", "valor_optimo": sig2, "error_estandar": np.nan,
                 "ic_2.5": np.nan, "ic_97.5": np.nan, "base_literatura": np.nan})
    rows.append({"parametro": "n_total_obs", "valor_optimo": sum(d["n_meses"] for d in series_dict.values()),
                 "error_estandar": np.nan, "ic_2.5": np.nan, "ic_97.5": np.nan, "base_literatura": np.nan})

    df = pd.DataFrame(rows)
    fname = RAIZ / f"calibracion_parametros_{sufijo}.csv"
    df.to_csv(fname, index=False, encoding="utf-8-sig")
    print(f"  Guardado: {fname.name}")
    return df


def graficar(series_dict, metricas, sufijo):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        n = len(series_dict)
        fig, axes = plt.subplots(n, 3, figsize=(15, 5*n))
        if n == 1:
            axes = axes.reshape(1, -1)

        for idx, (hosp, data) in enumerate(series_dict.items()):
            m = metricas[hosp]
            fechas = data["df"]["periodo"].dt.to_period("M").dt.to_timestamp()
            
            # Panel 1: Serie temporal
            ax = axes[idx, 0]
            ax.plot(fechas, m["h"]*m["escala"], "r--", label=f"Modelo (esc={m['escala']:.3f})", lw=2)
            ax.plot(fechas, data["casos"], "ko-", label="Obs", ms=4)
            ax.set_title(str(hosp).capitalize() + ": Ajuste")
            ax.legend()
            ax.grid(True, alpha=0.3)

            # Panel 2: Residuos
            ax = axes[idx, 1]
            residuos = np.log1p(data["casos"]) - np.log1p(m["pred"])
            ax.plot(fechas, residuos, "bo-", ms=4)
            ax.axhline(0, color="k", ls="--", alpha=0.5)
            ax.set_title(str(hosp).capitalize() + ": Residuos log")
            ax.grid(True, alpha=0.3)

            # Panel 3: Pred vs Obs
            ax = axes[idx, 2]
            ax.plot(data["casos"], m["pred"], "ro", alpha=0.6, ms=6)
            mv = max(float(data["casos"].max()), float(m["pred"].max()))
            ax.plot([0, mv], [0, mv], "k--", alpha=0.5)
            ax.set_title(str(hosp).capitalize() + ": Pred vs Obs")
            ax.grid(True, alpha=0.3)

        plt.tight_layout()
        fname = RAIZ / f"calibracion_diagnosticos_{sufijo}.png"
        plt.savefig(fname, dpi=160)
        plt.close()
        print(f"  Grafico: {fname.name}")
    except Exception as e:
        print(f"  Warning grafico: {e}")


# ============================================================
# MAIN: 3 CALIBRACIONES
# ============================================================

def main():
    print("="*60)
    print("CALIBRACIÓN TRIPLE: BOVINOS | PORCINOS | JOINT")
    print("="*60)

    series_all = cargar_series()

    # 1. Solo bovinos
    res_b = calibrar({"bovinos": series_all["bovinos"]}, "BOVINOS")
    cov_b, se_b, icl_b, icu_b, sig2_b = covarianza(res_b, {"bovinos": series_all["bovinos"]})
    met_b = metricas_por_especie(res_b.x, {"bovinos": series_all["bovinos"]})
    df_b = guardar_csv(res_b, se_b, icl_b, icu_b, sig2_b, met_b, {"bovinos": series_all["bovinos"]}, "bovinos")
    graficar({"bovinos": series_all["bovinos"]}, met_b, "bovinos")

    # 2. Solo porcinos
    res_p = calibrar({"porcinos": series_all["porcinos"]}, "PORCINOS")
    cov_p, se_p, icl_p, icu_p, sig2_p = covarianza(res_p, {"porcinos": series_all["porcinos"]})
    met_p = metricas_por_especie(res_p.x, {"porcinos": series_all["porcinos"]})
    df_p = guardar_csv(res_p, se_p, icl_p, icu_p, sig2_p, met_p, {"porcinos": series_all["porcinos"]}, "porcinos")
    graficar({"porcinos": series_all["porcinos"]}, met_p, "porcinos")

    # 3. Joint (ambos)
    res_j = calibrar(series_all, "JOINT (bovinos+porcinos)")
    cov_j, se_j, icl_j, icu_j, sig2_j = covarianza(res_j, series_all)
    met_j = metricas_por_especie(res_j.x, series_all)
    df_j = guardar_csv(res_j, se_j, icl_j, icu_j, sig2_j, met_j, series_all, "joint")
    graficar(series_all, met_j, "joint")

    # Resumen comparativo en consola
    print("\n" + "="*60)
    print("COMPARATIVA PARÁMETROS CALIBRADOS")
    print("="*60)
    for label, res in [("BOVINOS", res_b), ("PORCINOS", res_p), ("JOINT", res_j)]:
        print(f"\n{label}:")
        for i, n in enumerate(NOMBRES_PARAMS):
            print(f"  {n}: {res.x[i]:.4f}")
    print("\nEscalas empíricas:")
    print(f"  Bovinos (solo):     {met_b['bovinos']['escala']:.4f}")
    print(f"  Porcinos (solo):    {met_p['porcinos']['escala']:.4f}")
    print(f"  Joint - Bovinos:    {met_j['bovinos']['escala']:.4f}")
    print(f"  Joint - Porcinos:   {met_j['porcinos']['escala']:.4f}")

    print("\nOK Archivos generados:")
    for s in ["bovinos", "porcinos", "joint"]:
        print(f"  - calibracion_parametros_{s}.csv")
        print(f"  - calibracion_diagnosticos_{s}.png")


if __name__ == "__main__":
    main()