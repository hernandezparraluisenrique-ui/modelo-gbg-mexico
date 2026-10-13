
from src.simulacion.simulador import ejecutar_simulacion


def comparar_supervivencia(parametros_base, estado_inicial, tiempo, vidas_medias):
    """
    Compara simulaciones con diferentes duraciones medias
    esperadas de vida de los machos estériles, expresadas en días.
    """
    resultados = {}

    for vida_media in vidas_medias:
        if vida_media <= 0:
            raise ValueError("La vida media debe ser mayor que cero.")

        parametros = parametros_base.copy()
        parametros["mus"] = 1.0 / vida_media

        resultado = ejecutar_simulacion(
            parametros,
            estado_inicial,
            tiempo
        )

        if not resultado.success:
            raise RuntimeError(
                f"Falló la simulación para una duración de "
                f"{vida_media} días: {resultado.message}"
            )

        resultados[vida_media] = resultado

    return resultados