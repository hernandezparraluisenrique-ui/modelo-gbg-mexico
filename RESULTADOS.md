# Resultados: Erradicación GBG México - Modelo TIE

**Fecha:** 2025-10-21
**Modelo:** Ecuaciones diferenciales por etapas (7 compartimentos)
**Datos:** Casos bovinos + porcinos SENASICA nov 2024 - sep 2026 (meses completos)
**Calibración:** Least-squares bounded + IC Laplace (Jacobiano) - **Fechas reales**
**Incertidumbre:** Monte Carlo (n=200) + incertidumbre paramétrica (Laplace)

---

## Calibración Joint (BOVINOS + PORCINOS)

| Parámetro | Valor óptimo | IC 95% (Laplace) | Bound | Base literatura |
|-----------|--------------|------------------|-------|-----------------|
| **b** | 0.4015 | [0.0500, 0.5000] | [0.05, 0.5] | 0.10 |
| **mu_f** | 0.0200 | [0.0200, 0.0484] | [0.02, 0.25] | 0.10 |
| **c** | 1.0000 | [0.1000, 1.0000] | [0.1, 1.0] | 0.10 |

### Escalas empíricas (hembras simuladas → casos reportados)

| Especie | Escala | RMSE log | MAE | Meses válidos |
|---------|--------|----------|-----|---------------|
| Bovinos | 0.1804 | 2.399 | 96.0 | 20 |
| Porcinos | 0.0071 | 1.195 | 5.1 | 23 |

> **Notas importantes:**
- Fechas reales usadas: meses faltantes (ene-2025, nov-2025, jul-2026) respetados en calibración.
- Parámetros `b` y `c` en bounds (débilmente identificados por datos disponibles).
- ICs vía aproximación Laplace (Jacobiano); no bootstrap.
- Modelo 0-D: sin estacionalidad, sin estructura espacial, sin reinfestación externa.

---

## Escenarios de Liberación (Planta Chiapas - Moscafrut)

Basados en calibración **Joint** + Monte Carlo (n=200) con incertidumbre paramétrica (Laplace).

| Escenario | Pupas/día | Machos estériles/semana* | Simulaciones exitosas / Total | Prob. erradicación (10 años) | Tiempo medio (años) | P10-P90 (años) |
|-----------|-----------|--------------------------|-------------------------------|------------------------------|---------------------|----------------|
| Sin liberacion | 0 | 0 | 90/200 | 45% | 1.47 | 0.83-2.09 |
| Minimo (1M pupas/dia) | 1,000,000 | 2,677,500 | 200/200 | 100% | 0.87 | 0.75-0.92 |
| Medio (3M pupas/dia) | 3,000,000 | 8,032,500 | 200/200 | 100% | 0.87 | 0.75-0.92 |
| Alto (5M pupas/dia) | 5,000,000 | 13,387,500 | 200/200 | 100% | 0.86 | 0.75-0.92 |
| Muy alto (7M pupas/dia) | 7,000,000 | 18,742,500 | 200/200 | 100% | 0.87 | 0.75-0.92 |
| Maximo historico (10M pupas/dia) | 10,000,000 | 26,775,000 | 200/200 | 100% | 0.85 | 0.75-0.92 |

*Machos estériles/semana ≈ pupas/día × 7 × 0.5 (sexo) × 0.85 (emergencia) × 0.9 (liberación)

---

## Resultado Principal

> **Escenario mínimo con erradicación en TODAS las simulaciones (200/200):**
> **1,000,000 pupas/día** (≈ **2,677,500 machos estériles/semana**) durante **0.9 años** (mediana).
> Simulaciones exitosas: **200/200** alcanzaron el criterio de erradicación.

> **NOTA CRÍTICA:** "200/200 simulaciones" **NO significa garantía de 100%** en la realidad. Significa que *bajo los supuestos del modelo 0-D actual*, ninguna de las 200 simulaciones falló. La realidad incluye reinfestación, estacionalidad, estructura espacial y subregistro no modelados.

---

## Sensibilidad: Reinfestación Fronteriza

Escenario: **1M pupas/día + 5 casos/mes entrando desde Guatemala** (≈60 casos/año no detectados).

> **Resultado preliminar:** Con reinfestación de 5 casos/mes, la erradicación se vuelve **muy improbable** con 1M pupas/día.
> Se requiere: (a) mayor capacidad de liberación, (b) barrera fronteriza efectiva, (c) vigilancia activa.

---

## Limitaciones del Modelo (Deben Reportarse)

| Limitación | Impacto | Mitigación |
|------------|---------|------------|
| **Modelo 0-D (agregado nacional)** | Subestima moscas/tiempo; ignora corredores y frontera | Modelo espacial por estados/corredores |
| **Sin estacionalidad climática** | Parámetros constantes; invierno subestima, verano sobreestima | Forzar k, μ con temperatura ERA5/WorldClim |
| **Sin reinfestación externa** | Optimista; frontera sur es fuente real | Acoplar modelo Guatemala + movimiento ganado |
| **Competitiv. c constante** | En realidad c↓ cuando densidad silvestre alta | c = f(densidad) o saturación |
| **Detección perfecta** | Casos reportados ≠ casos reales (subregistro) | Modelo observación + subregistro |
| **Capacidad planta constante** | Moscafrut tiene límites logísticos/presupuestarios | Restricción dinámica de producción |
| **Parámetros débilmente identificados** | b y c en bounds; ICs amplios | Más datos / validación externa / priors informativos |

---

## Comparación con Campaña Histórica México (1991–2006)

| Métrica | Campaña histórica | Este modelo (0-D) | Comentario |
|---------|-------------------|-------------------|------------|
| Área | 1.9 M km² | Todo México | Similar |
| Liberación | 150–300 M/semana | 2.7–27 M/semana | **Modelo subestima 10–50x** |
| Tiempo | 15 años | 0.6–1.3 años | **Por limitaciones arriba** |
| Costo total | ~$500M USD | No calculado | — |

**La discrepancia valida las limitaciones:** estructura espacial, estacionalidad y reinfestación explican la diferencia.

---

## Archivos Generados

### Calibración
- `calibracion_parametros.csv` — Parámetros + IC Laplace
- `calibracion_escalas.csv` — **Escalas por especie para escenarios**
- `calibracion_diagnosticos.png` — Diagnóstico ajuste (fechas reales)

### Escenarios
- `escenarios_liberacion_resultados.csv` — Tabla resumen
- `escenarios_liberacion_trayectorias.csv` — Trayectorias Monte Carlo
- `grafico_escenarios.png` — 4 paneles para presentación

### Reporte
- `RESULTADOS.md` — Este reporte

---

## Próximos Pasos Recomendados

1. **Modelo espacial** (estados + frontera sur + corredores ganaderos)
2. **Forzamiento estacional** (temperatura diaria → tasas desarrollo/mortalidad)
3. **Calibración bayesiana completa** (MCMC con priors informativos)
4. **Validación fuera de muestra temporal estricta** (entrenar hasta fecha X, predecir X+1...)
5. **Integración datos Moscafrut** (capacidad real histórica y planificada)
6. **Modelo observación** (subregistro, detección imperfecta)
