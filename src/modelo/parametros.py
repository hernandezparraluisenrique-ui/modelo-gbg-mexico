
# Parámetros ficticios: solo para probar el modelo.
# No representan mediciones reales de una planta de GBG.

def produccion_pupas(t):
    return 1000.0


PARAMETROS = {
    "b": 0.1,
    "k_h": 1 / 2,
    "k_l": 1 / 5,
    "k_p": 1 / 7,
    "mu_h": 0.05,
    "mu_l": 0.05,
    "mu_p": 0.05,
    "mu_m": 0.1,
    "mu_f": 0.1,
    "mu_ps": 0.03,
    "mu_s": 1 / 7,
    "c": 1.0,
    "proporcion_machos": 0.5,
    "produccion_pupas": produccion_pupas,
    "proporcion_sexado": 0.5,
    "proporcion_emergencia": 0.8,
    "proporcion_liberacion": 0.9,
    "k_ps": 1 / 7,
}
