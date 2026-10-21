
from copy import deepcopy
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS


# Configuración de la simulación
DIAS = 180
ESTADO_INICIAL = [1000, 500, 200, 1000, 1000, 0, 0]

# Entradas constantes hipotéticas de machos estériles por día.
# Son valores de prueba, NO recomendaciones operativas.
ESCENARIOS = {
    "Sin liberación": 0,
    "Baja (prueba)": 100,
    "Media (prueba)": 500,
    "Alta (prueba)": 1000,
}


def simular(nombre, liberacion_diaria):
    parametros = deepcopy(PARAMETROS)

    # Apagamos la producción de pupas de la planta para aislar
    # el efecto de la entrada directa de machos estériles.
    parametros["produccion_pupas"] = lambda t: 0.0

    def modelo_con_liberacion(t, estado):
        derivadas = modelo_gbg_etapas(t, estado, parametros)

        # Orden del estado:
        # [H, L, P, Mw, Fw, Ps, Ms]
        # Agregamos machos estériles directamente a Ms.
        derivadas = np.array(derivadas, dtype=float)
        derivadas[6] += liberacion_diaria

        return derivadas

    tiempos = np.arange(DIAS + 1, dtype=float)

    resultado = solve_ivp(
        modelo_con_liberacion,
        (0, DIAS),
        ESTADO_INICIAL,
        t_eval=tiempos,
        rtol=1e-7,
        atol=1e-9,
    )

    if not resultado.success:
        raise RuntimeError(
            f"Falló el escenario '{nombre}': {resultado.message}"
        )

    # Evita mostrar pequeñas cantidades negativas por error numérico.
    valores = np.maximum(resultado.y, 0)

    return pd.DataFrame({
        "dia": tiempos.astype(int),
        "escenario": nombre,
        "hembras_silvestres": valores[4],
        "machos_silvestres": valores[3],
        "machos_esteriles": valores[6],
        "liberacion_diaria": liberacion_diaria,
    })


def main():
    carpeta_salida = Path("resultados_liberaciones")
    carpeta_salida.mkdir(exist_ok=True)

    resultados = []

    for nombre, tasa in ESCENARIOS.items():
        df = simular(nombre, tasa)
        resultados.append(df)

    datos = pd.concat(resultados, ignore_index=True)

    # Guardar trayectorias completas
    ruta_csv = carpeta_salida / "trayectorias_liberaciones.csv"
    datos.to_csv(ruta_csv, index=False, encoding="utf-8-sig")

    # Resumen de hembras silvestres
    dias_resumen = [30, 90, 180]
    resumen = (
        datos[datos["dia"].isin(dias_resumen)]
        .pivot(
            index="escenario",
            columns="dia",
            values="hembras_silvestres",
        )
        .rename_axis(columns="dia")
        .reset_index()
    )

    resumen.columns = [
        "escenario"
        if columna == "escenario"
        else f"hembras_dia_{columna}"
        for columna in resumen.columns
    ]

    ruta_resumen = carpeta_salida / "resumen_liberaciones.csv"
    resumen.to_csv(ruta_resumen, index=False, encoding="utf-8-sig")

    print("\nHEMBRAS SILVESTRES POR ESCENARIO")
    print(resumen.to_string(index=False, float_format=lambda x: f"{x:.4f}"))

    print("\nMACHOS ESTÉRILES Y LIBERACIÓN TOTAL")
    for nombre, tasa in ESCENARIOS.items():
        total = tasa * DIAS
        print(
            f"{nombre}: {tasa} machos/día; "
            f"{total} machos durante {DIAS} días"
        )

    # Gráfica de hembras silvestres
    plt.figure(figsize=(10, 6))

    for nombre in ESCENARIOS:
        grupo = datos[datos["escenario"] == nombre]
        plt.plot(
            grupo["dia"],
            grupo["hembras_silvestres"],
            label=nombre,
        )

    plt.xlabel("Día")
    plt.ylabel("Hembras silvestres (unidades del modelo)")
    plt.title("Respuesta del modelo a distintas entradas de machos estériles")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta_grafica = carpeta_salida / "hembras_por_liberacion.png"
    plt.savefig(ruta_grafica, dpi=160)
    plt.close()

    print("\nArchivos generados:")
    print(ruta_csv.resolve())
    print(ruta_resumen.resolve())
    print(ruta_grafica.resolve())

    print(
        "\nIMPORTANTE: simulación hipotética. "
        "No estima liberaciones necesarias en México."
    )


if __name__ == "__main__":
    main()
