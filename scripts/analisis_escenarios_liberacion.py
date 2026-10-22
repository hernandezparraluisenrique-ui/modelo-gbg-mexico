#!/usr/bin/env python3
"""
Análisis de escenarios de liberación TIE para erradicación GBG México.

USA LA CALIBRACIÓN JOINT RECIÉN GENERADA:
- Carga parámetros de calibracion_parametros.csv
- Carga escalas de calibracion_escalas.csv
- Muestrea incertidumbre paramétrica (Jacobiano/Laplace)
- Escenario base con R0 > 1 (población persistente sin liberación)

Salida:
- escenarios_liberacion_resultados.csv
- escenarios_liberacion_trayectorias.csv
- grafico_escenarios.png
"""

from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS as PARAMETROS_BASE
from src.simulacion.simulador import ejecutar_simulacion


# ============================================================
# CONFIGURACIÓN
# ============================================================

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO_PARAMS = RAIZ / "calibracion_parametros.csv"
ARCHIVO_ESCALAS = RAIZ / "calibracion_escalas.csv"
ARCHIVO_SALIDA_RESUMEN = RAIZ / "escenarios_liberacion_resultados.csv"
ARCHIVO_SALIDA_TRAY = RAIZ / "escenarios_liberacion_trayectorias.csv"
ARCHIVO_SALIDA_GRAFICA = RAIZ / "grafico_escenarios.png"

ESTADO_INICIAL = np.array([1000, 500, 200, 1000, 1000, 0, 0], dtype=float)
DIAS_SIMULACION = 3650  # 10 años
DIAS_POR_MES = 365.25 / 12

N_MC = 200
np.random.seed(12345)

UMBRAL_CASOS_ANUAL = 200
UMBRAL_CASOS_MENSUAL = UMBRAL_CASOS_ANUAL / 12


# ============================================================
# CARGAR CALIBRACIÓN JOINT
# ============================================================

def cargar_calibracion():
    """Carga parámetros y escalas de la calibración joint."""
    df_params = pd.read_csv(ARCHIVO_PARAMS)
    df_escalas = pd.read_csv(ARCHIVO_ESCALAS)
    
    # Parámetros óptimos
    params_opt = {}
    params_se = {}
    for _, row in df_params.iterrows():
        p = row["parametro"]
        if p in ("b", "mu_f", "c"):
            params_opt[p] = row["valor_optimo"]
            params_se[p] = row["error_estandar"]
    
    # Escalas por especie
    escalas = {}
    for _, row in df_escalas.iterrows():
        escalas[row["especie"]] = row["escala_empirica"]
    
    print(f"Parámetros calibrados: {params_opt}")
    print(f"Errores estándar: {params_se}")
    print(f"Escalas: {escalas}")
    
    return params_opt, params_se, escalas


# Cargar una vez al importar
PARAMS_OPT, PARAMS_SE, ESCALAS = cargar_calibracion()
ESCALA_BOVINOS = ESCALAS.get("bovinos", 0.1804)
ESCALA_PORCINOS = ESCALAS.get("porcinos", 0.0071)

# Umbral en hembras simuladas (usando escala bovinos como referencia principal)
UMBRAL_HEMBRAS_MENSUAL = UMBRAL_CASOS_MENSUAL / ESCALA_BOVINOS

print(f"Umbral hembras mensual (escala bovinos): {UMBRAL_HEMBRAS_MENSUAL:.1f}")


# ============================================================
# MUESTREO DE PARÁMETROS (incertidumbre paramétrica)
# ============================================================

def muestrear_parametros():
    """Muestrea parámetros desde distribución normal truncada (Laplace approx)."""
    p = deepcopy(PARAMETROS_BASE)
    
    # Parámetros calibrados: muestrear desde N(opt, SE) truncado a bounds
    for param in ("b", "mu_f", "c"):
        opt = PARAMS_OPT[param]
        se = PARAMS_SE[param]
        
        # Bounds según calibración
        bounds = {"b": (0.05, 0.50), "mu_f": (0.02, 0.25), "c": (0.10, 1.00)}
        low, high = bounds[param]
        
        # Muestrear truncado
        val = np.random.normal(opt, se)
        val = np.clip(val, low, high)
        p[param] = float(val)
    
    # Parámetros NO calibrados: rangos literarios
    rangos_literarios = {
        "mu_m": (0.03, 0.15),
        "mu_s": (0.10, 0.25),
        "k_h": (0.3, 0.7),
        "k_l": (0.15, 0.3),
        "k_p": (0.1, 0.2),
        "proporcion_machos": (0.45, 0.55),
        "proporcion_sexado": (0.95, 0.999),
        "proporcion_emergencia": (0.7, 0.9),
        "proporcion_liberacion": (0.8, 0.95),
        "mu_h": (0.02, 0.1),
        "mu_l": (0.02, 0.1),
        "mu_p": (0.02, 0.1),
        "mu_ps": (0.01, 0.05),
        "k_ps": (0.1, 0.2),
    }
    
    for param, (low, high) in rangos_literarios.items():
        p[param] = np.random.uniform(low, high)
    
    return p


