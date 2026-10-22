#!/usr/bin/env python3
"""
Calibración conjunta BOVINOS + PORCINOS - RÁPIDA Y CORREGIDA
- Fechas reales (meses faltantes respetados)
- Bounds biológicos estrictos
- IC 95% via Jacobiano (Laplace) - RÁPIDO
- Guarda TODO lo que necesitan los escenarios
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

# Archivos de salida (los que leerán los escenarios)
ARCHIVO_PARAMS = RAIZ / "calibracion_parametros.csv"
ARCHIVO_ESCALAS = RAIZ / "calibracion_escalas.csv"
ARCHIVO_GRAFICA = RAIZ / "calibracion_diagnosticos.png"

ESTADO_INICIAL = np.array([1000, 500, 200, 1000, 1000, 0, 0], dtype=float)
DIAS_SIMULACION = 730

# Parámetros a calibrar
NOMBRES_PARAMS = ["b", "mu_f", "c"]

# BOUNDS BIOLOGICOS ESTRICTOS (literatura GBG)
BOUNDS = {
    "b": (0.05, 0.50),
    "mu_f": (0.02, 0.25),
    "c": (0.10, 1.00),
}
LIMITES_INF = [BOUNDS[p][0] for p in NOMBRES_PARAMS]
LIMITES_SUP = [BOUNDS[p][1] for p in NOMBRES_PARAMS]

X0 = [0.20, 0.08, 0.60]  # Iniciales razonables, NO en bordes

np.random.seed(12345)


# ============================================================
# FUNCIONES
# ============================================================

def cargar_datos():
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
                "df": dfv,
                "casos": dfv["casos"].to_numpy(float),
                "fechas": pd.DatetimeIndex(dfv["periodo"]),
                "n_meses": len(dfv),
            }
            print(f"  {hosp}: {len(dfv)} meses ({dfv['periodo'].min().strftime('%Y-%m')} a {dfv['periodo'].max().strftime('%Y-%m')}), casos={dfv['casos'].sum():.0f}")
    return series


def simular_hembras_en_fechas(parametros, fechas_objetivo):
    """Simula e interpola hembras en fechas exactas (pandas DatetimeIndex)."""
    if len(fechas_objetivo) == 0:
        return np.array([])
    
    fecha_inicio = fechas_objetivo.min()
    fecha_fin = fechas_objetivo.max()
    n_dias = (fecha_fin - fecha_inicio).days + 60
    
    t_eval = np.arange(0, n_dias + 1, 7, dtype=float)
    
    resultado = ejecutar_simulacion(
        parametros=parametros,
        estado_inicial=ESTADO_INICIAL.copy(),
        tiempo=t_eval,
        modelo="etapas",
    )
    
    if not resultado.success:
        raise RuntimeError(f"Simulación falló: {resultado.message}")
    
    dias_objetivo = (fechas_objetivo - fecha_inicio).days.astype(float)
    hembras = np.interp(dias_objetivo, t_eval, resultado.y[4])
    return hembras


def construir_parametros(x):
    p = deepcopy(PARAMETROS_BASE)
    p["b"] = float(x[0])
    p["mu_f"] = float(x[1])
    p["c"] = float(x[2])
    return p


def residuos_conjuntos(x, series):
    """Residuos log para todas las series usando fechas reales."""
    p = construir_parametros(x)
    all_res = []
    
    for hosp, data in series.items():
        hembras = simular_hembras_en_fechas(p, data["fechas"])
        escala = max(np.mean(data["casos"]) / max(np.mean(hembras), 1e-6), 1e-6)
        pred = escala * hembras
        res = np.log1p(pred) - np.log1p(data["casos"])
        all_res.append(res)
    
    return np.concatenate(all_res)


def ajustar_deterministico(series):
    print("  -> Optimizando (least_squares bounded)...")
    
    def fun_res(x):
        return residuos_conjuntos(x, series)
    
    res = least_squares(
        fun=fun_res,
        x0=X0,
        bounds=(LIMITES_INF, LIMITES_SUP),
        loss="soft_l1",
        f_scale=0.5,
        max_nfev=200,
        verbose=0,
    )
    print(f"     Costo: {res.cost:.4f}, ok: {res.success}, nfev: {res.nfev}")
    return res


def calcular_ic_laplace(res, series):
    """IC 95% via aproximación Laplace (Jacobiano) - RÁPIDO."""
    print("  -> Calculando IC 95% (Laplace/Jacobiano)...")
    
    n_obs = sum(len(data["casos"]) for data in series.values())
    n_params = len(NOMBRES_PARAMS)
    
    # Jacobiano en el óptimo
    jac = res.jac
    if jac is None:
        from scipy.optimize import approx_derivative
        jac = approx_derivative(lambda x: residuos_conjuntos(x, series), res.x)
    
    # Covarianza: sigma^2 * (J^T J)^-1
    rss = 2 * res.cost
    sigma2 = rss / max(n_obs - n_params, 1)
    
    jtj = jac.T @ jac
    cond = np.linalg.cond(jtj)
    print(f"     Condición J^T J: {cond:.2e}")
    
    if cond > 1e12:
        print("     Regularizando matriz mal condicionada...")
        jtj = jtj + 1e-6 * np.eye(n_params)
    
    try:
        cov = sigma2 * np.linalg.inv(jtj)
    except np.linalg.LinAlgError:
        cov = sigma2 * np.linalg.pinv(jtj)
    
    se = np.sqrt(np.diag(cov))
    z = 1.96
    ic_low = np.maximum(res.x - z * se, LIMITES_INF)
    ic_high = np.minimum(res.x + z * se, LIMITES_SUP)
    
    return ic_low, ic_high, se, sigma2


def calcular_metricas_y_escalas(x_opt, series):
    p_opt = construir_parametros(x_opt)
    metricas = {}
    escalas = {}
    
    for hosp, data in series.items():
        hembras = simular_hembras_en_fechas(p_opt, data["fechas"])
        escala = max(np.mean(data["casos"]) / max(np.mean(hembras), 1e-6), 1e-6)
        pred = escala * hembras
        
        metricas[hosp] = {
            "escala": escala,
            "pred": pred,
            "hembras": hembras,
            "casos_obs": data["casos"],
            "fechas": data["fechas"],
            "rmse_log": float(np.sqrt(np.mean((np.log1p(pred) - np.log1p(data["casos"]))**2))),
            "mae": float(np.mean(np.abs(pred - data["casos"]))),
        }
        escalas[hosp] = escala
    
    return metricas, escalas


def guardar_todo(res, ic_low, ic_high, se, sigma2, metricas, escalas):
    x_opt = res.x
    
    # 1. Parámetros + IC Laplace
    rows_params = []
    for i, nombre in enumerate(NOMBRES_PARAMS):
        rows_params.append({
            "parametro": nombre,
            "valor_optimo": x_opt[i],
            "error_estandar": se[i],
            "ic_2.5": ic_low[i],
            "ic_97.5": ic_high[i],
            "bound_low": LIMITES_INF[i],
            "bound_high": LIMITES_SUP[i],
            "base_literatura": 0.1 if nombre != "c" else 1.0,
        })
    
    df_params = pd.DataFrame(rows_params)
    df_params.to_csv(ARCHIVO_PARAMS, index=False, encoding="utf-8-sig")
    print(f"  OK: {ARCHIVO_PARAMS.name}")
    
    # 2. Escalas (lo que leen los escenarios)
    rows_escalas = []
    for hosp, m in metricas.items():
        rows_escalas.append({
            "especie": hosp,
            "escala_empirica": m["escala"],
            "rmse_log": m["rmse_log"],
            "mae": m["mae"],
            "n_meses": len(m["casos_obs"]),
        })
    
    df_escalas = pd.DataFrame(rows_escalas)
    df_escalas.to_csv(ARCHIVO_ESCALAS, index=False, encoding="utf-8-sig")
    print(f"  OK: {ARCHIVO_ESCALAS.name}")
    
    return df_params, df_escalas


def graficar(series, metricas):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        
        n_sp = len(series)
        fig, axes = plt.subplots(n_sp, 3, figsize=(15, 5*n_sp))
        if n_sp == 1:
            axes = axes.reshape(1, -1)
        
        for idx, (hosp, data) in enumerate(series.items()):
            m = metricas[hosp]
            fechas = data["fechas"]
            
            ax = axes[idx, 0]
            ax.plot(fechas, m["casos_obs"], "ko-", label="Obs", ms=4)
            ax.plot(fechas, m["pred"], "r--", label=f"Mod (esc={m['escala']:.3f})", lw=2)
            ax.set_title(f"{hosp.capitalize()}: Ajuste (fechas reales)")
            ax.legend(); ax.grid(True, alpha=0.3)
            fig.autofmt_xdate()
            
            ax = axes[idx, 1]
            ax.plot(fechas, np.log1p(m["casos_obs"]) - np.log1p(m["pred"]), "bo-", ms=4)
            ax.axhline(0, color="k", ls="--", alpha=0.5)
            ax.set_title(f"{hosp.capitalize()}: Residuos log")
            ax.grid(True, alpha=0.3)
            fig.autofmt_xdate()
            
            ax = axes[idx, 2]
            ax.plot(m["casos_obs"], m["pred"], "ro", alpha=0.6, ms=6)
            mv = max(m["casos_obs"].max(), m["pred"].max())
            ax.plot([0, mv], [0, mv], "k--", alpha=0.5)
            ax.set_title(f"{hosp.capitalize()}: Pred vs Obs")
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(ARCHIVO_GRAFICA, dpi=160)
        plt.close()
        print(f"OK Gráficos: {ARCHIVO_GRAFICA.name}")
    except Exception as e:
        print(f"WARNING Gráficos: {e}")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("CALIBRACIÓN JOINT CORREGIDA - RÁPIDA (Laplace IC)")
    print("=" * 60)
    
    print("\n1. Cargando datos (fechas reales)...")
    series = cargar_datos()
    
    print("\n2. Calibración determinista (fechas reales)...")
    res = ajustar_deterministico(series)
    x_opt = res.x
    print(f"     b={x_opt[0]:.4f}, mu_f={x_opt[1]:.4f}, c={x_opt[2]:.4f}")
    
    print("\n3. IC 95% Laplace (Jacobiano)...")
    ic_low, ic_high, se, sigma2 = calcular_ic_laplace(res, series)
    
    print("\n4. Métricas y escalas...")
    metricas, escalas = calcular_metricas_y_escalas(x_opt, series)
    for hosp, m in metricas.items():
        print(f"  {hosp}: escala={m['escala']:.4f}, RMSE_log={m['rmse_log']:.3f}, MAE={m['mae']:.1f}")
    
    print("\n5. Guardando archivos para escenarios...")
    df_params, df_escalas = guardar_todo(res, ic_low, ic_high, se, sigma2, metricas, escalas)
    
    print("\n6. Gráficos...")
    graficar(series, metricas)
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESULTADOS CALIBRACIÓN JOINT")
    print("=" * 60)
    print(df_params.to_string(index=False, float_format=lambda v: f"{v:.6g}" if pd.notna(v) else "NA"))
    
    print("\nIC 95% LAPLACE:")
    for i, nombre in enumerate(NOMBRES_PARAMS):
        print(f"  {nombre}: [{ic_low[i]:.4f}, {ic_high[i]:.4f}] (opt={x_opt[i]:.4f}, se={se[i]:.4f})")
    
    print("\nESCALAS PARA ESCENARIOS:")
    for hosp, esc in escalas.items():
        print(f"  {hosp}: {esc:.6f}")
    
    print("\nOK CALIBRACION LISTA - Archivos para escenarios:")
    print(f"  - {ARCHIVO_PARAMS.name} (parámetros + IC Laplace)")
    print(f"  - {ARCHIVO_ESCALAS.name} (escalas por especie)")
    print(f"  - calibracion_diagnosticos.png")


if __name__ == "__main__":
    main()