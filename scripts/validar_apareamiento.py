
import pandas as pd

from src.modelo.parametros import PARAMETROS


def calcular_huevos(b, hembras, machos_silvestres,
                    machos_esteriles, competencia):
    denominador = machos_silvestres + competencia * machos_esteriles

    if denominador <= 0:
        return 0.0

    return b * hembras * machos_silvestres / denominador


def main():
    b = PARAMETROS["b"]
    c = PARAMETROS["c"]

    # Valores iniciales hipotéticos del modelo.
    hembras = 1000.0
    machos_silvestres = 1000.0

    niveles_esteriles = [0, 100, 500, 1000, 5000]

    huevos_sin_liberacion = calcular_huevos(
        b, hembras, machos_silvestres, 0, c
    )

    resultados = []

    for esteriles in niveles_esteriles:
        huevos = calcular_huevos(
            b, hembras, machos_silvestres, esteriles, c
        )

        reduccion = (
            100 * (1 - huevos / huevos_sin_liberacion)
            if huevos_sin_liberacion > 0
            else 0
        )

        resultados.append({
            "machos_esteriles": esteriles,
            "reproduccion_modelada": huevos,
            "reduccion_pct": reduccion,
        })

    df = pd.DataFrame(resultados)

    print("\nVALIDACIÓN DE LA ECUACIÓN DE APAREAMIENTO")
    print(df.to_string(index=False, float_format=lambda x: f"{x:.2f}"))

    # Comprobación: la reproducción debe disminuir al aumentar
    # los machos estériles, manteniendo las otras variables fijas.
    valores = df["reproduccion_modelada"].to_numpy()

    if all(valores[i + 1] < valores[i] for i in range(len(valores) - 1)):
        print("\nOK: la reproducción disminuye en todos los niveles probados.")
    else:
        raise AssertionError(
            "La reproducción no disminuye de forma monotónica."
        )

    df.to_csv(
        "validacion_apareamiento.csv",
        index=False,
        encoding="utf-8-sig",
    )
    print("\nArchivo generado: validacion_apareamiento.csv")


if __name__ == "__main__":
    main()


