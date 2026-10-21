
from pathlib import Path
import pandas as pd

carpeta = Path("resultados_liberaciones")
archivo = carpeta / "trayectorias_liberaciones.csv"
salida = carpeta / "informe_resultados.txt"

if not archivo.exists():
    raise FileNotFoundError(
        f"No existe {archivo}. Ejecuta primero "
        "'python -m scripts.simular_liberaciones'."
    )

df = pd.read_csv(archivo)

requeridas = {
    "dia",
    "escenario",
    "hembras_silvestres",
    "machos_silvestres",
    "machos_esteriles",
    "liberacion_diaria",
}
faltantes = requeridas - set(df.columns)

if faltantes:
    raise ValueError(f"Faltan columnas: {sorted(faltantes)}")

dias_clave = [30, 90, 180]
resumen = []

for escenario, grupo in df.groupby("escenario"):
    grupo = grupo.sort_values("dia")
    fila = {
        "escenario": escenario,
        "liberacion_diaria": grupo["liberacion_diaria"].iloc[0],
    }

    for dia in dias_clave:
        cercano = grupo.iloc[
            (grupo["dia"] - dia).abs().argsort()[:1]
        ].iloc[0]
        fila[f"hembras_dia_{dia}"] = (
            cercano["hembras_silvestres"]
        )

    resumen.append(fila)

tabla = pd.DataFrame(resumen).sort_values(
    "liberacion_diaria"
)

lineas = [
    "INFORME DE RESULTADOS: MODELO GBG",
    "=" * 42,
    "",
    f"Filas analizadas: {len(df)}",
    f"Escenarios analizados: {df['escenario'].nunique()}",
    f"Días simulados: {df['dia'].min()} a {df['dia'].max()}",
    "",
    "HEMBRAS SILVESTRES POR ESCENARIO",
    "-" * 42,
    tabla.to_string(index=False, float_format=lambda x: f"{x:.6f}"),
    "",
    "INTERPRETACIÓN Y LIMITACIONES",
    "-" * 42,
    "Los resultados corresponden a simulaciones matemáticas.",
    "Los parámetros utilizados son valores de prueba, no estimaciones",
    "biológicas verificadas para México.",
    "Los casos notificados en animales no equivalen directamente",
    "al tamaño de la población silvestre de moscas.",
    "Por tanto, estos resultados no permiten calcular todavía",
    "una cantidad nacional óptima de moscas estériles ni una fecha",
    "fiable de erradicación.",
    "",
    "Antes de usar el modelo para decisiones operativas se requiere",
    "calibrar y validar sus parámetros con datos entomológicos,",
    "epidemiológicos y de liberaciones reales.",
]

carpeta.mkdir(parents=True, exist_ok=True)
salida.write_text("\n".join(lineas), encoding="utf-8")

print("\n".join(lineas))
print(f"\nInforme guardado en: {salida}")


