from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "calibracion_modelo_etapas.csv"

def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(f"No se encontró: {ARCHIVO}")

    datos = pd.read_csv(ARCHIVO)
    datos["periodo"] = pd.to_datetime(
        datos["periodo"], format="%Y-%m", errors="coerce"
    )

    for hospedador in ("bovinos", "porcinos"):
        serie = datos[datos["hospedador"] == hospedador].sort_values("periodo")
        if serie.empty:
            print(f"No hay datos para {hospedador}")
            continue

        plt.figure(figsize=(10, 5))
        plt.plot(
            serie["periodo"], serie["casos_observados"],
            marker="o", label="Casos observados"
        )
        plt.plot(
            serie["periodo"], serie["casos_ajustados"],
            marker="s", linestyle="--", label="Casos ajustados"
        )
        plt.title(f"Calibración exploratoria: {hospedador}")
        plt.xlabel("Mes")
        plt.ylabel("Casos reportados")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        salida = RAIZ / f"calibracion_etapas_{hospedador}.png"
        plt.savefig(salida, dpi=150)
        plt.close()
        print(f"Gráfica generada: {salida}")

if __name__ == "__main__":
    main()
