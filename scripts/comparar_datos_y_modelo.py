
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

ARCHIVO_CASOS = BASE_DIR / "resumen_mensual.csv"
ARCHIVO_MODELO = BASE_DIR / "resultados_modelo_etapas.csv"

ARCHIVO_TABLA = BASE_DIR / "resumen_comparacion.csv"
ARCHIVO_GRAFICA = BASE_DIR / "comparacion_datos_y_modelo.png"


def main():
    # 1. Comprobar que existen los archivos
    if not ARCHIVO_CASOS.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO_CASOS}"
        )

    if not ARCHIVO_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO_MODELO}"
        )

    # 2. Leer los datos
    casos = pd.read_csv(ARCHIVO_CASOS)
    modelo = pd.read_csv(ARCHIVO_MODELO)

    # 3. Verificar las columnas necesarias
    columnas_casos = {"periodo", "bovinos", "porcinos"}
    
    columnas_modelo = {
        "dia",
        "huevos_silvestres",
        "larvas_silvestres",
        "pupas_silvestres",
        "machos_silvestres",
        "hembras_silvestres",
        "pupas_planta",
        "machos_esteriles_campo",
    }


    if not columnas_casos.issubset(casos.columns):
        raise ValueError(
            f"Faltan columnas en casos. Columnas encontradas: "
            f"{list(casos.columns)}"
        )

    if not columnas_modelo.issubset(modelo.columns):
        raise ValueError(
            f"Faltan columnas en el modelo. Columnas encontradas: "
            f"{list(modelo.columns)}"
        )

    # 4. Preparar los datos observados
    casos["periodo"] = casos["periodo"].astype(str)
    casos["bovinos"] = pd.to_numeric(
        casos["bovinos"], errors="coerce"
    )
    casos["porcinos"] = pd.to_numeric(
        casos["porcinos"], errors="coerce"
    )

    # Los totales bovinos incompletos no se consideran definitivos
    if "bovinos_completo" in casos.columns:
        casos.loc[
            casos["bovinos_completo"].eq("no"), "bovinos"
        ] = float("nan")

    # 5. Preparar los resultados del modelo
    
    columnas_etapas = [
        "huevos_silvestres",
        "larvas_silvestres",
        "pupas_silvestres",
        "machos_silvestres",
        "hembras_silvestres",
        "pupas_planta",
        "machos_esteriles_campo",
    ]


    for columna in ["dia"] + columnas_etapas:
        modelo[columna] = pd.to_numeric(
            modelo[columna], errors="coerce"
        )

    modelo = modelo.dropna(subset=["dia"]).sort_values("dia")

    # 6. Guardar una tabla de casos y otra de resultados del modelo
    # Se conservan por separado porque sus unidades son diferentes.
    casos.to_csv(
        ARCHIVO_TABLA.with_name("tabla_casos_observados.csv"),
        index=False,
        encoding="utf-8-sig"
    )

    modelo.to_csv(
        ARCHIVO_TABLA.with_name("tabla_resultados_modelo.csv"),
        index=False,
        encoding="utf-8-sig"
    )

    # 7. Crear una figura con dos paneles independientes
    fig, ejes = plt.subplots(2, 1, figsize=(13, 10))

    # Panel superior: casos mensuales observados
    ejes[0].plot(
        casos["periodo"], casos["bovinos"],
        marker="o", label="Bovinos"
    )
    ejes[0].plot(
        casos["periodo"], casos["porcinos"],
        marker="s", label="Porcinos"
    )
    ejes[0].set_title("Casos mensuales registrados")
    ejes[0].set_xlabel("Mes")
    ejes[0].set_ylabel("Casos registrados")
    ejes[0].tick_params(axis="x", rotation=60)
    ejes[0].grid(True, alpha=0.3)
    ejes[0].legend()

    # Panel inferior: trayectoria simulada por etapas
    for columna in columnas_etapas:
        ejes[1].plot(
            modelo["dia"], modelo[columna], label=columna
        )

    ejes[1].set_title(
        "Modelo hipotético por etapas (simulación de 30 días)"
    )
    ejes[1].set_xlabel("Día de simulación")
    ejes[1].set_ylabel("Valor de la variable del modelo")
    ejes[1].grid(True, alpha=0.3)
    ejes[1].legend(ncol=4)

    fig.suptitle(
        "Datos observados y modelo GBG: escalas separadas",
        fontsize=14
    )
    fig.tight_layout()
    fig.savefig(ARCHIVO_GRAFICA, dpi=150)
    plt.close(fig)

    print("Análisis terminado correctamente.")
    print(f"Meses de casos observados: {len(casos)}")
    print(f"Filas de simulación: {len(modelo)}")
    print(
        "Tabla de casos:",
        ARCHIVO_TABLA.with_name("tabla_casos_observados.csv")
    )
    print(
        "Tabla del modelo:",
        ARCHIVO_TABLA.with_name("tabla_resultados_modelo.csv")
    )
    print("Gráfica:", ARCHIVO_GRAFICA)
    print(
        "\nNota: las dos series se muestran por separado. "
        "Los casos registrados no equivalen a la abundancia "
        "de moscas y los parámetros del modelo son hipotéticos."
    )


if __name__ == "__main__":
    main()
