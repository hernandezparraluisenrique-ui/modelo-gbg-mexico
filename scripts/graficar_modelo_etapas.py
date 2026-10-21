
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from src.modelo.parametros import PARAMETROS

from src.modelo.modelo_etapas import modelo_gbg_etapas



# Parámetros ficticios: solo para probar la gráfica.
parametros = PARAMETROS

# Orden: H, L, P, Mw, Fw, Ps, Ms
estado_inicial = [
    1000, 500, 200, 1000, 1000, 0, 0
]

tiempo = np.linspace(0, 30, 301)

resultado = solve_ivp(
    fun=lambda t, estado: modelo_gbg_etapas(
        t, estado, parametros
    ),
    t_span=(0, 30),
    y0=estado_inicial,
    t_eval=tiempo,
    method="RK45",
)

if not resultado.success:
    raise RuntimeError(resultado.message)

nombres = [
    "Huevos silvestres",
    "Larvas silvestres",
    "Pupas silvestres",
    "Machos silvestres",
    "Hembras silvestres",
    "Pupas en proceso de planta",
    "Machos estériles en campo",
]

# Dos gráficas para distinguir el ciclo silvestre
# del proceso industrial.
fig, ejes = plt.subplots(2, 1, figsize=(11, 9))

for i in range(5):
    ejes[0].plot(
        resultado.t,
        resultado.y[i],
        label=nombres[i],
    )

ejes[0].set_title("Ciclo silvestre de GBG")
ejes[0].set_xlabel("Días")
ejes[0].set_ylabel("Cantidad modelada")
ejes[0].legend()
ejes[0].grid(True)

ejes[1].plot(
    resultado.t,
    resultado.y[5],
    label=nombres[5],
)
ejes[1].plot(
    resultado.t,
    resultado.y[6],
    label=nombres[6],
)

ejes[1].set_title("Proceso de planta y machos estériles")
ejes[1].set_xlabel("Días")
ejes[1].set_ylabel("Cantidad modelada")
ejes[1].legend()
ejes[1].grid(True)

plt.tight_layout()
plt.savefig("evolucion_modelo_etapas.png", dpi=150)


# Guardar los resultados numéricos en un CSV
import pandas as pd

datos = {
    "dia": resultado.t,
    "huevos_silvestres": resultado.y[0],
    "larvas_silvestres": resultado.y[1],
    "pupas_silvestres": resultado.y[2],
    "machos_silvestres": resultado.y[3],
    "hembras_silvestres": resultado.y[4],
    "pupas_planta": resultado.y[5],
    "machos_esteriles_campo": resultado.y[6],
}

df = pd.DataFrame(datos)
df.to_csv(
    "resultados_modelo_etapas.csv",
    index=False,
    encoding="utf-8-sig",
)

print("Resultados guardados en resultados_modelo_etapas.csv")

plt.show()




print("Gráfica guardada como evolucion_modelo_etapas.png")