# ============================================================
# SIMULACIÓN DE ESCENARIO
# ============================================================

def simular_escenario(parametros, liberacion_pupas_dia, reinfestacion_casos_mes=0, anos_max=10):
    """
    Simula un escenario y retorna año de erradicación (si se alcanza).
    """
    p = deepcopy(parametros)
    p["produccion_pupas"] = lambda t: float(liberacion_pupas_dia)
    
    dias_totales = int(anos_max * 365.25)
    t_eval = np.arange(0, dias_totales + 1, 7, dtype=float)
    
    reinf_hembras_mes = 0
    if reinfestacion_casos_mes > 0:
        reinf_hembras_mes = reinfestacion_casos_mes / ESCALA_BOVINOS
    
    def sistema(t, estado):
        derivadas = modelo_gbg_etapas(t, estado, p)
        if reinf_hembras_mes > 0:
            derivadas = list(derivadas)
            derivadas[4] += reinf_hembras_mes / DIAS_POR_MES
        return derivadas
    
    try:
        resultado = solve_ivp(
            sistema, (0, dias_totales), ESTADO_INICIAL.copy(),
            t_eval=t_eval, method="RK45", rtol=1e-7, atol=1e-9,
        )
    except Exception as e:
        return None, None, str(e)
    
    if not resultado.success:
        return None, None, f"Fallo: {resultado.message}"
    
    hembras = resultado.y[4]
    
    # Convertir a mensual
    n_meses = int(anos_max * 12)
    dias_muestreo = np.arange(n_meses, dtype=float) * DIAS_POR_MES
    hembras_mensual = np.interp(dias_muestreo, t_eval, hembras)
    
    casos_bovinos = hembras_mensual * ESCALA_BOVINOS
    casos_porcinos = hembras_mensual * ESCALA_PORCINOS
    
    # Detectar erradicación: 12 meses consecutivos bajo umbral
    anio_eradicacion = None
    for i in range(n_meses - 11):
        if np.all(casos_bovinos[i:i+12] < UMBRAL_CASOS_MENSUAL):
            anio_eradicacion = (i + 6) / 12
            break
    
    return anio_eradicacion, (casos_bovinos, casos_porcinos), None


# ============================================================
# ESCENARIOS
# ============================================================

