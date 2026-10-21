
from pathlib import Path

import pandas as pd

from src.modelo.parametros import PARAMETROS


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ENTRADA = BASE_DIR / "resultados_modelo_etapas.csv"
ARCHIVO_SALIDA = BASE_DIR / "analisis_flujos_planta.csv"

# Parámetros actuales del modelo (hipotéticos)



def main():
    if not ARCHIVO_ENTRADA.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO_ENTRADA}\n"
            "Ejecuta primero: python -m scripts.graficar_modelo_etapas"
        )

    df = pd.read_csv(ARCHIVO_ENTRADA)

    columnas_necesarias = {
        "dia",
        "pupas_planta",
        "machos_esteriles_campo",
    }

    faltantes = columnas_necesarias - set(df.columns)

    if faltantes:
        raise ValueError(
            f"Faltan columnas en el CSV: {sorted(faltantes)}"
        )

    # Convertir columnas a valores numéricos
    for columna in columnas_necesarias:
        df[columna] = pd.to_numeric(
            df[columna], errors="coerce"
        )

    df = df.dropna(
        subset=[
            "dia",
            "pupas_planta",
            "machos_esteriles_campo",
        ]
    ).sort_values("dia")

    # Flujo de procesamiento y liberación
        # Obtener parámetros del archivo central
    k_ps = PARAMETROS["k_ps"]
    mu_s = PARAMETROS["mu_s"]

    proporcion_sexado = PARAMETROS["proporcion_sexado"]
    proporcion_emergencia = PARAMETROS["proporcion_emergencia"]
    proporcion_liberacion = PARAMETROS["proporcion_liberacion"]

    # Flujo de procesamiento y liberación
    df["pupas_procesadas_por_dia"] = (
        k_ps * df["pupas_planta"]
    )

    fraccion_final = (
        proporcion_sexado
        * proporcion_emergencia
        * proporcion_liberacion
    )

    df["machos_liberados_por_dia"] = (
        df["pupas_procesadas_por_dia"] * fraccion_final
    )

    # Pérdidas instantáneas según la mortalidad del modelo
    df["perdida_machos_por_dia"] = (
        mu_s * df["machos_esteriles_campo"]
    )

    # Pérdidas instantáneas según la mortalidad del modelo
    df["perdida_machos_por_dia"] = (
        mu_s * df["machos_esteriles_campo"]
    )

    # Cambio instantáneo estimado en la población de campo
    df["cambio_neto_por_dia"] = (
        df["machos_liberados_por_dia"]
        - df["perdida_machos_por_dia"]
    )

    df["tendencia_instantanea"] = df[
        "cambio_neto_por_dia"
    ].apply(
        lambda x: (
            "aumenta" if x > 0
            else "disminuye" if x < 0
            else "equilibrio instantáneo"
        )
    )

    # Guardar los resultados
    df.to_csv(
        ARCHIVO_SALIDA,
        index=False,
        encoding="utf-8-sig",
    )

    # Mostrar puntos de referencia
    indices = sorted(set([
        df.index[0],
        df.index[len(df) // 3],
        df.index[(2 * len(df)) // 3],
        df.index[-1],
    ])) if not df.empty else []

    columnas_mostrar = [
        "dia",
        "pupas_planta",
        "pupas_procesadas_por_dia",
        "machos_liberados_por_dia",
        "machos_esteriles_campo",
        "perdida_machos_por_dia",
        "cambio_neto_por_dia",
        "tendencia_instantanea",
    ]

    print("\nANÁLISIS DE FLUJOS DE LA SIMULACIÓN")
    print(df.loc[indices, columnas_mostrar].to_string(index=False))
    print(f"\nArchivo guardado: {ARCHIVO_SALIDA}")
    print(
        "\nAviso: los resultados dependen de parámetros hipotéticos. "
        "No son una recomendación de liberación real."
    )


if __name__ == "__main__":
    main()
