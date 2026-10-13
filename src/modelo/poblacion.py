
def modelo_gbg(t, estado, parametros):
    # Poblaciones:
    # Mw = machos silvestres
    # Fw = hembras silvestres
    # Ms = machos estériles
    Mw, Fw, Ms = estado

    # Parámetros biológicos
    b = parametros["b"]
    muM = parametros["muM"]
    muF = parametros["muF"]
    mus = parametros["mus"]
    c = parametros["c"]
    R = parametros["R"](t)

    # Evitar poblaciones negativas por pequeños errores numéricos
    Mw = max(0.0, Mw)
    Fw = max(0.0, Fw)
    Ms = max(0.0, Ms)

    # Proporción de apareamientos con machos silvestres
    denominador = Mw + c * Ms

    if denominador > 0:
        pw = Mw / denominador
    else:
        pw = 0.0

    # Reproducción: solo los apareamientos con machos
    # silvestres generan descendencia viable en este modelo
    nacimientos = b * Fw * pw

    proporcion_machos = parametros.get("proporcion_machos", 0.5)
    proporcion_hembras = 1.0 - proporcion_machos

    nuevos_machos = proporcion_machos * nacimientos
    nuevas_hembras = proporcion_hembras * nacimientos

    # Cambios diarios de las poblaciones
    dMw_dt = nuevos_machos - muM * Mw
    dFw_dt = nuevas_hembras - muF * Fw
    dMs_dt = R - mus * Ms

    return [dMw_dt, dFw_dt, dMs_dt]