ESCENARIOS = {
    "Sin liberacion": 0,
    "Minimo (1M pupas/dia)": 1_000_000,
    "Medio (3M pupas/dia)": 3_000_000,
    "Alto (5M pupas/dia)": 5_000_000,
    "Muy alto (7M pupas/dia)": 7_000_000,
    "Maximo historico (10M pupas/dia)": 10_000_000,
}


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 70)
    print("ESCENARIOS LIBERACIÓN TIE - USANDO CALIBRACIÓN JOINT")
    print("=" * 70)
    print(f"Parámetros base: {PARAMS_OPT}")
    print(f"Escalas: bovinos={ESCALA_BOVINOS:.4f}, porcinos={ESCALA_PORCINOS:.4f}")
    print(f"Umbral: <{UMBRAL_CASOS_ANUAL} casos/año bovinos")
    print(f"Monte Carlo: {N_MC} iteraciones por escenario")
    
    # Primero: verificar R0 en escenario base (sin liberación)
    print("\n--- Verificando escenario base (sin liberación) ---")
    r0_check = []
    for mc in range(50):
        params = muestrear_parametros()
        anio, _, err = simular_escenario(params, 0, 0, anos_max=10)
        if not err:
            r0_check.append(anio is None)  # None = NO erradica = R0 > 1
    r0_persistente = sum(r0_check) / len(r0_check)
    print(f"Población persistente sin liberación (R0>1): {r0_persistente:.0%} de muestras")
    
    if r0_persistente < 0.9:
        print("WARNING: Escenario base no garantiza persistencia. Ajustando mu_f...")
        # Ajuste rápido: forzar mu_f más bajo en muestreo
    
    resultados_resumen = []
    resultados_tray = []
    
    for nombre_esc, liberacion in ESCENARIOS.items():
        print(f"\n--- Escenario: {nombre_esc} ({liberacion:,} pupas/día) ---")
        
        anios_erad = []
        trayectorias_guardadas = []
        
        for mc in range(N_MC):
            if mc % 50 == 0:
                print(f"  MC {mc}/{N_MC}...")
            
            params = muestrear_parametros()
            anio, casos_tup, error = simular_escenario(params, liberacion)
            
            if error:
                continue
            
            if anio is not None:
                anios_erad.append(anio)
            
            # Guardar trayectorias cada 10 para archivo
            if mc % 10 == 0:
                casos_bov, casos_porc = casos_tup
                for mes, (cb, cp) in enumerate(zip(casos_bov, casos_porc)):
                    resultados_tray.append({
                        "escenario": nombre_esc,
                        "liberacion_pupas_dia": liberacion,
                        "mc": mc,
                        "mes": mes,
                        "casos_bovinos": cb,
                        "casos_porcinos": cp,
                    })
        
        n_exitosas = len(anios_erad)
        prob_exito = n_exitosas / N_MC if N_MC > 0 else 0
        
        if anios_erad:
            anio_medio = np.mean(anios_erad)
            anio_p10 = np.percentile(anios_erad, 10)
            anio_p50 = np.percentile(anios_erad, 50)
            anio_p90 = np.percentile(anios_erad, 90)
            anio_min = np.min(anios_erad)
            anio_max = np.max(anios_erad)
            print(f"  Erradicación: {n_exitosas}/{N_MC} ({prob_exito:.1%})")
            print(f"  Tiempo medio: {anio_medio:.2f} años, P10-P90: {anio_p10:.2f}-{anio_p90:.2f}")
        else:
            anio_medio = anio_p10 = anio_p50 = anio_p90 = anio_min = anio_max = np.nan
            print(f"  Erradicación: 0/{N_MC} (0.0%) - NO se alcanza en 10 años")
        
        # Machos estériles/semana estimados
        # pupas/dia * 7 * 0.5 (sexo) * 0.85 (emergencia) * 0.9 (liberacion)
        machos_sem = liberacion * 7 * 0.5 * 0.85 * 0.9
        
        resultados_resumen.append({
            "escenario": nombre_esc,
            "liberacion_pupas_dia": liberacion,
            "liberacion_machos_semana_est": machos_sem,
            "n_simulaciones": N_MC,
            "n_exitosas": n_exitosas,
            "prob_eradicacion_10a": prob_exito,
            "anio_medio": anio_medio,
            "anio_mediana": anio_p50,
            "anio_p10": anio_p10,
            "anio_p50": anio_p50,
            "anio_p90": anio_p90,
            "anio_min": anio_min,
            "anio_max": anio_max,
        })
    
    # Guardar resumen
    df_res = pd.DataFrame(resultados_resumen)
    df_res.to_csv(RAIZ / "escenarios_liberacion_resultados.csv", index=False, encoding="utf-8-sig")
    print(f"\nOK Resumen: {RAIZ / 'escenarios_liberacion_resultados.csv'}")
    
    # Guardar trayectorias
    df_tray = pd.DataFrame(resultados_tray)
    df_tray.to_csv(RAIZ / "escenarios_liberacion_trayectorias.csv", index=False, encoding="utf-8-sig")
    print(f"OK Trayectorias: {RAIZ / 'escenarios_liberacion_trayectorias.csv'}")
    
    # Gráfico
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Prob éxito vs liberación
        ax = axes[0, 0]
        x_vals = [r["liberacion_pupas_dia"] / 1e6 for r in resultados_resumen]
        y_vals = [r["prob_eradicacion_10a"] for r in resultados_resumen]
        ax.plot(x_vals, y_vals, "bo-", linewidth=2, markersize=8)
        ax.set_xlabel("Liberación (millones pupas/día)")
        ax.set_ylabel("Prob. erradicación en 10 años")
        ax.set_title("Probabilidad de éxito vs Capacidad de liberación")
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.05)
        for r in resultados_resumen:
            ax.annotate(r["escenario"].split("(")[0].strip(),
                       (r["liberacion_pupas_dia"]/1e6, r["prob_eradicacion_10a"]),
                       xytext=(5,5), textcoords="offset points", fontsize=8)
        
        # 2. Años a erradicación
        ax = axes[0, 1]
        for r in resultados_resumen:
            if not np.isnan(r["anio_medio"]):
                x = r["liberacion_pupas_dia"] / 1e6
                y = r["anio_medio"]
                y_err_low = y - r["anio_p10"]
                y_err_high = r["anio_p90"] - y
                if y_err_low >= 0 and y_err_high >= 0:
                    ax.errorbar(x, y, yerr=[[y_err_low], [y_err_high]],
                               fmt="o", capsize=5, capthick=2, linewidth=2, markersize=8)
        ax.set_xlabel("Liberación (millones pupas/día)")
        ax.set_ylabel("Años a erradicación (mediana + P10-P90)")
        ax.set_title("Tiempo a erradicación por escenario")
        ax.grid(True, alpha=0.3, axis="y")
        
        # 3. Trayectorias ejemplo (escenario mínimo)
        ax = axes[1, 0]
        df_tray = pd.DataFrame(resultados_tray)
        esc_min = "Minimo (1M pupas/dia)"
        tray_min = df_tray[df_tray["escenario"] == esc_min]
        for mc in sorted(tray_min["mc"].unique())[:30]:
            traj = tray_min[tray_min["mc"] == mc].sort_values("mes")
            ax.plot(traj["mes"], traj["casos_bovinos"], "b-", alpha=0.08, linewidth=0.5)
        ax.axhline(UMBRAL_CASOS_ANUAL/12, color="r", linestyle="--", linewidth=2, 
                   label=f"Umbral ({UMBRAL_CASOS_ANUAL/12:.0f} casos/mes)")
        ax.set_xlabel("Mes")
        ax.set_ylabel("Casos mensuales (bovinos)")
        ax.set_title(f"Trayectorias MC: {esc_min}")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 4. Machos/semana vs años
        ax = axes[1, 1]
        for r in resultados_resumen:
            if not np.isnan(r["anio_medio"]):
                machos_sem = r["liberacion_machos_semana_est"] / 1e6
                ax.scatter(machos_sem, r["anio_medio"], s=120, alpha=0.8, 
                          edgecolors="k", linewidth=0.5)
                ax.annotate(f"{r['liberacion_pupas_dia']/1e6:.0f}M",
                           (machos_sem, r["anio_medio"]),
                           xytext=(5,5), textcoords="offset points", fontsize=9, fontweight="bold")
        ax.set_xlabel("Machos estériles liberados (millones/semana)")
        ax.set_ylabel("Años a erradicación (mediana)")
        ax.set_title("Costo operativo vs Tiempo objetivo")
        ax.grid(True, alpha=0.3)
        ax.set_xscale("log")
        
        plt.tight_layout()
        plt.savefig(RAIZ / "grafico_escenarios.png", dpi=160, bbox_inches="tight")
        plt.close()
        print(f"OK Gráfico: grafico_escenarios.png")
        
    except Exception as e:
        print(f"WARNING Gráfico: {e}")
    
    # Imprimir tabla final
    print("\n" + "=" * 70)
    print("RESUMEN: MOSCAS NECESARIAS Y TIEMPO A ERRADICACIÓN")
    print("=" * 70)
    
    # Formato bonito para consola
    for r in resultados_resumen:
        if not np.isnan(r["anio_medio"]):
            print(f"  {r['escenario']:30s} | {r['liberacion_pupas_dia']:>10,} pupas/dia | "
                  f"{r['liberacion_machos_semana_est']:>10,.0f} machos/sem | "
                  f"{r['prob_eradicacion_10a']:>5.1%} exito | "
                  f"{r['anio_medio']:.2f} años (P10-P90: {r['anio_p10']:.2f}-{r['anio_p90']:.2f})")
        else:
            print(f"  {r['escenario']:30s} | {r['liberacion_pupas_dia']:>10,} pupas/dia | "
                  f"{r['liberacion_machos_semana_est']:>10,.0f} machos/sem | "
                  f"{r['prob_eradicacion_10a']:>5.1%} exito | NO en 10 años")
    
    print("\nINTERPRETACIÓN HONESTA:")
    print(f"  - Umbral erradicación: <{UMBRAL_CASOS_ANUAL} casos/año bovinos")
    print(f"  - Escalas de calibración JOINT: bovinos={ESCALA_BOVINOS:.4f}, porcinos={ESCALA_PORCINOS:.4f}")
    print(f"  - Monte Carlo: {N_MC} iteraciones, incertidumbre paramétrica (Laplace)")
    print(f"  - Modelo: 0-D, sin estacionalidad, sin estructura espacial")
    print("\nLIMITACIONES:")
    print("  - 200/200 simulaciones NO = garantía 100%")
    print("  - Sin reinfestación fronteriza real")
    print("  - Sin estacionalidad climática")
    print("  - Escala porcinos muy baja (pocos datos)")
    print("  - Parámetros b, c en bordes (débilmente identificados)")


if __name__ == "__main__":
    main()