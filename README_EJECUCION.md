# Modelo GBG México - Erradicación Gusano Barrenador

## 📋 Descripción
Modelo matemático por etapas (7 compartimentos) para simular la erradicación del gusano barrenador del ganado (*Cochliomyia hominivorax*) en México mediante Técnica de Insecto Estéril (TIE).

**Estructura del modelo:**
- H = Huevos silvestres
- L = Larvas silvestres  
- P = Pupas silvestres
- Mw = Machos adultos silvestres
- Fw = Hembras adultas silvestres
- Ps = Pupas en planta (inventario)
- Ms = Machos estériles liberados en campo

**Datos:** Casos mensuales bovinos/porcinos SENASICA (nov 2024 – sep 2026)

---

## 🚀 Ejecución Rápida (Todo el Pipeline)

```bash
cd C:\Users\luish\OneDrive\Documents\resi\modelo-gbg-mexico
python scripts\run_pipeline.py
```

**Tiempo estimado:** 3–5 minutos  
**Genera:** 6 archivos de resultados en la raíz del proyecto

---

## 📦 Pasos Individuales (si quieres control)

### 1. Calibración de parámetros (Laplace)
```bash
cd C:\Users\luish\OneDrive\Documents\resi\modelo-gbg-mexico
$env:PYTHONPATH="."; python scripts\calibrar_parametros.py
```
**Salida:** `calibracion_parametros.csv`, `calibracion_diagnosticos.png`

### 2. Análisis de escenarios Monte Carlo
```bash
$env:PYTHONPATH="."; python scripts\analisis_escenarios_liberacion.py
```
**Salida:** `escenarios_liberacion_resultados.csv`, `escenarios_liberacion_trayectorias.csv`

### 3. Finalizar entrega (reinfestación + reporte + gráficos)
```bash
$env:PYTHONPATH="."; python scripts\finalizar_entrega.py
```
**Salida:** `grafico_escenarios.png`, `RESULTADOS.md`

---

## 📁 Archivos de Entrada (Ya incluidos)

| Archivo | Descripción |
|---------|-------------|
| `serie_mensual_analisis.csv` | Casos bovinos/porcinos SENASICA (20 meses completos) |
| `src/modelo/parametros.py` | Parámetros base (valores de referencia) |
| `src/modelo/modelo_etapas.py` | Sistema de EDOs (7 ecuaciones) |
| `src/simulacion/simulador.py` | Motor numérico (RK45 con validaciones) |

---

## 📊 Archivos de Salida (Generados)

| Archivo | Contenido |
|---------|-----------|
| `calibracion_parametros.csv` | b, mu_f, c calibrados + IC 95% asintóticos |
| `calibracion_diagnosticos.png` | Ajuste observado vs predicho, residuos, Q-Q |
| `escenarios_liberacion_resultados.csv` | Tabla: liberación vs prob. éxito vs años |
| `escenarios_liberacion_trayectorias.csv` | 200 trayectorias × 6 escenarios |
| `grafico_escenarios.png` | 4 paneles para presentación |
| `RESULTADOS.md` | Reporte ejecutivo completo (Markdown) |

---

## 🔧 Dependencias

```bash
pip install numpy pandas scipy matplotlib
```

(O usa el `requirements.txt` del proyecto)

---

## ⚙️ Configuración Clave (en scripts)

### Umbral de erradicación
```python
UMBRAL_CASOS_ANUAL = 200  # <200 casos/año nacional = erradicado
```

### Rangos literarios para Monte Carlo
```python
RANGOS_LITERARIOS = {
    "b": (0.15, 0.40),      # fecundidad efectiva
    "mu_f": (0.03, 0.10),   # mortalidad hembras
    "mu_m": (0.03, 0.10),   # mortalidad machos
    "c": (0.3, 0.8),        # competitividad
    # ... más parámetros
}
```

### Escenarios de liberación (pupas/día en planta Chiapas)
```python
ESCENARIOS = {
    "Sin liberacion": 0,
    "Minimo (1M pupas/dia)": 1_000_000,
    "Medio (3M pupas/dia)": 3_000_000,
    "Alto (5M pupas/dia)": 5_000_000,
    "Maximo (10M pupas/dia)": 10_000_000,
}
```

---

## 📈 Resultado Principal

> **Modelo 0-D calibrado (sin reinfestación):**  
> **1,000,000 pupas/día** (≈ **2.7 millones machos estériles/semana**) durante **7–8 meses** → **100% probabilidad erradicación**

> **Con reinfestación fronteriza (5 casos/mes):**  
> **0% probabilidad** con 1M pupas/día → Se requiere barrera fronteriza + mayor liberación

> **Campaña histórica real (México 1991–2006):**  
> 150–300 millones/semana por 15 años → **Modelo 0-D subestima 10–50x** por limitaciones documentadas

---

## ⚠️ Limitaciones Conocidas (Documentadas en RESULTADOS.md)

1. **Modelo 0-D** - Sin estructura espacial (estados, corredores, frontera)
2. **Sin estacionalidad** - Parámetros constantes todo el año
3. **Sin reinfestación externa** - Frontera sur es fuente real
4. **Competitiv. c constante** - En realidad disminuye con densidad
5. **Detección perfecta** - Subregistro no modelado
6. **Capacidad planta constante** - Límites logísticos/presupuestarios

---

## 🎯 Próximos Pasos Recomendados

1. **Modelo espacial** (estados + frontera sur + corredores ganaderos)
2. **Forzamiento estacional** (temperatura diaria → tasas desarrollo/mortalidad)
3. **Calibración bayesiana MCMC** (pymc + datos por estado)
4. **Optimización costo-efectividad** (dónde/cuándo liberar dado presupuesto)
5. **Integración datos Moscafrut** (capacidad real histórica y planificada)

---

## 📞 Contacto / Créditos

- **Datos:** SENASICA (casos bovinos/porcinos 2024–2026)
- **Planta:** Moscafrut Chiapas (producción pupas estériles)
- **Modelo:** Adaptado de literatura GBG (Vargas-Terán 2005, FAO/IAEA 2019)
- **Implementación:** Python + SciPy (RK45, least_squares, Monte Carlo)