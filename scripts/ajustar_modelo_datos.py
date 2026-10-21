
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import least_squares

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "serie_mensual_analisis.csv"
SALIDA = RAIZ / "ajuste_casos_modelo.csv"
GRAFICA = RAIZ / "ajuste_casos_modelo.png"


def curva(t, nivel, tasa, base):
    """Curva exploratoria para describir la tendencia de casos."""
    return base + nivel * np.exp(np.clip(tasa * t, -30, 30))


def main():
    df = pd.read_csv(ENTRADA)

    # Excluir meses bovinos incompletos. Los porcinos se incluyen
    # cuando su registro está completo.
    bovinos = pd.to_numeric(df["bovinos"], errors="coerce")
    porcinos = pd.to_numeric(df["porcinos"], errors="coerce")

    df["casos_validos"] = bovinos.fillna(0) + porcinos.fillna(0)
    df["hay_dato"] = bovinos.notna() | porcinos.notna()

    df = df[df["hay_dato"]].copy().reset_index(drop=True)

    if len(df) < 5:
        raise ValueError("No hay suficientes meses con datos válidos.")

    t = np.arange(len(df), dtype=float)
    y = df["casos_validos"].to_numpy(dtype=float)

    # Ajustar una tendencia exponencial con nivel, tasa y base.
    # Se usa log(1 + casos) para reducir el peso de los picos.
    objetivo = np.log1p(y)

    def residuos(p):
        nivel, tasa, base = p
        pred = curva(t, nivel, tasa, base)
        return np.log1p(pred) - objetivo

    ajuste = least_squares(
        residuos,
        x0=[max(float(np.median(y)), 1.0), 0.0, 0.0],
        bounds=([0.0, -1.0, 0.0], [1e7, 1.0, 1e7]),
        loss="soft_l1",
    )

    nivel, tasa, base = ajuste.x
    estimados = curva(t, nivel, tasa, base)

    df["indice_mes"] = t.astype(int)
    df["casos_estimados_tendencia"] = estimados
    df["residuo_casos"] = y - estimados
    df["tipo_ajuste"] = "tendencia exploratoria; no es población de moscas"

    df.to_csv(SALIDA, index=False, encoding="utf-8-sig")

    plt.figure(figsize=(11, 6))
    plt.plot(df["periodo"], y, marker="o", label="Casos observados disponibles")
    plt.plot(
        df["periodo"],
        estimados,
        linestyle="--",
        label="Tendencia ajustada",
    )
    plt.xticks(rotation=60)
    plt.ylabel("Casos animales reportados")
    plt.xlabel("Mes")
    plt.title("Casos observados y tendencia ajustada del GBG")
    plt.legend()
    plt.tight_layout()
    plt.savefig(GRAFICA, dpi=160)
    plt.close()

    print("Ajuste terminado:", ajuste.success)
    print(f"Meses incluidos: {len(df)}")
    print(f"Parámetros de tendencia: nivel={nivel:.3f}, tasa={tasa:.5f}, base={base:.3f}")
    print(f"Archivo de resultados: {SALIDA}")
    print(f"Gráfica: {GRAFICA}")
    print(
        "Nota: la curva describe casos reportados; no estima directamente "
        "el número de hembras silvestres ni el efecto causal de liberaciones."
    )


if __name__ == "__main__":
    main()
