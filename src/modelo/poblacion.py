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

    # =========================================
    # 1. VARIABLES DEL ESTADO
    # =========================================

    Mw, Fw, Ms = estado

    # =========================================
    # 2. PARÁMETROS
    # =========================================

    b = parametros["b"]

    muM = parametros["muM"]
    muF = parametros["muF"]
    mus = parametros["mus"]

    c = parametros["c"]

    R = parametros["R"]

    # =========================================
    # 3. COMPETENCIA ENTRE MACHOS
    # =========================================

    denominador = Mw + c * Ms

    if denominador > 0:

        pw = Mw / denominador

        ps = (c * Ms) / denominador

    else:

        pw = 0.0
        ps = 0.0

    # =========================================
    # 4. DESCENDENCIA VIABLE
    # =========================================

    Bv = b * Fw * pw

    # =========================================
    # 5. NUEVOS MACHOS Y HEMBRAS
    # =========================================

    proporcion_machos = 0.5
    proporcion_hembras = 0.5

    nuevos_machos = proporcion_machos * Bv
    nuevas_hembras = proporcion_hembras * Bv

    # =========================================
    # 6. ECUACIONES DIFERENCIALES
    # =========================================

    dMw_dt = nuevos_machos - muM * Mw

    dFw_dt = nuevas_hembras - muF * Fw

    dMs_dt = R - mus * Ms

    # =========================================
    # 7. RETORNAR TASAS DE CAMBIO
    # =========================================

    return [
        dMw_dt,
        dFw_dt,
        dMs_dt
    ]