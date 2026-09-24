def modelo_gbg(t, estado, parametros):
    """
    Modelo simplificado de la dinámica poblacional
    del gusano barrenador del ganado (Cochliomyia hominivorax).

    Estado
    ------
    [Mw, Fw, Ms]

    Mw = machos silvestres
    Fw = hembras silvestres
    Ms = machos estériles
    """

    Mw, Fw, Ms = estado

    # =========================================
    # PARÁMETROS
    # =========================================

    b = parametros["b"]

    muM = parametros["muM"]
    muF = parametros["muF"]
    mus = parametros["mus"]

    c = parametros["c"]

    # =========================================
    # LIBERACIÓN DE MACHOS ESTÉRILES
    # =========================================

    funcion_liberacion = parametros["R"]

    R = funcion_liberacion(t)

    # =========================================
    # PROPORCIÓN DE APAREAMIENTO
    # =========================================

    denominador = Mw + c * Ms

    if denominador > 0:

        pw = Mw / denominador

    else:

        pw = 0.0

    # =========================================
    # REPRODUCCIÓN
    # =========================================

    Bv = b * Fw * pw

    proporcion_machos = 0.5
    proporcion_hembras = 0.5

    nuevos_machos = proporcion_machos * Bv
    nuevas_hembras = proporcion_hembras * Bv

    # =========================================
    # ECUACIONES DIFERENCIALES
    # =========================================

    dMw_dt = (
        nuevos_machos
        - muM * Mw
    )

    dFw_dt = (
        nuevas_hembras
        - muF * Fw
    )

    dMs_dt = (
        R
        - mus * Ms
    )

    return [
        dMw_dt,
        dFw_dt,
        dMs_dt
    ]