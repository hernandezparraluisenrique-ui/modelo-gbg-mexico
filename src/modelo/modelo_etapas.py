
def modelo_gbg_etapas(t, estado, parametros):
    """
    Modelo simplificado por etapas.

    Población silvestre:
    H  = huevos
    L  = larvas
    P  = pupas
    Mw = machos adultos silvestres
    Fw = hembras adultas silvestres

    Proceso de planta simplificado:
    Ps = pupas disponibles para producir machos estériles
    Ms = machos estériles adultos liberados en campo

    Todas las tasas se expresan por día.
    """

    H, L, P, Mw, Fw, Ps, Ms = estado

    # Parámetros del ciclo silvestre
    b = parametros["b"]
    k_h = parametros["k_h"]
    k_l = parametros["k_l"]
    k_p = parametros["k_p"]

    mu_h = parametros["mu_h"]
    mu_l = parametros["mu_l"]
    mu_p = parametros["mu_p"]
    mu_m = parametros["mu_m"]
    mu_f = parametros["mu_f"]
    mu_ps = parametros["mu_ps"]
    mu_s = parametros["mu_s"]

    # Competitividad de los machos estériles
    c = parametros["c"]
    proporcion_machos = parametros.get("proporcion_machos", 0.5)

    # Flujo de pupas que la planta aporta por día.
    # Este dato debe proceder de información real de producción.
    produccion_pupas = max(
        0.0, parametros["produccion_pupas"](t)
    )

    # Fracciones del proceso industrial.
    proporcion_sexado = parametros["proporcion_sexado"]
    proporcion_emergencia = parametros["proporcion_emergencia"]
    proporcion_liberacion = parametros["proporcion_liberacion"]

    # Evitar valores negativos por errores numéricos
    H, L, P, Mw, Fw, Ps, Ms = [
        max(0.0, x) for x in (H, L, P, Mw, Fw, Ps, Ms)
    ]

    # Proporción de apareamientos con machos silvestres.
    denominador = Mw + c * Ms
    if denominador > 0:
        proporcion_silvestre = Mw / denominador
    else:
        proporcion_silvestre = 0.0

    # Huevos producidos por hembras silvestres.
    huevos = b * Fw * proporcion_silvestre

    # Desarrollo silvestre: huevos -> larvas -> pupas -> adultos
    dH_dt = huevos - (k_h + mu_h) * H
    dL_dt = k_h * H - (k_l + mu_l) * L
    dP_dt = k_l * L - (k_p + mu_p) * P

    adultos_nuevos = k_p * P
    dMw_dt = proporcion_machos * adultos_nuevos - mu_m * Mw
    dFw_dt = (1.0 - proporcion_machos) * adultos_nuevos - mu_f * Fw

    # Planta: entrada de pupas al inventario de proceso.
    # La salida depende de las pupas disponibles y su tasa de desarrollo.
    k_ps = parametros["k_ps"]
    pupas_procesadas = k_ps * Ps

    dPs_dt = produccion_pupas - (k_p + mu_ps) * Ps

    # Fracción estimada que emerge como machos y llega a liberación.
    machos_liberados = (
        pupas_procesadas
        * proporcion_sexado
        * proporcion_emergencia
        * proporcion_liberacion
    )

    dMs_dt = machos_liberados - mu_s * Ms

    return [
        dH_dt,
        dL_dt,
        dP_dt,
        dMw_dt,
        dFw_dt,
        dPs_dt,
        dMs_dt,
    ]
