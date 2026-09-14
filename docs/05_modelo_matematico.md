# 5. Modelo matemático

## 5.1 Definición y propósito del modelo

El modelo matemático tiene como propósito representar la dinámica poblacional del gusano barrenador del ganado (GBG), *Cochliomyia hominivorax*, y analizar el efecto que tiene la liberación de machos estériles sobre la reproducción y evolución de la población silvestre.

El modelo se desarrollará como una representación matemática de la interacción entre la población silvestre del GBG y los machos estériles utilizados mediante la Técnica del Insecto Estéril (TIE).

La finalidad principal será determinar cómo cambia la población del GBG a lo largo del tiempo bajo diferentes estrategias de liberación y, posteriormente, estimar:

* la cantidad de moscas estériles necesaria;
* la frecuencia de liberación;
* la duración de la estrategia;
* la relación entre machos estériles y machos silvestres;
* la cantidad total de moscas utilizadas;
* el aprovechamiento de la capacidad de producción de la planta de Metapa;
* el tiempo necesario para alcanzar un criterio de control o erradicación.

### 5.1.1 Población objetivo

La población objetivo del modelo corresponde al GBG silvestre presente en el sistema de estudio.

La población de insectos será representada mediante variables que describen principalmente sus componentes adultos:

$$
M_w(t)
$$

$$
F_v(t)
$$

$$
F_m(t)
$$

donde:

* \(M_w(t)\) representa los machos silvestres fértiles;
* \(F_v(t)\) representa las hembras silvestres vírgenes;
* \(F_m(t)\) representa las hembras silvestres apareadas.

A esta población se incorporará la población de machos estériles:

$$
M_s(t)
$$

que representa los individuos provenientes de las estrategias de liberación.

### 5.1.2 Principio de funcionamiento

El modelo se fundamentará en el principio de que la liberación de machos estériles modifica la probabilidad de apareamiento de las hembras silvestres.

De manera conceptual, una hembra silvestre puede aparearse con:

$$
\text{Macho silvestre fértil}
$$

o con:

$$
\text{Macho estéril}
$$

Los apareamientos con machos silvestres pueden producir descendencia viable, mientras que los apareamientos con machos estériles tienen como finalidad reducir la producción de descendencia viable.

Por lo tanto, el efecto principal de la TIE será representado mediante una reducción de la reproducción efectiva de la población silvestre.

### 5.1.3 Dinámica temporal

Las variables del modelo serán representadas como funciones del tiempo:

$$
X=X(t)
$$

El tiempo podrá expresarse inicialmente en días o semanas, dependiendo de la resolución temporal seleccionada para la simulación.

La unidad temporal definitiva deberá ser compatible con:

* los tiempos biológicos del GBG;
* la información disponible sobre supervivencia y reproducción;
* la frecuencia de liberación;
* los datos de producción de la planta de Metapa.

La elección de la unidad temporal se establecerá antes de implementar el sistema definitivo de ecuaciones.

### 5.1.4 Estructura general

La dinámica conceptual del modelo será:

$$
\text{Población silvestre}
\rightarrow
\text{apareamiento}
\rightarrow
\text{reproducción}
\rightarrow
\text{nueva generación}
\rightarrow
\text{población silvestre}
$$

La TIE introduce una modificación en el proceso:

$$
\text{Machos estériles}
\rightarrow
\text{competencia por apareamiento}
\rightarrow
\text{menor reproducción viable}
\rightarrow
\text{disminución de la población}
$$

La producción de la planta de Metapa funcionará como una restricción externa:

$$
\text{Producción}
\rightarrow
\text{Disponibilidad}
\rightarrow
\text{Liberación}
\rightarrow
\text{Machos estériles}
$$

Por lo tanto, el modelo integrará tres componentes principales:

1. **Dinámica poblacional del GBG.**
2. **Efecto reproductivo de la TIE.**
3. **Restricción de producción y liberación de moscas estériles.**

### 5.1.5 Objetivo matemático

El modelo deberá permitir evaluar la evolución de la población silvestre:

$$
N_w(t)
$$

bajo diferentes estrategias de liberación:

$$
S_R=\{R_t,\Delta t_R,T_R\}
$$

donde:

* \(R_t\) = cantidad de moscas estériles liberadas;
* \(\Delta t_R\) = intervalo entre liberaciones;
* \(T_R\) = duración de la estrategia.

Para cada estrategia se analizará el comportamiento de la población y se determinará si se alcanza el criterio establecido de control o erradicación.

### 5.1.6 Restricción de producción

La cantidad de moscas que puede utilizar una estrategia estará limitada por la producción disponible de la planta de Metapa.

La relación será:

$$
R_t\leq A_t\leq C_t
$$

donde:

* \(R_t\) = cantidad liberada;
* \(A_t\) = cantidad disponible para la estrategia;
* \(C_t\) = producción disponible durante el periodo.

De esta manera, el modelo no podrá generar una estrategia de liberación que utilice más moscas de las disponibles en la planta bajo el escenario seleccionado.

### 5.1.7 Resultados esperados

A partir de la simulación se espera obtener, como mínimo:

$$
N_w(t)
$$

$$
M_s(t)
$$

$$
\rho(t)
$$

$$
R_{total}
$$

$$
T_C
$$

$$
T_E
$$

$$
U_C
$$

Estos resultados permitirán comparar diferentes estrategias de liberación y determinar cuáles presentan mejores resultados bajo las condiciones establecidas.

### 5.1.8 Alcance del modelo matemático

El modelo se enfocará inicialmente en representar la dinámica poblacional necesaria para evaluar la TIE.

No se pretende construir en esta etapa una representación detallada de todos los procesos industriales de la planta ni una simulación completa del ciclo productivo de las moscas dentro de las instalaciones.

La planta de Metapa será representada principalmente mediante su capacidad y disponibilidad de producción, las cuales funcionarán como restricciones para las estrategias de liberación.

De igual manera, la información sobre bovinos y porcinos será incorporada únicamente en la medida en que permita representar o validar la relación entre la población del GBG y sus hospedadores.

### 5.1.9 Principio de construcción

La formulación del modelo seguirá el principio:

$$
\text{Datos}
\rightarrow
\text{Parámetros}
\rightarrow
\text{Variables}
\rightarrow
\text{Ecuaciones}
\rightarrow
\text{Simulación}
\rightarrow
\text{Resultados}
$$

Cada ecuación deberá estar relacionada con una característica biológica o con una restricción operacional documentada.

Cuando no exista información suficiente para establecer una relación matemática, se utilizarán rangos, escenarios o supuestos explícitamente documentados en lugar de introducir valores arbitrarios.

### 5.1.10 Consideración sobre la incertidumbre

Los resultados del modelo dependerán de la calidad y disponibilidad de los parámetros utilizados.

Por esta razón, el modelo deberá permitir posteriormente evaluar diferentes valores o rangos para los parámetros que presenten incertidumbre.

Esto permitirá determinar si las conclusiones obtenidas son robustas ante cambios en variables como:

* población inicial;
* fecundidad;
* mortalidad;
* supervivencia;
* competitividad de machos estériles;
* supervivencia de machos estériles;
* frecuencia de liberación.

La incertidumbre será analizada mediante escenarios y, cuando sea posible, mediante análisis de sensibilidad.

### 5.1.11 Criterio general de diseño

El modelo deberá ser suficientemente detallado para representar el mecanismo de acción de la TIE, pero no deberá incorporar variables, relaciones o procesos que no puedan justificarse mediante información científica o datos disponibles.

Por lo tanto, se priorizará:

* trazabilidad de los parámetros;
* claridad de las variables;
* consistencia dimensional;
* justificación biológica de las ecuaciones;
* compatibilidad con los datos de producción de Metapa;
* capacidad de reproducir diferentes escenarios;
* posibilidad de implementación computacional en Python.

La estructura matemática definitiva se construirá progresivamente a partir de estos principios.

## 5.2 Supuestos del modelo

Para formular el modelo matemático de la dinámica poblacional del gusano barrenador del ganado (GBG) y evaluar el efecto de la Técnica del Insecto Estéril (TIE), se establecen una serie de supuestos que delimitan las condiciones bajo las cuales funcionará la simulación.

Los supuestos permiten simplificar el sistema biológico sin perder los procesos fundamentales que determinan la dinámica de la población y la efectividad de la liberación de machos estériles.

### 5.2.1 Supuesto sobre la población objetivo

La población objetivo corresponde exclusivamente al GBG silvestre, *Cochliomyia hominivorax*.

El modelo no considerará otras especies de moscas ni otros organismos como parte de la población objetivo.

La población silvestre estará representada inicialmente mediante:

$$
M_w(t),\quad F_v(t),\quad F_m(t)
$$

donde se distinguen los machos silvestres fértiles, las hembras vírgenes y las hembras apareadas.

### 5.2.2 Supuesto sobre la población de machos estériles

Los machos estériles utilizados en la estrategia de control serán considerados como individuos producidos mediante el proceso de TIE y destinados a competir con los machos silvestres por el apareamiento con hembras silvestres.

La población de machos estériles se representará mediante:

$$
M_s(t)
$$

La cantidad de machos estériles presentes en el ambiente dependerá de las liberaciones realizadas y de su supervivencia posterior.

Por lo tanto:

$$
M_s(t)\neq R_t
$$

en general, debido a que \(R_t\) representa los individuos liberados durante un periodo, mientras que \(M_s(t)\) representa los individuos que permanecen disponibles después de considerar las pérdidas.

### 5.2.3 Supuesto sobre el apareamiento

Se supone que las hembras silvestres pueden aparearse con machos silvestres fértiles o con machos estériles.

La probabilidad relativa de que una hembra se aparee con un macho estéril dependerá de:

* la cantidad de machos estériles disponibles;
* la cantidad de machos silvestres fértiles;
* la competitividad relativa de los machos estériles.

De manera conceptual:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

donde \(c\) representa la competitividad relativa del macho estéril respecto al macho silvestre.

Esta expresión será revisada durante la formulación definitiva del modelo.

### 5.2.4 Supuesto sobre la reproducción

Se supone que los apareamientos entre hembras silvestres y machos silvestres fértiles pueden producir descendencia viable.

En cambio, los apareamientos entre hembras silvestres y machos estériles tienen como objetivo reducir o impedir la producción de descendencia viable.

Por lo tanto, el efecto de la TIE se incorporará principalmente mediante una reducción de la reproducción efectiva de la población silvestre.

### 5.2.5 Supuesto sobre la esterilidad

Los machos sometidos al proceso de irradiación serán considerados estériles para efectos reproductivos del modelo.

Esto significa que su función principal dentro de la simulación será competir por el apareamiento, pero no generar descendencia viable cuando se apareen con hembras silvestres.

La eficacia real de la esterilización deberá estar respaldada por información experimental o técnica.

Por esta razón, la eficacia de esterilización no se establecerá arbitrariamente como un valor definitivo mientras no se disponga de una fuente adecuada.

### 5.2.6 Supuesto sobre la supervivencia

Los individuos silvestres y estériles estarán sujetos a pérdidas durante el tiempo.

Para los machos silvestres se podrá utilizar una tasa de mortalidad:

$$
\mu_M
$$

y para las hembras una tasa de mortalidad:

$$
\mu_F
$$

Para los machos estériles se podrá utilizar:

$$
\mu_s
$$

Estas tasas deberán determinarse mediante información científica disponible.

En ausencia de un valor único suficientemente respaldado, se podrán utilizar rangos o escenarios.

### 5.2.7 Supuesto sobre la población de hospedadores

El modelo considerará únicamente bovinos y porcinos como hospedadores.

Se utilizarán las variables:

$$
B(t)
$$

para representar la población bovina y:

$$
P(t)
$$

para representar la población porcina.

Las infestaciones se representarán mediante:

$$
I_b(t)
$$

e

$$
I_p(t)
$$

respectivamente.

Sin embargo, se reconoce que la infestación por GBG no debe modelarse como una enfermedad contagiosa convencional entre animales.

La presencia de hospedadores infestados se utilizará para representar o validar la interacción entre la población del GBG y los hospedadores cuando existan datos suficientes.

### 5.2.8 Supuesto sobre la relación entre hospedadores y población de GBG

No se establecerá una conversión directa y arbitraria entre el número de animales infestados y el número de moscas presentes.

Por ejemplo, no se asumirá que:

$$
1\text{ animal infestado}=X\text{ moscas}
$$

sin evidencia científica que permita justificar dicha relación.

La relación entre hospedadores y población del GBG deberá establecerse mediante información epidemiológica, biológica u observacional disponible.

Cuando los datos no sean suficientes para incorporar esta relación directamente en las ecuaciones principales, las variables epidemiológicas podrán utilizarse como variables de observación o validación.

### 5.2.9 Supuesto sobre la planta de producción

La única fuente de moscas estériles considerada para el modelo será la planta de producción ubicada en Metapa de Domínguez, Chiapas, México.

No se utilizarán otras plantas de producción como fuente de capacidad para las estrategias simuladas.

La producción de la planta será representada mediante:

$$
C_t
$$

y funcionará como una restricción de las cantidades que pueden ser destinadas a las estrategias de liberación.

### 5.2.10 Supuesto sobre la capacidad de producción

La capacidad productiva disponible podrá variar con el tiempo.

Para representar diferentes condiciones operativas se podrán utilizar escenarios basados en:

* producción inicial reportada;
* incremento progresivo de producción;
* capacidad proyectada de 100 millones de moscas por semana;
* escenario futuro de hasta 120 millones de moscas por semana.

Estos valores se tratarán como condiciones de escenario y no como una producción constante garantizada durante todo el periodo de simulación.

### 5.2.11 Supuesto sobre disponibilidad y liberación

La cantidad producida no necesariamente será igual a la cantidad liberada.

Por ello se mantendrá la separación:

$$
C_t\rightarrow A_t\rightarrow R_t
$$

donde:

* \(C_t\) = producción disponible;
* \(A_t\) = cantidad disponible para la estrategia;
* \(R_t\) = cantidad efectivamente liberada.

La restricción será:

$$
R_t\leq A_t\leq C_t
$$

Esto permitirá representar pérdidas, disponibilidad limitada u otras restricciones operativas cuando existan datos suficientes para incorporarlas.

### 5.2.12 Supuesto sobre la frecuencia de liberación

Las liberaciones podrán realizarse con diferentes frecuencias.

La estrategia de liberación se representará mediante:

$$
S_R=\{R_t,\Delta t_R,T_R\}
$$

donde:

* \(R_t\) representa la cantidad liberada;
* \(\Delta t_R\) representa el intervalo entre liberaciones;
* \(T_R\) representa la duración de la estrategia.

La simulación permitirá comparar diferentes combinaciones de estos elementos.

### 5.2.13 Supuesto sobre la relación estéril:silvestre

La relación entre machos estériles y machos silvestres se representará mediante:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

Esta relación será utilizada para evaluar la presión relativa ejercida por los machos estériles sobre la población silvestre.

La referencia operativa de una relación de 10:1 podrá utilizarse como uno de los escenarios de análisis, especialmente en condiciones de baja densidad.

Sin embargo, este valor no será considerado una constante biológica universal ni se aplicará automáticamente a todas las condiciones.

### 5.2.14 Supuesto sobre la dinámica espacial

En la primera formulación se considerará una representación agregada de la población dentro del área de estudio.

No se incorporará inicialmente una simulación espacial detallada de movimientos entre municipios, regiones o zonas geográficas.

La inclusión de dispersión espacial dependerá de la disponibilidad de datos suficientes y de la necesidad de incorporarla para responder a los objetivos del proyecto.

### 5.2.15 Supuesto sobre factores ambientales

La temperatura, humedad y otros factores ambientales pueden modificar la supervivencia, desarrollo y reproducción del GBG.

Sin embargo, dichos factores no serán incorporados inicialmente como variables dinámicas independientes si no se dispone de información suficiente para parametrizar su efecto.

Cuando sea necesario, podrán representarse posteriormente mediante escenarios o parámetros dependientes de condiciones ambientales.

### 5.2.16 Supuesto sobre el tiempo

El modelo representará la evolución de la población mediante pasos temporales definidos.

La unidad de tiempo definitiva deberá permitir representar adecuadamente:

* reproducción;
* supervivencia;
* mortalidad;
* liberaciones;
* producción de moscas estériles.

La resolución temporal será seleccionada antes de la implementación definitiva de las ecuaciones.

### 5.2.17 Supuesto sobre la población inicial

La población inicial del GBG:

$$
N_w(0)
$$

no será determinada mediante una estimación arbitraria.

La condición inicial deberá basarse, cuando sea posible, en datos científicos, epidemiológicos, observacionales o en escenarios claramente definidos.

En caso de no existir una estimación suficientemente confiable, se utilizarán diferentes escenarios de población inicial para evaluar el comportamiento del modelo.

### 5.2.18 Supuesto sobre el criterio de control y erradicación

El modelo distinguirá entre control y erradicación.

El control se definirá mediante un umbral:

$$
N_w(t)\leq N_C
$$

mientras que la erradicación se representará mediante un criterio:

$$
N_w(t)\leq N_E
$$

Los valores de \(N_C\) y \(N_E\) deberán ser establecidos posteriormente con base en criterios científicos, epidemiológicos u operativos.

Por lo tanto, no se asumirá inicialmente que la erradicación significa necesariamente que el número calculado de individuos sea exactamente cero.

### 5.2.19 Supuesto sobre los resultados del modelo

Los resultados obtenidos serán interpretados como resultados de simulación condicionados a los parámetros, supuestos y escenarios seleccionados.

Por lo tanto:

$$
\text{Resultado del modelo}
\neq
\text{predicción absoluta del comportamiento real}
$$

Los resultados deberán interpretarse considerando la incertidumbre de los parámetros y las limitaciones de los datos disponibles.

### 5.2.20 Principio general de los supuestos

Los supuestos deberán cumplir las siguientes condiciones:

1. Ser explícitos.
2. Tener una justificación biológica, matemática u operativa.
3. No contradecir información científica disponible.
4. Poder modificarse cuando se obtengan nuevos datos.
5. Diferenciar claramente entre hechos confirmados y escenarios hipotéticos.
6. Evitar la incorporación de valores arbitrarios.

Estos supuestos constituyen la base para desarrollar el sistema de ecuaciones del modelo.

## 5.3 Diagrama conceptual del modelo

El diagrama conceptual representa las principales relaciones que serán consideradas posteriormente en la formulación matemática.

Su función es mostrar de manera simplificada cómo interactúan la población silvestre del gusano barrenador del ganado, la población de machos estériles y la capacidad de producción de la planta de Metapa.

### 5.3.1 Estructura general

La estructura conceptual del modelo se representa de la siguiente manera:

```text
                         ┌───────────────────────┐
                         │   Planta de Metapa    │
                         │       Chiapas         │
                         └───────────┬───────────┘
                                     │
                                     │ Producción C(t)
                                     ▼
                         ┌───────────────────────┐
                         │    Disponibilidad     │
                         │        A(t)           │
                         └───────────┬───────────┘
                                     │
                                     │ Liberación R(t)
                                     ▼
                         ┌───────────────────────┐
                         │   Machos estériles    │
                         │        Ms(t)           │
                         └───────────┬───────────┘
                                     │
                                     │ Competencia
                                     │ reproductiva
                                     ▼
┌───────────────────┐       ┌───────────────────────┐
│ Machos silvestres │──────►│     Apareamiento      │
│      Mw(t)        │       │                       │
└───────────────────┘       └───────────┬───────────┘
                                        │
                                        │
                         ┌──────────────┴──────────────┐
                         │                             │
                         ▼                             ▼
                Apareamiento con             Apareamiento con
                macho silvestre              macho estéril
                         │                             │
                         ▼                             ▼
                  Descendencia                  Reducción de
                     viable                    descendencia
                         │                             │
                         └──────────────┬──────────────┘
                                        │
                                        ▼
                              Nueva población silvestre
                                        │
                                        ▼
                               Dinámica poblacional
                                        │
                                        └───────────────►
                                         siguiente periodo
```

### 5.3.2 Población silvestre

La población silvestre constituye el componente central del modelo.

Inicialmente se representará mediante:

$$
M_w(t)
$$

$$
F_v(t)
$$

$$
F_m(t)
$$

donde:

* \(M_w(t)\) = machos silvestres fértiles;
* \(F_v(t)\) = hembras silvestres vírgenes;
* \(F_m(t)\) = hembras silvestres apareadas.

La población adulta silvestre total podrá calcularse como:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

La dinámica de esta población dependerá principalmente de:

* reproducción;
* apareamiento;
* mortalidad;
* incorporación de nuevos individuos.

### 5.3.3 Machos estériles

Los machos estériles serán incorporados al sistema mediante las liberaciones provenientes de la estrategia de control.

La cadena de entrada será:

$$
C_t\rightarrow A_t\rightarrow R_t\rightarrow M_s(t)
$$

donde:

* \(C_t\) = producción disponible de la planta;
* \(A_t\) = cantidad disponible para la estrategia;
* \(R_t\) = cantidad liberada;
* \(M_s(t)\) = machos estériles presentes en el sistema.

Los machos estériles competirán con los machos silvestres por el apareamiento.

### 5.3.4 Competencia reproductiva

La interacción fundamental de la TIE se producirá durante el apareamiento.

Una hembra silvestre podrá tener contacto reproductivo con:

$$
M_w(t)
$$

o con:

$$
M_s(t)
$$

La proporción de apareamientos asociados con machos estériles podrá representarse inicialmente mediante:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

donde \(c\) representa la competitividad relativa de los machos estériles.

La proporción complementaria de apareamientos con machos silvestres será:

$$
p_w(t)=1-p_s(t)
$$

Estas expresiones serán revisadas y, si es necesario, modificadas durante la formulación matemática.

### 5.3.5 Reproducción

Los apareamientos con machos silvestres fértiles contribuirán a la producción de descendencia viable.

Conceptualmente:

$$
F_m(t)
\rightarrow
\text{reproducción}
\rightarrow
\text{nuevos individuos}
$$

Mientras que los apareamientos con machos estériles tendrán como objetivo reducir la descendencia viable:

$$
F_v(t)+M_s(t)
\rightarrow
\text{apareamiento estéril}
\rightarrow
\text{reducción de descendencia viable}
$$

Por lo tanto, el efecto acumulado de la TIE será una disminución de la incorporación de nuevos individuos a la población silvestre.

### 5.3.6 Mortalidad y permanencia

Los individuos de la población silvestre estarán sujetos a mortalidad.

De manera conceptual:

$$
M_w(t)\rightarrow \mu_M
$$

$$
F_v(t)\rightarrow \mu_F
$$

$$
F_m(t)\rightarrow \mu_F
$$

Los machos estériles también estarán sujetos a pérdidas:

$$
M_s(t)\rightarrow \mu_s
$$

Esto significa que la población estéril presente en un periodo no será necesariamente igual a la cantidad liberada durante ese mismo periodo.

### 5.3.7 Retroalimentación poblacional

La población resultante de un periodo se convertirá en la población inicial del periodo siguiente.

Conceptualmente:

$$
N_w(t)
\rightarrow
\text{reproducción}
\rightarrow
N_w(t+\Delta t)
$$

En ausencia de liberaciones suficientes de machos estériles, la población silvestre podrá mantenerse o aumentar dependiendo de sus parámetros biológicos.

Cuando la presión de los machos estériles sea suficiente, la reproducción viable deberá disminuir y la población silvestre podrá reducirse progresivamente.

### 5.3.8 Incorporación de hospedadores

Los bovinos y porcinos serán considerados como hospedadores del GBG y podrán aportar información epidemiológica al modelo.

La relación conceptual será:

```text
             Población de GBG
                    │
                    │
                    ▼
             Hembras adultas
                    │
                    │ Ovoposición
                    ▼
             Heridas de hospedadores
                    │
             ┌──────┴──────┐
             ▼             ▼
          Bovinos        Porcinos
             │             │
             ▼             ▼
       I_b(t)          I_p(t)
```

Las variables:

$$
I_b(t)
$$

e

$$
I_p(t)
$$

podrán utilizarse para representar o validar la presencia de infestaciones en bovinos y porcinos.

Estas variables no serán consideradas automáticamente como equivalentes a una cantidad determinada de moscas.

### 5.3.9 Restricción de producción

La planta de Metapa constituye una restricción externa al modelo poblacional.

Por lo tanto:

$$
R_t\leq A_t\leq C_t
$$

La estrategia de control deberá permanecer dentro de la capacidad disponible durante cada periodo.

Esto permitirá comparar una estrategia biológicamente efectiva con una estrategia que además sea factible desde el punto de vista de producción.

### 5.3.10 Relación entre los componentes

La interacción completa puede resumirse mediante:

$$
\boxed{
\text{Producción}
\rightarrow
\text{Liberación}
\rightarrow
\text{Competencia}
\rightarrow
\text{Menor reproducción}
\rightarrow
\text{Reducción poblacional}
}
$$

Mientras que la dinámica natural puede representarse como:

$$
\boxed{
\text{Población}
\rightarrow
\text{Apareamiento}
\rightarrow
\text{Reproducción}
\rightarrow
\text{Nueva población}
}
$$

Ambos procesos se integran en el modelo matemático.

### 5.3.11 Flujo general del modelo

El flujo completo del sistema será:

```text
┌─────────────────────┐
│ Datos y parámetros  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Población inicial   │
│ Mw, Fv, Fm          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Producción Metapa   │
│ C(t)                │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Estrategia de       │
│ liberación R(t)     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Machos estériles    │
│ Ms(t)               │
└──────────┬──────────┘
           │
           ▼
┌────────────────────────────┐
│ Competencia por            │
│ apareamiento               │
│ Mw(t) vs Ms(t)             │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Reproducción efectiva      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Nueva población silvestre  │
└────────────┬───────────────┘
             │
             ▼
       siguiente periodo
             │
             └──────────────►

                 RESULTADOS
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Nw(t)         TE          Rtotal
        │
        ▼
   criterio de
   control/erradicación
```

### 5.3.12 Función del diagrama conceptual

El diagrama establece la arquitectura lógica que posteriormente será transformada en un sistema de ecuaciones diferenciales o de ecuaciones de dinámica poblacional.

La formulación matemática deberá conservar las relaciones principales identificadas en este diagrama:

1. La población silvestre presenta dinámica propia.
2. Las hembras silvestres participan en el proceso reproductivo.
3. Los machos silvestres y estériles compiten por el apareamiento.
4. Los apareamientos estériles reducen la reproducción viable.
5. Los individuos presentan supervivencia y mortalidad.
6. La planta de Metapa limita la cantidad disponible para liberación.
7. Las estrategias de liberación pueden modificarse entre escenarios.
8. La población resultante se utiliza como condición para el siguiente periodo.
9. Los resultados permiten calcular el tiempo necesario para alcanzar los criterios establecidos.

Este diagrama constituye la base conceptual para la construcción de las ecuaciones matemáticas del modelo.

## 5.4 Formulación de las ecuaciones del modelo

La formulación matemática tiene como finalidad representar mediante ecuaciones la evolución temporal de la población adulta del gusano barrenador del ganado y el efecto de la liberación de machos estériles.

El sistema se construirá a partir de las variables de estado definidas en el capítulo 4:

$$
M_w(t),\quad F_v(t),\quad F_m(t),\quad M_s(t)
$$

donde:

* \(M_w(t)\) = machos silvestres fértiles;
* \(F_v(t)\) = hembras silvestres vírgenes;
* \(F_m(t)\) = hembras silvestres apareadas;
* \(M_s(t)\) = machos estériles presentes.

La formulación se realizará mediante ecuaciones diferenciales que representen los principales procesos de la dinámica poblacional.

### 5.4.1 Vector de estado

El sistema se representa mediante el vector:

$$
X(t)=
\begin{bmatrix}
M_w(t)\\
F_v(t)\\
F_m(t)\\
M_s(t)
\end{bmatrix}
$$

y de manera general puede expresarse como:

$$
\frac{dX(t)}{dt}=F(X(t),\theta,u(t))
$$

donde:

* \(X(t)\) = vector de variables de estado;
* \(\theta\) = conjunto de parámetros biológicos y de la TIE;
* \(u(t)\) = entradas o variables de control, principalmente las liberaciones de moscas estériles;
* \(F\) = función que describe la dinámica del sistema.

La forma específica de \(F\) se construirá a partir de los procesos descritos en las siguientes subsecciones.

---

### 5.4.2 Dinámica de los machos silvestres

Los machos silvestres se incorporan a la población como consecuencia de la reproducción y se eliminan mediante mortalidad.

La ecuación general puede expresarse como:

$$
\frac{dM_w}{dt}
=
B_M(t)-\mu_M M_w(t)
$$

donde:

* \(B_M(t)\) = incorporación de nuevos machos silvestres;
* \(\mu_M\) = tasa de mortalidad de los machos silvestres.

Si \(r_M\) representa la proporción de individuos nuevos que corresponden a machos, entonces:

$$
B_M(t)=r_M B_v(t)
$$

por lo que:

$$
\boxed{
\frac{dM_w}{dt}
=
r_M B_v(t)-\mu_M M_w(t)
}
$$

donde \(B_v(t)\) representa la cantidad de descendencia viable producida durante el periodo.

El valor de \(r_M\) deberá establecerse a partir de información biológica adecuada y no se fijará arbitrariamente.

---

### 5.4.3 Dinámica de las hembras vírgenes

Las hembras vírgenes se incorporan mediante el nacimiento de nuevas hembras y salen de este estado cuando se aparean o mueren.

La ecuación general será:

$$
\frac{dF_v}{dt}
=
B_F(t)-A_w(t)-A_s(t)-\mu_FF_v(t)
$$

donde:

* \(B_F(t)\) = nuevas hembras producidas;
* \(A_w(t)\) = apareamientos efectivos con machos silvestres;
* \(A_s(t)\) = apareamientos efectivos con machos estériles;
* \(\mu_F\) = tasa de mortalidad de las hembras.

Si \(r_F\) representa la proporción de hembras entre los nuevos individuos:

$$
B_F(t)=r_F B_v(t)
$$

por lo que:

$$
\boxed{
\frac{dF_v}{dt}
=
r_FB_v(t)-A_w(t)-A_s(t)-\mu_FF_v(t)
}
$$

Esta ecuación representa uno de los principales puntos de interacción entre la población silvestre y los machos estériles.

---

### 5.4.4 Dinámica de las hembras apareadas

Las hembras que se aparean pasan del estado de hembras vírgenes al estado de hembras apareadas.

Por lo tanto:

$$
\boxed{
\frac{dF_m}{dt}
=
A_w(t)+A_s(t)-\mu_FF_m(t)
}
$$

La distinción entre \(A_w(t)\) y \(A_s(t)\) permitirá determinar si el apareamiento fue realizado con un macho fértil o con un macho estéril.

Esta separación es necesaria porque ambos tipos de apareamiento tienen consecuencias reproductivas diferentes dentro del modelo.

---

### 5.4.5 Competencia entre machos silvestres y estériles

La competencia reproductiva constituye el mecanismo principal mediante el cual la TIE modifica la dinámica poblacional.

Se utilizará inicialmente una función de competencia basada en la abundancia relativa y la competitividad de los machos:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

donde:

* \(p_s(t)\) = proporción de apareamientos asociados con machos estériles;
* \(M_s(t)\) = machos estériles disponibles;
* \(M_w(t)\) = machos silvestres fértiles;
* \(c\) = competitividad relativa de los machos estériles.

La proporción correspondiente a machos silvestres será:

$$
\boxed{
p_w(t)=1-p_s(t)
}
$$

Por lo tanto:

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

Estas expresiones representan inicialmente una hipótesis funcional del modelo y deberán ser evaluadas posteriormente mediante información científica y análisis de sensibilidad.

---

### 5.4.6 Apareamientos efectivos

Si \(a\) representa la tasa de apareamiento potencial de las hembras vírgenes, el número de apareamientos efectivos podrá expresarse inicialmente como:

$$
A_w(t)=aF_v(t)p_w(t)
$$

y:

$$
A_s(t)=aF_v(t)p_s(t)
$$

Por lo tanto:

$$
A_w(t)+A_s(t)=aF_v(t)
$$

Esta relación supone que una fracción de las hembras vírgenes disponibles puede participar en el proceso de apareamiento durante el periodo considerado.

El parámetro \(a\) deberá ser determinado posteriormente a partir de información biológica disponible.

---

### 5.4.7 Producción de descendencia viable

La cantidad de descendencia viable dependerá de los apareamientos realizados con machos silvestres fértiles.

De manera simplificada:

$$
\boxed{
B_v(t)=bA_w(t)
}
$$

donde:

* \(B_v(t)\) = descendencia viable producida;
* \(b\) = producción promedio de descendientes viables por apareamiento efectivo con un macho fértil.

Esta representación es una simplificación inicial.

El parámetro \(b\) no deberá confundirse automáticamente con el número máximo de huevos que puede producir una hembra, ya que deberán considerarse posteriormente factores como fecundidad efectiva, viabilidad y supervivencia.

---

### 5.4.8 Incorporación de la TIE en la reproducción

La TIE reduce la reproducción efectiva al aumentar la proporción de apareamientos con machos estériles.

El mecanismo conceptual será:

$$
M_s(t)\uparrow
$$

$$
\Downarrow
$$

$$
p_s(t)\uparrow
$$

$$
\Downarrow
$$

$$
A_w(t)\downarrow
$$

$$
\Downarrow
$$

$$
B_v(t)\downarrow
$$

$$
\Downarrow
$$

$$
N_w(t)\downarrow
$$

Esta cadena representa el mecanismo fundamental que deberá reproducir la simulación.

---

### 5.4.9 Dinámica de los machos estériles

Los machos estériles ingresan al sistema mediante las liberaciones:

$$
R_t
$$

y posteriormente disminuyen debido a mortalidad o pérdida de disponibilidad.

Una formulación continua simplificada puede expresarse como:

$$
\boxed{
\frac{dM_s}{dt}
=
R(t)-\mu_sM_s(t)
}
$$

donde:

* \(R(t)\) = tasa de incorporación de machos estériles;
* \(\mu_s\) = tasa de mortalidad o pérdida de machos estériles.

Sin embargo, debido a que las liberaciones pueden ocurrir en momentos específicos, la implementación computacional podrá utilizar una representación discreta:

$$
M_s(t^+)=M_s(t^-)+R_t
$$

seguida de la reducción correspondiente por mortalidad durante el intervalo.

La elección entre una formulación continua o discreta se establecerá durante la implementación del simulador.

---

### 5.4.10 Restricción de producción de la planta

La estrategia de liberación estará limitada por la producción disponible de la planta de Metapa.

Se establece:

$$
\boxed{
R_t\leq A_t\leq C_t
}
$$

donde:

* \(C_t\) = producción disponible;
* \(A_t\) = cantidad disponible para la estrategia;
* \(R_t\) = cantidad liberada.

Esta restricción evita que el modelo proponga estrategias que requieran una cantidad de moscas superior a la disponible bajo el escenario de producción seleccionado.

---

### 5.4.11 Relación entre población silvestre y machos estériles

La relación entre machos estériles y machos silvestres se calculará como:

$$
\boxed{
\rho(t)=\frac{M_s(t)}{M_w(t)}
}
$$

Esta variable permitirá evaluar la intensidad de la presión ejercida por la población estéril.

Cuando \(M_w(t)>0\), un incremento de \(M_s(t)\) producirá un aumento de \(\rho(t)\), siempre que las demás condiciones permanezcan constantes.

La relación de referencia de 10:1 podrá utilizarse posteriormente como escenario de comparación, pero no será considerada una condición universal.

---

### 5.4.12 Población silvestre total

La población adulta silvestre total se calculará mediante:

$$
\boxed{
N_w(t)=M_w(t)+F_v(t)+F_m(t)
}
$$

Esta variable será utilizada principalmente para analizar la evolución global de la población objetivo.

El modelo podrá utilizar \(N_w(t)\) para determinar si se alcanza un criterio de control o erradicación.

---

### 5.4.13 Sistema preliminar de ecuaciones

Integrando las relaciones anteriores, el sistema preliminar puede expresarse como:

$$
\boxed{
\frac{dM_w}{dt}
=
r_MB_v(t)-\mu_MM_w(t)
}
$$

$$
\boxed{
\frac{dF_v}{dt}
=
r_FB_v(t)-A_w(t)-A_s(t)-\mu_FF_v(t)
}
$$

$$
\boxed{
\frac{dF_m}{dt}
=
A_w(t)+A_s(t)-\mu_FF_m(t)
}
$$

$$
\boxed{
\frac{dM_s}{dt}
=
R(t)-\mu_sM_s(t)
}
$$

con:

$$
A_w(t)=aF_v(t)p_w(t)
$$

$$
A_s(t)=aF_v(t)p_s(t)
$$

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

y:

$$
B_v(t)=bA_w(t)
$$

Este conjunto constituye una **formulación preliminar**, no la versión definitiva del modelo.

---

### 5.4.14 Consideraciones para la revisión de las ecuaciones

Antes de implementar estas ecuaciones en Python será necesario revisar:

1. La unidad temporal utilizada.
2. La definición exacta de \(b\).
3. La definición de \(a\).
4. Las tasas de mortalidad.
5. La competitividad relativa \(c\).
6. La supervivencia de los machos estériles.
7. La representación de las liberaciones.
8. La necesidad de incorporar etapas inmaduras.
9. La posible capacidad reproductiva dependiente de la población.
10. La consistencia dimensional de todas las ecuaciones.

También deberá comprobarse que:

$$
M_w(t)\geq0
$$

$$
F_v(t)\geq0
$$

$$
F_m(t)\geq0
$$

$$
M_s(t)\geq0
$$

para todo el periodo de simulación.

### 5.4.15 Estado de la formulación

Las ecuaciones presentadas en esta sección constituyen una primera formulación matemática del modelo.

No se considerarán definitivas hasta completar:

* revisión de parámetros;
* búsqueda y selección de valores científicos;
* análisis dimensional;
* definición de condiciones iniciales;
* análisis de sensibilidad;
* validación;
* implementación computacional.

La finalidad de esta formulación preliminar es establecer una estructura matemática coherente que pueda ser refinada conforme se incorporen datos y evidencia científica.

## 5.5 Condiciones iniciales del modelo

Las condiciones iniciales representan el estado de la población y del sistema de control en el momento en que comienza una simulación.

Estas condiciones son necesarias para resolver el sistema de ecuaciones diferenciales y determinar la evolución de la población a lo largo del tiempo.

La condición inicial general se expresa como:

$$
X(0)=
\begin{bmatrix}
M_w(0)\\
F_v(0)\\
F_m(0)\\
M_s(0)
\end{bmatrix}
$$

donde cada componente representa el estado inicial de una población.

### 5.5.1 Población inicial de machos silvestres

La población inicial de machos silvestres se representa mediante:

$$
M_w(0)
$$

Este valor representa el número estimado de machos silvestres fértiles presentes al inicio de la simulación.

Actualmente este parámetro se encuentra pendiente de determinación.

No se establecerá un valor arbitrario, debido a que una estimación incorrecta de la población inicial puede modificar significativamente los resultados de la simulación.

El valor deberá obtenerse, cuando sea posible, mediante:

* información científica;
* estimaciones poblacionales;
* datos epidemiológicos;
* información de vigilancia;
* modelos previamente publicados;
* o escenarios de población inicial claramente definidos.

### 5.5.2 Población inicial de hembras vírgenes

La población inicial de hembras vírgenes se representa mediante:

$$
F_v(0)
$$

Este valor corresponde a la cantidad estimada de hembras silvestres que todavía no han tenido un apareamiento al inicio de la simulación.

El valor deberá ser determinado a partir de información biológica o mediante una condición inicial derivada de la estructura poblacional seleccionada.

No deberá asumirse automáticamente que:

$$
F_v(0)=M_w(0)
$$

sin una justificación biológica.

### 5.5.3 Población inicial de hembras apareadas

La población inicial de hembras apareadas se representa mediante:

$$
F_m(0)
$$

Este valor representa las hembras que ya han tenido un apareamiento al inicio de la simulación.

Su valor dependerá del estado reproductivo inicial que se quiera representar.

Se podrán considerar diferentes escenarios iniciales cuando no exista información suficiente para determinar un valor único.

### 5.5.4 Población inicial de machos estériles

La población inicial de machos estériles se representa mediante:

$$
M_s(0)
$$

En una simulación que comienza antes de la primera liberación, puede establecerse:

$$
\boxed{
M_s(0)=0
}
$$

En cambio, si la simulación comienza cuando ya existe una población estéril presente en el ambiente, el valor deberá corresponder a la cantidad de machos estériles disponibles en ese momento.

Por lo tanto, el valor de \(M_s(0)\) dependerá del momento seleccionado para iniciar la simulación.

### 5.5.5 Condición inicial de la producción

La producción de la planta de Metapa será representada mediante:

$$
C_t
$$

La producción podrá variar durante la simulación de acuerdo con el escenario seleccionado.

Por ejemplo, podrán analizarse escenarios correspondientes a:

$$
C_{ini}=28\,000\,000
$$

moscas por semana,

$$
C_{max}=100\,000\,000
$$

moscas por semana,

y un escenario futuro de:

$$
C_{fut}=120\,000\,000
$$

moscas por semana.

Estos valores corresponden a escenarios de producción y no deben interpretarse como una producción constante garantizada durante todo el periodo.

### 5.5.6 Condición inicial de liberación

La cantidad de moscas estériles liberadas en cada periodo se representa mediante:

$$
R_t
$$

La primera liberación dependerá de la estrategia seleccionada.

Para una simulación que inicia antes de la primera liberación:

$$
R_0=0
$$

y posteriormente se aplicará la estrategia definida.

Por ejemplo:

$$
R_t=
\begin{cases}
R_1 & \text{si corresponde realizar una liberación}\\
0 & \text{en otro caso}
\end{cases}
$$

La estructura definitiva dependerá de la frecuencia y del tipo de estrategia que se implemente.

### 5.5.7 Condiciones iniciales epidemiológicas

Cuando las variables epidemiológicas formen parte de la simulación, deberán definirse inicialmente:

$$
B(0)
$$

$$
I_b(0)
$$

$$
P(0)
$$

$$
I_p(0)
$$

donde:

* \(B(0)\) = población bovina inicial;
* \(I_b(0)\) = bovinos infestados inicialmente;
* \(P(0)\) = población porcina inicial;
* \(I_p(0)\) = porcinos infestados inicialmente.

Estas variables estarán condicionadas a la disponibilidad de información para el área geográfica seleccionada.

No se asumirán valores nacionales automáticamente si el modelo posteriormente utiliza una escala geográfica menor.

### 5.5.8 Condiciones iniciales y escala geográfica

Las condiciones iniciales deberán ser coherentes con la escala espacial seleccionada.

Por ejemplo, no sería adecuado combinar:

$$
M_w(0)
$$

estimado para una región determinada con:

$$
B(0)
$$

correspondiente a todo México, sin establecer una relación espacial que lo justifique.

Por esta razón, antes de establecer las condiciones iniciales definitivas deberá determinarse la escala geográfica de aplicación del modelo.

### 5.5.9 Escenarios de población inicial

En caso de que no exista una estimación confiable de la población inicial del GBG, se podrán construir escenarios.

Por ejemplo:

| Escenario | Población inicial | Descripción               |
| --------- | ----------------: | ------------------------- |
| I1        |    \(N_{0,bajo}\) | Infestación inicial baja  |
| I2        |   \(N_{0,medio}\) | Infestación inicial media |
| I3        |    \(N_{0,alto}\) | Infestación inicial alta  |

Los valores de estos escenarios deberán establecerse posteriormente con base en datos o rangos científicamente justificables.

No deberán asignarse valores arbitrarios únicamente para ejecutar la simulación.

### 5.5.10 Estado inicial del sistema

De manera general, el estado inicial podrá expresarse como:

$$
\boxed{
X(0)=
\begin{bmatrix}
M_w(0)\\
F_v(0)\\
F_m(0)\\
M_s(0)
\end{bmatrix}
}
$$

con:

$$
M_w(0)=\text{pendiente}
$$

$$
F_v(0)=\text{pendiente}
$$

$$
F_m(0)=\text{pendiente}
$$

y, cuando la simulación comience antes de la primera liberación:

$$
M_s(0)=0
$$

La condición inicial definitiva deberá establecerse antes de la validación del modelo.

### 5.5.11 Requisitos para aceptar una condición inicial

Una condición inicial podrá considerarse adecuada cuando cumpla con:

1. Tener una definición biológica clara.
2. Utilizar unidades consistentes con el modelo.
3. Contar con una fuente o justificación.
4. Ser compatible con la escala espacial seleccionada.
5. Ser compatible con la escala temporal utilizada.
6. No contradecir otras variables iniciales.
7. Permitir reproducir escenarios alternativos cuando exista incertidumbre.

### 5.5.12 Condiciones iniciales y sensibilidad

Debido a que la población inicial puede presentar incertidumbre, se deberá evaluar posteriormente cómo afectan sus diferentes valores al resultado del modelo.

En particular, se analizará el efecto de:

$$
N_w(0)
$$

sobre:

$$
T_C
$$

$$
T_E
$$

y:

$$
R_{total}
$$

Esto permitirá determinar si una estrategia de TIE mantiene su efectividad bajo diferentes niveles iniciales de infestación.

### 5.5.13 Estado actual de las condiciones iniciales

Las condiciones iniciales se clasifican actualmente de la siguiente manera:

| Variable   |   Estado inicial | Situación                                  |
| ---------- | ---------------: | ------------------------------------------ |
| \(M_w(0)\) |        Pendiente | Requiere estimación de población silvestre |
| \(F_v(0)\) |        Pendiente | Requiere estructura poblacional            |
| \(F_m(0)\) |        Pendiente | Requiere estructura reproductiva           |
| \(M_s(0)\) | 0 o condicionado | Depende del momento de inicio              |
| \(B(0)\)   |        Pendiente | Depende de escala geográfica               |
| \(I_b(0)\) |        Pendiente | Requiere datos epidemiológicos             |
| \(P(0)\)   |        Pendiente | Depende de escala geográfica               |
| \(I_p(0)\) |        Pendiente | Requiere datos epidemiológicos             |
| \(C_t\)    |         Variable | Depende del escenario de producción        |
| \(R_t\)    |         Variable | Depende de la estrategia de liberación     |

### 5.5.14 Criterio para establecer las condiciones definitivas

Antes de ejecutar simulaciones de resultados finales, deberán establecerse las condiciones iniciales definitivas y documentar su procedencia.

La prioridad será:

1. Datos oficiales.
2. Estudios científicos.
3. Estimaciones epidemiológicas.
4. Modelos científicos publicados.
5. Rangos derivados de literatura.
6. Escenarios hipotéticos claramente identificados.

Las condiciones iniciales no deberán utilizarse como valores definitivos únicamente porque permitan ejecutar el código.

El objetivo es que cada simulación pueda responder claramente a la pregunta:

> ¿Con qué estado inicial de la población se realizó esta simulación y de dónde proviene ese valor?

De esta manera se mantiene la trazabilidad entre:

$$
\text{Fuente}
\rightarrow
\text{Condición inicial}
\rightarrow
\text{Modelo}
\rightarrow
\text{Simulación}
\rightarrow
\text{Resultado}
$$

Las condiciones iniciales definitivas serán revisadas nuevamente durante la etapa de validación del modelo.

## 5.6 Restricciones del modelo

Las restricciones del modelo establecen las condiciones que deben cumplirse durante la simulación para mantener la coherencia biológica, matemática y operativa del sistema.

Estas restricciones permiten evitar resultados imposibles, como poblaciones negativas, liberaciones superiores a la producción disponible o relaciones matemáticas que no tengan significado biológico.

### 5.6.1 Restricción de no negatividad

Las variables que representan cantidades de individuos deberán mantenerse mayores o iguales a cero:

$$
M_w(t)\geq0
$$

$$
F_v(t)\geq0
$$

$$
F_m(t)\geq0
$$

$$
M_s(t)\geq0
$$

Por lo tanto:

$$
\boxed{
M_w(t),F_v(t),F_m(t),M_s(t)\geq0
}
$$

Una simulación que produzca valores negativos de individuos deberá considerarse matemáticamente inválida y deberá revisarse el método numérico o la formulación de las ecuaciones.

### 5.6.2 Restricción de producción de Metapa

La cantidad de moscas que puede ser liberada durante un periodo no deberá superar la cantidad disponible de producción:

$$
\boxed{
R_t\leq A_t
}
$$

donde:

* \(R_t\) = cantidad liberada;
* \(A_t\) = cantidad disponible para la estrategia.

A su vez:

$$
\boxed{
A_t\leq C_t
}
$$

donde:

* \(C_t\) = producción disponible de la planta durante el periodo.

Por lo tanto, la restricción completa será:

$$
\boxed{
R_t\leq A_t\leq C_t
}
$$

Esta condición garantiza que las estrategias simuladas sean compatibles con la capacidad productiva considerada.

### 5.6.3 Restricción de liberación no negativa

La cantidad liberada tampoco podrá ser negativa:

$$
\boxed{
R_t\geq0
}
$$

Una estrategia podrá establecer:

$$
R_t=0
$$

cuando no exista una liberación durante determinado periodo.

### 5.6.4 Restricción de disponibilidad de machos estériles

La cantidad de machos estériles presentes en el sistema deberá ser no negativa:

$$
M_s(t)\geq0
$$

Además, su dinámica deberá considerar las liberaciones y las pérdidas por mortalidad o supervivencia limitada.

Conceptualmente:

$$
M_s(t+\Delta t)
=
M_s(t)
+
R_t
-
L_s(t)
$$

donde \(L_s(t)\) representa las pérdidas de machos estériles durante el periodo.

En consecuencia, no podrá suponerse que:

$$
M_s(t)=R_t
$$

para todos los periodos.

### 5.6.5 Restricción de población silvestre

La población silvestre total deberá mantenerse dentro de valores físicamente posibles:

$$
N_w(t)\geq0
$$

donde:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

Por definición:

$$
\boxed{
N_w(t)\geq0
}
$$

### 5.6.6 Restricción de proporciones

Las proporciones de apareamiento deberán encontrarse dentro del intervalo:

$$
0\leq p_s(t)\leq1
$$

y:

$$
0\leq p_w(t)\leq1
$$

Además:

$$
\boxed{
p_s(t)+p_w(t)=1
}
$$

cuando el modelo considere únicamente estas dos posibilidades de apareamiento.

### 5.6.7 Restricción de competitividad

La competitividad relativa:

$$
c
$$

deberá ser un valor no negativo:

$$
\boxed{
c\geq0
}
$$

Un valor:

$$
c=0
$$

representaría un escenario en el que los machos estériles no tienen capacidad efectiva de competir por apareamientos.

Un valor positivo:

$$
c>0
$$

representará cierta capacidad competitiva.

El valor específico deberá establecerse mediante evidencia científica o análisis de escenarios.

### 5.6.8 Restricción de la relación estéril:silvestre

La relación:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

solo podrá calcularse directamente cuando:

$$
M_w(t)>0
$$

Si:

$$
M_w(t)=0
$$

la razón deberá tratarse de manera especial en la implementación para evitar una división entre cero.

En ese caso, el modelo podrá registrar que la población silvestre ha alcanzado el criterio de erradicación antes de intentar calcular una razón convencional.

### 5.6.9 Restricción de apareamientos

Los apareamientos efectivos no podrán ser negativos:

$$
A_w(t)\geq0
$$

$$
A_s(t)\geq0
$$

Además, bajo la formulación preliminar:

$$
A_w(t)+A_s(t)\leq aF_v(t)
$$

y, si todas las hembras disponibles tienen una oportunidad de apareamiento durante el intervalo considerado:

$$
A_w(t)+A_s(t)=aF_v(t)
$$

La relación definitiva dependerá de cómo se defina el parámetro \(a\) y de la resolución temporal utilizada.

### 5.6.10 Restricción de reproducción

La producción de descendencia viable deberá ser no negativa:

$$
\boxed{
B_v(t)\geq0
}
$$

Si se utiliza:

$$
B_v(t)=bA_w(t)
$$

entonces deberán cumplirse:

$$
b\geq0
$$

y:

$$
A_w(t)\geq0
$$

### 5.6.11 Restricción de mortalidad

Las tasas de mortalidad utilizadas en el modelo deberán ser no negativas:

$$
\mu_M\geq0
$$

$$
\mu_F\geq0
$$

$$
\mu_s\geq0
$$

Estas tasas deberán tener unidades compatibles con la unidad temporal seleccionada.

### 5.6.12 Restricción de supervivencia

Cuando se utilicen parámetros expresados como proporciones de supervivencia, estos deberán encontrarse dentro del intervalo:

$$
0\leq S\leq1
$$

Por ejemplo:

$$
0\leq S_s\leq1
$$

para la supervivencia de machos estériles.

No deberán confundirse las tasas de mortalidad con las proporciones de supervivencia.

### 5.6.13 Restricción de proporción sexual

Si se utiliza una proporción de individuos machos y hembras:

$$
r_M+r_F=1
$$

con:

$$
0\leq r_M\leq1
$$

$$
0\leq r_F\leq1
$$

Esta condición deberá mantenerse durante la generación de nuevos individuos cuando el modelo utilice una proporción sexual fija.

### 5.6.14 Restricción de capacidad productiva

La capacidad máxima considerada para cada escenario deberá respetar las condiciones establecidas en la matriz de parámetros.

Entre los escenarios definidos se encuentran:

$$
C_{ini}=28\,000\,000
$$

moscas por semana,

$$
C_{max}=100\,000\,000
$$

moscas por semana,

y:

$$
C_{fut}=120\,000\,000
$$

moscas por semana como escenario futuro.

El valor de 120 millones de moscas por semana deberá permanecer identificado como escenario de expansión y no como capacidad actual garantizada.

### 5.6.15 Restricción temporal de liberaciones

Las liberaciones deberán ocurrir únicamente en los periodos establecidos por la estrategia.

Si:

$$
\Delta t_R
$$

representa el intervalo entre liberaciones, entonces la simulación deberá respetar dicho intervalo.

Una estrategia podrá representarse de manera conceptual como:

$$
R_t=
\begin{cases}
R & \text{si }t\text{ corresponde a una liberación}\\
0 & \text{en otro caso}
\end{cases}
$$

Esto permitirá comparar estrategias con diferentes frecuencias.

### 5.6.16 Restricción de duración

La estrategia de liberación deberá tener una duración definida:

$$
T_R\geq0
$$

Durante el periodo:

$$
0\leq t\leq T_R
$$

se aplicarán las liberaciones establecidas por la estrategia.

Después de finalizar la estrategia:

$$
t>T_R
$$

se podrá establecer:

$$
R_t=0
$$

si el escenario así lo determina.

### 5.6.17 Restricción de criterios de control y erradicación

Los criterios de control y erradicación deberán respetar:

$$
N_E\leq N_C
$$

donde:

* \(N_C\) = umbral de control;
* \(N_E\) = umbral de erradicación.

Esto permite que el criterio de erradicación sea igual o más estricto que el criterio de control.

El valor definitivo de ambos parámetros queda pendiente de establecer mediante criterios científicos u operativos.

### 5.6.18 Restricción de tiempo de simulación

El periodo total de simulación deberá ser suficiente para observar la respuesta de la población.

Se definirá:

$$
0\leq t\leq T_{sim}
$$

donde \(T_{sim}\) representa la duración total de la simulación.

Si el criterio de control o erradicación no se alcanza durante este periodo:

$$
T_E>T_{sim}
$$

o podrá registrarse como:

$$
T_E=\text{no alcanzado}
$$

según la implementación seleccionada.

### 5.6.19 Restricción de consistencia dimensional

Todas las ecuaciones deberán mantener consistencia entre sus unidades.

Por ejemplo, si:

$$
\frac{dM_w}{dt}
$$

representa individuos por unidad de tiempo, entonces todos los términos del lado derecho deberán tener las mismas unidades.

Para:

$$
\frac{dM_w}{dt}
=
r_MB_v-\mu_MM_w
$$

los términos deberán ser compatibles dimensionalmente:

$$
[r_MB_v]=\text{individuos/tiempo}
$$

y:

$$
[\mu_MM_w]=\text{individuos/tiempo}
$$

Esta revisión será obligatoria antes de implementar las ecuaciones definitivamente.

### 5.6.20 Restricción de trazabilidad

Cada parámetro utilizado en una ecuación deberá poder relacionarse con su fuente, estimación o escenario.

La cadena de trazabilidad será:

$$
\boxed{
Fuente
\rightarrow
Parámetro
\rightarrow
Ecuación
\rightarrow
Simulación
\rightarrow
Resultado
}
$$

Los parámetros que todavía no cuenten con evidencia suficiente deberán permanecer identificados como pendientes, estimados o pertenecientes a un escenario.

### 5.6.21 Restricción de no arbitrariedad

El modelo no deberá introducir valores numéricos únicamente para conseguir que la simulación produzca un resultado determinado.

Cuando un parámetro no pueda determinarse directamente, se utilizará preferentemente:

* un rango;
* un escenario;
* una distribución de incertidumbre;
* o una estimación respaldada por literatura.

Esto permitirá diferenciar los resultados derivados de evidencia de aquellos obtenidos mediante escenarios hipotéticos.

### 5.6.22 Resumen de restricciones

Las principales restricciones del modelo pueden resumirse como:

$$
\boxed{
M_w,F_v,F_m,M_s\geq0
}
$$

$$
\boxed{
R_t\geq0
}
$$

$$
\boxed{
R_t\leq A_t\leq C_t
}
$$

$$
\boxed{
0\leq p_s,p_w\leq1
}
$$

$$
\boxed{
p_s+p_w=1
}
$$

$$
\boxed{
c\geq0
}
$$

$$
\boxed{
\mu_M,\mu_F,\mu_s\geq0
}
$$

$$
\boxed{
0\leq S\leq1
}
$$

$$
\boxed{
N_E\leq N_C
}
$$

Estas restricciones deberán implementarse tanto en la formulación matemática como posteriormente en el código Python.

### 5.6.23 Importancia de las restricciones

Las restricciones permitirán que el modelo no solo produzca resultados matemáticamente calculables, sino resultados que mantengan una interpretación biológica y operacional.

En particular, la restricción:

$$
R_t\leq A_t\leq C_t
$$

garantiza que las estrategias simuladas respeten la disponibilidad de moscas estériles de la planta de Metapa bajo el escenario seleccionado.

Por otra parte, las restricciones de no negatividad, proporciones y consistencia dimensional permitirán detectar errores durante la implementación y validación del modelo.

Las restricciones serán revisadas nuevamente cuando se complete la formulación definitiva de las ecuaciones.

## 5.7 Criterios de control y erradicación

El modelo deberá establecer criterios cuantitativos que permitan determinar cuándo una estrategia de liberación de moscas estériles ha logrado reducir la población silvestre del gusano barrenador del ganado (GBG) hasta un nivel definido de control o erradicación.

Estos criterios serán utilizados posteriormente para calcular el tiempo necesario para alcanzar cada condición.

Se distinguirán dos conceptos:

* **Control:** reducción de la población hasta un nivel establecido como aceptable para el escenario de estudio.
* **Erradicación:** cumplimiento de una condición más estricta que represente la eliminación o interrupción sostenida de la población objetivo bajo los criterios definidos por el proyecto.

### 5.7.1 Variable utilizada para evaluar el estado de la población

La principal variable utilizada para evaluar la evolución de la población será:

$$
N_w(t)
$$

donde:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

representa la población adulta silvestre total.

Esta variable permitirá comparar el tamaño de la población durante cada periodo de la simulación.

### 5.7.2 Criterio de control

El control se representará mediante un umbral:

$$
\boxed{
N_w(t)\leq N_C
}
$$

donde:

* \(N_w(t)\) = población silvestre en el tiempo \(t\);
* \(N_C\) = umbral establecido para considerar que existe control.

El valor de \(N_C\) permanecerá inicialmente como parámetro pendiente.

No se establecerá arbitrariamente un valor de control sin una justificación científica, epidemiológica u operativa.

### 5.7.3 Tiempo para alcanzar el control

El tiempo de control se definirá como el primer momento en que la población alcance o se encuentre por debajo del umbral:

$$
\boxed{
T_C=\min\{t:N_w(t)\leq N_C\}
}
$$

Esto permitirá calcular cuánto tiempo tarda una estrategia determinada en alcanzar el nivel de control establecido.

Si la población nunca alcanza el umbral durante la simulación:

$$
T_C=\text{no alcanzado}
$$

o:

$$
T_C>T_{sim}
$$

según la implementación computacional.

### 5.7.4 Criterio de erradicación

La erradicación se representará mediante un criterio más estricto:

$$
\boxed{
N_w(t)\leq N_E
}
$$

donde:

* \(N_E\) = umbral de erradicación.

Deberá cumplirse:

$$
N_E\leq N_C
$$

para que el criterio de erradicación sea igual o más estricto que el de control.

El valor definitivo de \(N_E\) deberá establecerse posteriormente con base en criterios científicos u operativos apropiados.

### 5.7.5 Tiempo para alcanzar la erradicación

El tiempo de erradicación se calculará como:

$$
\boxed{
T_E=\min\{t:N_w(t)\leq N_E\}
}
$$

Este será uno de los resultados principales del modelo.

Permitirá comparar diferentes estrategias de liberación en función del tiempo requerido para alcanzar el criterio establecido.

### 5.7.6 Criterio de erradicación sostenida

Alcanzar temporalmente el umbral no necesariamente significa que la población haya sido eliminada de manera estable.

Por ello, se podrá establecer posteriormente un criterio de permanencia.

Por ejemplo:

$$
N_w(t)\leq N_E
$$

durante un periodo mínimo:

$$
T_S
$$

donde \(T_S\) representa el tiempo de permanencia requerido por debajo del umbral.

En este caso, el criterio sería:

$$
\boxed{
N_w(t)\leq N_E
\quad
\forall t\in[t^*,t^*+T_S]
}
$$

donde \(t^*\) representa el momento en que se alcanza inicialmente el umbral.

Este criterio permitirá diferenciar entre:

* una reducción temporal de la población;
* una reducción sostenida de la población.

El valor de \(T_S\) quedará pendiente de establecer.

### 5.7.7 Criterio basado en ausencia de recuperación

Además del tamaño de la población, podrá evaluarse si la población presenta una recuperación posterior.

Una estrategia será considerada más robusta cuando, después de alcanzar el criterio:

$$
N_w(t)\leq N_E
$$

no se observe un crecimiento posterior que supere nuevamente el umbral.

Conceptualmente:

$$
N_w(t)\leq N_E
$$

durante el periodo de evaluación posterior.

Esto permitirá identificar estrategias que producen una disminución temporal pero no suficiente para mantener la población bajo control.

### 5.7.8 Criterio basado en población silvestre

El modelo utilizará inicialmente la población silvestre como indicador principal:

$$
N_w(t)
$$

La población de machos estériles:

$$
M_s(t)
$$

no será utilizada por sí misma como criterio de control.

Su función será representar la presión de la TIE sobre la población silvestre.

Por lo tanto:

$$
M_s(t)\uparrow
$$

no implica automáticamente:

$$
N_w(t)\downarrow
$$

ya que el resultado dependerá también de la competitividad, supervivencia, reproducción y dinámica de la población silvestre.

### 5.7.9 Relación con la proporción estéril:silvestre

La relación:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

se utilizará como indicador de la intensidad de la estrategia de liberación.

Sin embargo, no será utilizada como criterio directo de erradicación.

Por ejemplo, una relación:

$$
\rho(t)=10
$$

no significa por sí misma que la población haya sido controlada o erradicada.

La relación deberá interpretarse junto con:

$$
N_w(t)
$$

y el resto de los parámetros del modelo.

### 5.7.10 Criterios de control para bovinos y porcinos

Cuando el componente epidemiológico sea incorporado al modelo, podrán utilizarse adicionalmente:

$$
I_b(t)
$$

para bovinos infestados y:

$$
I_p(t)
$$

para porcinos infestados.

En ese caso, podrán establecerse criterios complementarios relacionados con la reducción de infestaciones.

Sin embargo, estos criterios no sustituirán automáticamente al criterio poblacional del GBG.

La relación entre población de moscas e infestaciones deberá estar respaldada por información epidemiológica suficiente.

### 5.7.11 Criterio combinado

Una versión posterior del modelo podrá utilizar un criterio combinado.

Por ejemplo:

$$
N_w(t)\leq N_E
$$

y simultáneamente:

$$
I_b(t)\leq I_{b,E}
$$

$$
I_p(t)\leq I_{p,E}
$$

donde:

* \(I_{b,E}\) = umbral de infestación bovina;
* \(I_{p,E}\) = umbral de infestación porcina.

Sin embargo, este criterio solo será incorporado si existen datos suficientes para relacionar adecuadamente la dinámica del GBG con la infestación de los hospedadores.

### 5.7.12 Criterio de éxito de una estrategia

Una estrategia de liberación podrá considerarse exitosa cuando:

1. Respete la capacidad disponible de producción.
2. Mantenga las variables dentro de límites biológicamente válidos.
3. Alcance el criterio de control o erradicación.
4. Mantenga la población bajo el umbral durante el periodo requerido, cuando aplique.
5. Utilice una cantidad de moscas compatible con la producción de Metapa.

Por lo tanto, la efectividad no dependerá únicamente de reducir la población.

La estrategia deberá ser también factible bajo las restricciones de producción.

### 5.7.13 Comparación entre estrategias

Para comparar diferentes estrategias se utilizarán como indicadores principales:

$$
T_C
$$

$$
T_E
$$

$$
R_{total}
$$

$$
U_C
$$

y:

$$
N_{w,f}
$$

Estos indicadores permitirán responder preguntas como:

* ¿Qué estrategia alcanza primero el criterio de control?
* ¿Qué estrategia alcanza primero el criterio de erradicación?
* ¿Cuántas moscas estériles requiere?
* ¿Qué porcentaje de la capacidad de Metapa utiliza?
* ¿Cuál deja una menor población final?
* ¿Qué estrategia mantiene el efecto durante más tiempo?

### 5.7.14 Criterio de factibilidad

Una estrategia será considerada matemáticamente factible cuando:

$$
R_t\leq A_t\leq C_t
$$

para todos los periodos de simulación.

Si una estrategia requiere:

$$
R_t>C_t
$$

en algún periodo, será considerada incompatible con la capacidad productiva del escenario seleccionado.

Por ejemplo, una estrategia que requiera 120 millones de moscas en un periodo en el que la producción disponible sea de 100 millones no podrá considerarse factible bajo ese escenario.

### 5.7.15 Criterio de eficiencia

Además de la factibilidad, podrá evaluarse la eficiencia relativa de una estrategia.

Una estrategia podrá considerarse más eficiente cuando alcance el mismo criterio utilizando:

* menor cantidad total de moscas;
* menor tiempo;
* menor utilización de capacidad;
* o una combinación de estos factores.

De manera conceptual:

$$
\text{Eficiencia}
=
f(T_E,R_{total},U_C,N_{w,f})
$$

La función definitiva de eficiencia se establecerá posteriormente, evitando asignar pesos arbitrarios antes de contar con una justificación metodológica.

### 5.7.16 Situaciones posibles durante la simulación

El modelo deberá distinguir al menos entre las siguientes situaciones:

| Situación                 | Condición                                                     |
| ------------------------- | ------------------------------------------------------------- |
| No controlado             | \(N_w(t)>N_C\)                                                |
| Control alcanzado         | \(N_w(t)\leq N_C\)                                            |
| Erradicación alcanzada    | \(N_w(t)\leq N_E\)                                            |
| Control no alcanzado      | \(N_w(t)>N_C\) durante toda la simulación                     |
| Erradicación no alcanzada | \(N_w(t)>N_E\) durante toda la simulación                     |
| Recuperación              | La población vuelve a superar el umbral después de alcanzarlo |
| Estrategia no factible    | \(R_t>C_t\) en algún periodo                                  |

Esta clasificación facilitará posteriormente la interpretación automática de los resultados en Python.

### 5.7.17 Variables necesarias para los criterios

Los principales parámetros y variables relacionados con los criterios serán:

| Elemento                | Símbolo     | Estado    |
| ----------------------- | ----------- | --------- |
| Población silvestre     | \(N_w(t)\)  | Calculada |
| Umbral de control       | \(N_C\)     | Pendiente |
| Umbral de erradicación  | \(N_E\)     | Pendiente |
| Tiempo de control       | \(T_C\)     | Calculado |
| Tiempo de erradicación  | \(T_E\)     | Calculado |
| Periodo de permanencia  | \(T_S\)     | Pendiente |
| Población final         | \(N_{w,f}\) | Calculada |
| Capacidad de producción | \(C_t\)     | Variable  |
| Liberación              | \(R_t\)     | Variable  |

### 5.7.18 Criterio provisional para la primera implementación

Para la primera versión computacional se utilizará inicialmente el criterio:

$$
N_w(t)\leq N_C
$$

para identificar control y:

$$
N_w(t)\leq N_E
$$

para identificar erradicación.

Los valores de \(N_C\) y \(N_E\) permanecerán como parámetros configurables.

Esto permitirá desarrollar y probar la estructura computacional sin fijar prematuramente valores que todavía no cuentan con suficiente respaldo.

Posteriormente, los umbrales serán sustituidos por valores justificados mediante evidencia científica, epidemiológica u operativa.

### 5.7.19 Principio de interpretación

Los criterios de control y erradicación serán utilizados como reglas matemáticas para interpretar la salida del modelo.

No deberán interpretarse automáticamente como una declaración de erradicación real del GBG en México.

La interpretación final dependerá de:

* calidad de los datos;
* incertidumbre de los parámetros;
* validez del modelo;
* escala espacial;
* condiciones iniciales;
* estrategia de liberación;
* capacidad productiva;
* validación con datos independientes.

Por lo tanto:

$$
\boxed{
\text{Criterio matemático alcanzado}
\neq
\text{confirmación epidemiológica de erradicación}
}
$$

El modelo permitirá estimar cuándo se alcanza una condición definida bajo los supuestos establecidos, pero la confirmación de erradicación requerirá evidencia epidemiológica independiente.

## 5.8 Representación matemática de la producción y liberación de moscas estériles

La estrategia de Técnica del Insecto Estéril (TIE) depende de la disponibilidad de machos estériles para ser liberados sobre la población silvestre.

En el modelo, la producción de moscas estériles se representará mediante la capacidad de la planta de Metapa de Domínguez, Chiapas, mientras que la liberación será considerada como una decisión de la estrategia de control.

Para evitar confundir la capacidad industrial con la cantidad efectivamente liberada, se utilizarán tres conceptos diferentes:

$$
\boxed{
\text{Producción} \rightarrow \text{Disponibilidad} \rightarrow \text{Liberación}
}
$$

### 5.8.1 Capacidad de producción

La capacidad disponible de la planta durante un periodo \(t\) será representada mediante:

$$
C_t
$$

donde:

* \(C_t\) = cantidad máxima de moscas estériles que puede producirse durante el periodo \(t\).

Para la primera versión del modelo se considerarán los escenarios de capacidad documentados para la planta de Metapa:

$$
C_{ini}=28\,000\,000
$$

moscas por semana como escenario inicial de producción.

También se considerará:

$$
C_{max}=100\,000\,000
$$

moscas por semana como escenario de capacidad proyectada.

Finalmente, podrá evaluarse un escenario futuro:

$$
C_{fut}=120\,000\,000
$$

moscas por semana.

Estos valores serán tratados como escenarios de capacidad y no como producción histórica constante durante todo el periodo de simulación.

### 5.8.2 Disponibilidad para la estrategia

No toda la producción necesariamente estará disponible para una estrategia específica de liberación.

Por ello se define:

$$
A_t
$$

como la cantidad de moscas estériles disponibles para ser asignadas a la estrategia durante el periodo \(t\).

Debe cumplirse:

$$
\boxed{
A_t\leq C_t
}
$$

donde:

* \(A_t\) = moscas disponibles para la estrategia;
* \(C_t\) = capacidad de producción correspondiente al periodo.

Esta separación permite incorporar posteriormente factores como almacenamiento, distribución, pérdidas operativas u otras restricciones, siempre que existan datos suficientes para parametrizarlos.

### 5.8.3 Cantidad liberada

La cantidad efectivamente liberada será representada por:

$$
R_t
$$

donde:

* \(R_t\) = número de moscas estériles liberadas durante el periodo \(t\).

La cantidad liberada deberá cumplir:

$$
\boxed{
R_t\leq A_t
}
$$

Por lo tanto:

$$
\boxed{
R_t\leq A_t\leq C_t
}
$$

Esta será una de las principales restricciones de factibilidad del modelo.

### 5.8.4 Relación entre producción, disponibilidad y liberación

El flujo matemático será:

$$
C_t\rightarrow A_t\rightarrow R_t
$$

donde:

$$
C_t=\text{capacidad de producción}
$$

$$
A_t=\text{cantidad disponible}
$$

$$
R_t=\text{cantidad liberada}
$$

De esta manera, el modelo podrá distinguir entre una estrategia que necesita una cantidad determinada de moscas y una estrategia que realmente puede ser abastecida por la planta.

### 5.8.5 Incorporación de los machos estériles a la población

Una vez liberados, los machos estériles pasan a formar parte de la población estéril presente en el área modelada.

Esta población será representada por:

$$
M_s(t)
$$

Su dinámica se representará inicialmente mediante:

$$
\boxed{
\frac{dM_s}{dt}=R(t)-\mu_sM_s(t)
}
$$

donde:

* \(M_s(t)\) = número de machos estériles presentes;
* \(R(t)\) = tasa de incorporación de machos estériles mediante liberaciones;
* \(\mu_s\) = tasa de mortalidad de los machos estériles.

Esta ecuación representa el balance entre la incorporación de nuevos individuos mediante las liberaciones y la pérdida de individuos por mortalidad.

### 5.8.6 Representación de liberaciones discretas

En la práctica, las liberaciones pueden realizarse en fechas o intervalos determinados.

Por ello, cuando la liberación se represente como un evento discreto, se utilizará:

$$
\boxed{
M_s(t^+)=M_s(t^-)+R_t
}
$$

donde:

* \(t^-\) = instante inmediatamente anterior a la liberación;
* \(t^+\) = instante inmediatamente posterior;
* \(R_t\) = cantidad liberada en ese momento.

Esta representación permitirá modelar estrategias como:

* liberaciones semanales;
* liberaciones cada determinado número de días;
* liberaciones con cantidades variables;
* periodos sin liberación;
* incrementos o reducciones progresivas.

### 5.8.7 Estrategia de liberación

La estrategia de liberación estará definida mediante:

$$
S_R=\{R_t,\Delta t_R,T_R\}
$$

donde:

* \(R_t\) = cantidad liberada;
* \(\Delta t_R\) = intervalo entre liberaciones;
* \(T_R\) = duración del periodo de liberación.

Esto permitirá comparar diferentes estrategias sin modificar la estructura fundamental del modelo.

### 5.8.8 Liberación constante

Una estrategia básica podrá representarse mediante una cantidad constante:

$$
R_t=R
$$

para cada periodo de liberación.

Por ejemplo, si se establece una liberación semanal:

$$
R_1=R_2=R_3=\cdots=R_n=R
$$

Esta estrategia permitirá estudiar el efecto de mantener una presión constante de machos estériles sobre la población silvestre.

El valor de \(R\) será una variable configurable y no se fijará arbitrariamente como estrategia definitiva.

### 5.8.9 Liberación proporcional a la población silvestre

Otra estrategia podrá relacionar la cantidad de machos estériles con la población silvestre estimada.

Conceptualmente:

$$
R_t=\rho_R M_w(t)
$$

donde:

* \(\rho_R\) = proporción de liberación deseada;
* \(M_w(t)\) = machos silvestres presentes.

Sin embargo, esta estrategia deberá respetar:

$$
R_t\leq C_t
$$

Por lo tanto, una demanda de liberación superior a la capacidad disponible no será considerada factible.

### 5.8.10 Relación estériles:silvestres

La intensidad de la TIE podrá evaluarse mediante:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

Esta relación permite conocer cuántos machos estériles se encuentran disponibles en relación con los machos silvestres.

Como referencia operacional, se podrá evaluar inicialmente una relación:

$$
\rho_{ref}=10:1
$$

sin considerarla una constante biológica universal.

El modelo permitirá modificar este parámetro posteriormente cuando exista evidencia suficiente para establecer otros valores.

### 5.8.11 Competencia reproductiva

La presencia de machos estériles modifica la probabilidad de que una hembra se aparee con un macho silvestre.

La probabilidad de apareamiento con un macho estéril se representará inicialmente mediante:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

Mientras que la probabilidad de apareamiento con un macho silvestre será:

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

por lo que:

$$
p_s(t)+p_w(t)=1
$$

El parámetro:

$$
c
$$

representará la competitividad relativa de los machos estériles respecto a los machos silvestres.

Su valor permanecerá pendiente de validación científica.

### 5.8.12 Efecto de la capacidad de producción

La capacidad de producción de Metapa limitará las estrategias posibles.

Si:

$$
R_t\leq C_t
$$

la estrategia será compatible con la capacidad de producción considerada.

Si:

$$
R_t>C_t
$$

la estrategia será considerada no factible para ese escenario.

Por ejemplo, una estrategia que demande:

$$
R_t=110\,000\,000
$$

moscas durante una semana no podrá ejecutarse bajo un escenario cuya capacidad disponible sea:

$$
C_t=100\,000\,000
$$

moscas por semana.

El modelo deberá identificar automáticamente esta condición.

### 5.8.13 Capacidad variable durante la simulación

La capacidad de producción podrá variar durante el tiempo.

Por ejemplo, una simulación podrá considerar inicialmente:

$$
C_t=28\,000\,000
$$

moscas por semana y posteriormente incrementar la capacidad:

$$
C_t=100\,000\,000
$$

moscas por semana.

Esto permitirá representar un escenario de incremento progresivo de la capacidad productiva de la planta.

La transición exacta entre capacidades deberá definirse posteriormente con base en información oficial sobre la evolución de la producción.

### 5.8.14 Cantidad total liberada

La cantidad acumulada de moscas liberadas durante la simulación será:

$$
\boxed{
R_{total}=\sum_{t=1}^{n}R_t
}
$$

donde:

* \(R_{total}\) = cantidad total de moscas liberadas;
* \(R_t\) = cantidad liberada durante el periodo \(t\);
* \(n\) = número total de periodos de liberación.

Este indicador permitirá comparar el consumo total de moscas entre diferentes estrategias.

### 5.8.15 Utilización de la capacidad productiva

Se definirá un indicador de utilización de capacidad:

$$
\boxed{
U_C=
\frac{\sum R_t}
{\sum C_t}
}
$$

donde:

* \(U_C\) = utilización acumulada de la capacidad productiva;
* \(R_t\) = cantidad liberada;
* \(C_t\) = capacidad disponible.

También podrá calcularse por periodo:

$$
U_{C,t}=\frac{R_t}{C_t}
$$

Este indicador permitirá identificar qué proporción de la capacidad disponible está utilizando cada estrategia.

### 5.8.16 Estrategias que superen la capacidad de Metapa

Cuando una estrategia requiera una cantidad superior a la producción disponible:

$$
R_t>C_t
$$

el modelo no deberá incrementar artificialmente la producción para cumplir la estrategia.

En su lugar, deberá marcar la estrategia como:

**No factible por restricción de producción.**

Esto es importante para mantener la relación entre el modelo matemático y la capacidad real considerada para la planta de Metapa.

### 5.8.17 Escenarios de producción

Para comparar estrategias se utilizarán inicialmente tres escenarios:

| Escenario  |           Capacidad |
| ---------- | ------------------: |
| Inicial    |  28 millones/semana |
| Proyectado | 100 millones/semana |
| Futuro     | 120 millones/semana |

El escenario de 120 millones de moscas por semana será tratado como una posibilidad futura y no como la capacidad actual confirmada.

### 5.8.18 Variables principales de producción y liberación

| Variable                   | Símbolo       | Unidad         | Estado                   |
| -------------------------- | ------------- | -------------- | ------------------------ |
| Capacidad de producción    | \(C_t\)       | moscas/periodo | Confirmada por escenario |
| Disponibilidad             | \(A_t\)       | moscas/periodo | Calculada/configurable   |
| Liberación                 | \(R_t\)       | moscas/periodo | Configurable             |
| Población estéril          | \(M_s(t)\)    | moscas         | Calculada                |
| Mortalidad estéril         | \(\mu_s\)     | 1/tiempo       | Pendiente                |
| Relación estéril:silvestre | \(\rho(t)\)   | proporción     | Calculada                |
| Liberación acumulada       | \(R_{total}\) | moscas         | Calculada                |
| Utilización de capacidad   | \(U_C\)       | proporción     | Calculada                |

### 5.8.19 Consideración sobre la disponibilidad real

La capacidad nominal de producción no deberá interpretarse automáticamente como cantidad liberable.

En el modelo se mantendrá la distinción:

$$
\boxed{
C_t\neq A_t\neq R_t
}
$$

salvo que los datos disponibles permitan justificar que estas cantidades son equivalentes para un escenario determinado.

Esta separación permitirá incorporar posteriormente restricciones relacionadas con preparación, distribución, almacenamiento o disponibilidad operativa, sin modificar la estructura fundamental del modelo.

### 5.8.20 Integración con el modelo poblacional

La producción y liberación de moscas estériles se integrará con la dinámica de la población silvestre mediante:

$$
C_t\rightarrow A_t\rightarrow R_t\rightarrow M_s(t)
$$

y posteriormente:

$$
M_s(t)\rightarrow p_s(t)\rightarrow A_s(t)
$$

donde \(A_s(t)\) representa los apareamientos de hembras con machos estériles.

El flujo completo será:

$$
\boxed{
\text{Metapa}
\rightarrow
C_t
\rightarrow
A_t
\rightarrow
R_t
\rightarrow
M_s(t)
\rightarrow
p_s(t)
\rightarrow
\text{reducción reproductiva}
\rightarrow
N_w(t)
}
$$

De esta manera, la capacidad productiva de la planta se convierte en una restricción directa de las estrategias de control evaluadas por el modelo.

### 5.8.21 Principio de trazabilidad

Toda estrategia simulada deberá mantener la relación:

$$
\boxed{
\text{Capacidad}
\rightarrow
\text{Disponibilidad}
\rightarrow
\text{Liberación}
\rightarrow
\text{Población estéril}
\rightarrow
\text{Efecto poblacional}
}
$$

Esto permitirá identificar cómo una modificación en la capacidad de producción o en la estrategia de liberación afecta los resultados finales del modelo.

La estructura también permitirá posteriormente conectar el modelo matemático con el simulador y, en una fase posterior, con la plataforma web.

## 5.9 Solución numérica del modelo

El modelo matemático definido en las secciones anteriores está compuesto por ecuaciones diferenciales que describen la evolución de la población silvestre y de la población de machos estériles a lo largo del tiempo.

Debido a que estas ecuaciones no necesariamente tendrán una solución analítica sencilla, se utilizarán métodos numéricos para obtener una aproximación de la evolución de las variables del sistema.

La solución numérica permitirá transformar el modelo matemático en un modelo computacional ejecutable en Python.

### 5.9.1 Sistema de ecuaciones a resolver

El sistema preliminar está definido por:

$$
\frac{dM_w}{dt}=r_MB_v-\mu_MM_w
$$

$$
\frac{dF_v}{dt}=r_FB_v-A_w-A_s-\mu_FF_v
$$

$$
\frac{dF_m}{dt}=A_w+A_s-\mu_FF_m
$$

$$
\frac{dM_s}{dt}=R(t)-\mu_sM_s
$$

con:

$$
B_v(t)=bA_w(t)
$$

$$
A_w(t)=aF_v(t)p_w(t)
$$

$$
A_s(t)=aF_v(t)p_s(t)
$$

y:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

Este sistema será implementado inicialmente como una aproximación numérica y podrá modificarse posteriormente conforme se validen los parámetros y supuestos biológicos.

### 5.9.2 Método de integración numérica

Para la primera implementación computacional se utilizará un método de integración numérica para ecuaciones diferenciales ordinarias.

Como primera opción se utilizará el método **Runge-Kutta de cuarto y quinto orden con control adaptativo del paso**, disponible mediante la función `solve_ivp` de la biblioteca `SciPy`.

La implementación permitirá calcular:

$$
X(t)
$$

para diferentes instantes durante el periodo de simulación.

El vector de estado será:

$$
X(t)=
\begin{bmatrix}
M_w(t)\\
F_v(t)\\
F_m(t)\\
M_s(t)
\end{bmatrix}
$$

### 5.9.3 Representación computacional

En Python, el sistema podrá representarse conceptualmente mediante una función:

```python
def modelo_gbg(t, estado, parametros):
    Mw, Fv, Fm, Ms = estado

    # Cálculo de probabilidades de apareamiento
    # Cálculo de apareamientos
    # Cálculo de descendencia viable
    # Cálculo de las tasas de cambio

    return [dMw_dt, dFv_dt, dFm_dt, dMs_dt]
```

La función recibirá:

* tiempo \(t\);
* vector de estado;
* parámetros del modelo.

Y devolverá:

$$
\frac{dX}{dt}
$$

es decir, las tasas de cambio de cada variable.

### 5.9.4 Intervalo de simulación

La simulación estará definida dentro de un intervalo:

$$
0\leq t\leq T_{sim}
$$

donde:

* \(t\) = tiempo transcurrido;
* \(T_{sim}\) = duración máxima de la simulación.

La unidad de tiempo deberá mantenerse consistente con las unidades utilizadas por los parámetros biológicos y productivos.

Para la primera implementación se recomienda trabajar con **semanas**, debido a que la capacidad de producción de la planta de Metapa está expresada principalmente en moscas por semana.

Sin embargo, esta decisión deberá revisarse cuando se incorporen parámetros biológicos expresados en días.

### 5.9.5 Conversión de unidades temporales

Si un parámetro biológico se encuentra expresado por día y el modelo utiliza semanas, deberá realizarse la conversión correspondiente.

Por ejemplo, una tasa diaria:

$$
\mu_d
$$

podrá convertirse a una tasa semanal mediante una transformación consistente con la definición matemática del parámetro.

No deberán mezclarse directamente parámetros expresados en diferentes unidades temporales.

Por lo tanto, antes de ejecutar una simulación deberá verificarse:

$$
\boxed{
\text{Unidades temporales consistentes}
}
$$

### 5.9.6 Resolución temporal

El método numérico podrá utilizar pasos internos variables para mejorar la precisión de la solución.

Además, se establecerá una malla de tiempos para almacenar los resultados:

$$
t_0,t_1,t_2,\ldots,t_n
$$

En cada instante se almacenarán las variables principales:

$$
M_w(t),F_v(t),F_m(t),M_s(t)
$$

y las variables calculadas:

$$
N_w(t),\rho(t),p_s(t),p_w(t)
$$

Esto permitirá analizar posteriormente la evolución temporal de la población.

### 5.9.7 Liberaciones durante la integración

Las liberaciones de moscas estériles pueden ocurrir en momentos específicos.

Por ejemplo:

$$
t=t_1,t_2,t_3,\ldots
$$

En cada evento se agregará la cantidad correspondiente:

$$
M_s(t^+)=M_s(t^-)+R_t
$$

Por esta razón, la implementación deberá ser capaz de representar eventos discretos dentro de una simulación continua.

En una primera versión, podrá utilizarse una representación por periodos de liberación, por ejemplo semanal.

Posteriormente podrá implementarse una representación con fechas o tiempos específicos si la estrategia lo requiere.

### 5.9.8 Integración de la capacidad de producción

Antes de ejecutar cada liberación deberá comprobarse:

$$
R_t\leq A_t
$$

y:

$$
A_t\leq C_t
$$

por lo que:

$$
R_t\leq C_t
$$

como condición mínima de factibilidad.

Si una estrategia incumple esta condición, el simulador deberá identificarla como no factible bajo el escenario de producción seleccionado.

### 5.9.9 Algoritmo general de simulación

El procedimiento general será:

1. Definir los parámetros del escenario.
2. Definir las condiciones iniciales.
3. Definir la capacidad productiva de Metapa.
4. Definir la estrategia de liberación.
5. Verificar las restricciones de producción.
6. Resolver el sistema de ecuaciones.
7. Incorporar las liberaciones correspondientes.
8. Calcular las variables derivadas.
9. Evaluar los criterios de control y erradicación.
10. Almacenar los resultados.
11. Generar indicadores y gráficas.

De forma conceptual:

```text
Parámetros
    ↓
Condiciones iniciales
    ↓
Escenario de producción
    ↓
Estrategia de liberación
    ↓
Verificación de restricciones
    ↓
Integración numérica
    ↓
Población silvestre + población estéril
    ↓
Criterios de control/erradicación
    ↓
Resultados
```

### 5.9.10 Pseudocódigo

El procedimiento podrá representarse mediante el siguiente pseudocódigo:

```text
INICIO

Cargar parámetros
Cargar condiciones iniciales
Seleccionar escenario de producción
Seleccionar estrategia de liberación

Verificar:
    R(t) <= A(t)
    A(t) <= C(t)

Si no se cumple:
    Marcar estrategia como no factible

Si se cumple:
    Inicializar población

    Para cada periodo de simulación:

        Calcular población silvestre
        Calcular población estéril
        Calcular probabilidad de apareamiento
        Calcular apareamientos
        Calcular descendencia viable
        Calcular mortalidad
        Aplicar liberación correspondiente

        Actualizar estado poblacional

        Calcular:
            Nw
            rho
            ps
            pw

        Evaluar:
            criterio de control
            criterio de erradicación

    Fin del periodo

Calcular:
    TC
    TE
    Rtotal
    UC
    Nwf

Generar resultados

FIN
```

### 5.9.11 Condiciones de no negatividad

La solución numérica deberá respetar las restricciones establecidas anteriormente:

$$
M_w,F_v,F_m,M_s\geq0
$$

Una solución numérica que produzca valores negativos deberá considerarse un problema de implementación, parametrización o formulación del modelo.

No se deberán corregir automáticamente valores negativos sin identificar primero su causa.

### 5.9.12 Manejo de la división entre cero

La relación:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

presenta un problema cuando:

$$
M_w(t)=0
$$

Por lo tanto, el programa deberá manejar explícitamente esta condición.

Una posibilidad será considerar:

$$
\rho(t)=\text{no definido}
$$

cuando:

$$
M_w(t)=0
$$

en lugar de generar una división por cero.

La misma consideración deberá aplicarse a la ecuación de las probabilidades de apareamiento cuando:

$$
M_w(t)+cM_s(t)=0
$$

### 5.9.13 Control de errores numéricos

La implementación deberá verificar que:

* no existan valores `NaN`;
* no existan valores infinitos;
* las poblaciones no sean negativas;
* las probabilidades se encuentren entre 0 y 1;
* las restricciones de producción se cumplan;
* las unidades sean consistentes;
* los parámetros requeridos estén disponibles.

Estas validaciones serán necesarias antes de considerar válida una simulación.

### 5.9.14 Precisión de la solución

La precisión del método numérico dependerá de los parámetros utilizados y de la resolución temporal.

Se deberán evaluar diferentes configuraciones del método para comprobar que pequeñas modificaciones en el paso de integración no produzcan cambios importantes en los resultados.

Esta evaluación permitirá comprobar la estabilidad numérica de la solución.

### 5.9.15 Validación numérica

Antes de utilizar el modelo para comparar estrategias de control, deberá comprobarse que la implementación reproduce correctamente el comportamiento esperado.

Se realizarán pruebas como:

* simulación sin liberación de moscas estériles;
* simulación con liberación;
* simulación con diferentes cantidades de liberación;
* simulación con diferentes capacidades de producción;
* simulación con mortalidad estéril modificada;
* simulación con diferentes condiciones iniciales.

Estas pruebas permitirán detectar errores de implementación y evaluar la sensibilidad del comportamiento del modelo.

### 5.9.16 Escenario sin liberación

Se utilizará un escenario de referencia en el que:

$$
R_t=0
$$

durante toda la simulación.

En este escenario:

$$
M_s(t)=0
$$

si inicialmente:

$$
M_s(0)=0
$$

Este escenario permitirá observar el comportamiento de referencia de la población silvestre sin intervención mediante TIE.

Posteriormente, los resultados de los escenarios con liberación podrán compararse contra esta condición de referencia.

### 5.9.17 Escenarios con liberación

Para evaluar la eficacia de la TIE se podrán definir diferentes estrategias de liberación.

Por ejemplo:

$$
S_1=\{R_1,\Delta t_1,T_1\}
$$

$$
S_2=\{R_2,\Delta t_2,T_2\}
$$

$$
S_3=\{R_3,\Delta t_3,T_3\}
$$

Cada estrategia será evaluada bajo las mismas condiciones iniciales para permitir una comparación adecuada.

Posteriormente se podrán combinar estas estrategias con los escenarios de capacidad:

$$
C_{ini},C_{max},C_{fut}
$$

### 5.9.18 Resultados de la solución numérica

La simulación deberá generar como mínimo:

* evolución de \(M_w(t)\);
* evolución de \(F_v(t)\);
* evolución de \(F_m(t)\);
* evolución de \(M_s(t)\);
* población silvestre \(N_w(t)\);
* relación \(\rho(t)\);
* probabilidad \(p_s(t)\);
* probabilidad \(p_w(t)\);
* cantidad liberada \(R_t\);
* cantidad acumulada \(R_{total}\);
* tiempo de control \(T_C\);
* tiempo de erradicación \(T_E\);
* utilización de capacidad \(U_C\);
* población final \(N_{w,f}\).

Estos resultados constituirán la salida principal del modelo computacional.

### 5.9.19 Implementación inicial en Python

La implementación del modelo se realizará utilizando principalmente:

* **Python** como lenguaje de programación;
* **NumPy** para operaciones numéricas;
* **SciPy** para la integración de ecuaciones diferenciales;
* **Pandas** para organizar los resultados;
* **Matplotlib** para la generación de gráficas.

La implementación deberá mantenerse separada de la documentación y de los datos de entrada.

La estructura prevista será:

```text
src/
├── modelo/
│   └── poblacion.py
│
├── produccion/
│   └── planta.py
│
├── simulacion/
│   └── simulador.py
│
└── escenarios/
    └── escenarios.py
```

### 5.9.20 Principio de separación entre modelo y simulación

El modelo matemático deberá mantenerse separado de la lógica encargada de ejecutar los escenarios.

De esta manera:

```text
Modelo matemático
        ↓
Implementación de ecuaciones
        ↓
Simulador
        ↓
Escenario
        ↓
Resultados
```

Esto permitirá modificar una estrategia de liberación sin tener que modificar las ecuaciones fundamentales del modelo.

### 5.9.21 Consideración sobre la naturaleza preliminar

La implementación numérica descrita en esta sección corresponde a la primera versión del modelo.

Antes de utilizarla para realizar estimaciones finales deberán validarse:

* los parámetros biológicos;
* las tasas de mortalidad;
* la competitividad de los machos estériles;
* las condiciones iniciales;
* la relación entre población de GBG e infestaciones;
* los criterios de control y erradicación;
* la representación temporal;
* la capacidad y disponibilidad de moscas de la planta.

Por lo tanto:

$$
\boxed{
\text{Simulación numérica}
\neq
\text{validación biológica}
}
$$

La correcta ejecución computacional de las ecuaciones no garantiza por sí misma que el modelo represente adecuadamente la dinámica real del GBG.

La validación científica y la calibración de los parámetros serán etapas posteriores del proyecto.

## 5.10 Análisis de escenarios

El análisis de escenarios permitirá evaluar el comportamiento del modelo bajo diferentes condiciones iniciales, capacidades de producción y estrategias de liberación de moscas estériles.

Su finalidad será determinar cómo cambian los resultados de la simulación cuando se modifican los principales factores que intervienen en la dinámica poblacional del gusano barrenador del ganado (GBG).

Los escenarios no representan predicciones definitivas sobre el comportamiento de la población en México. Constituyen configuraciones del modelo que permiten analizar diferentes condiciones posibles y comparar sus resultados.

### 5.10.1 Objetivo del análisis de escenarios

El análisis tendrá como objetivos principales:

* Evaluar diferentes niveles iniciales de población silvestre.
* Comparar diferentes capacidades de producción de la planta de Metapa.
* Evaluar diferentes cantidades de liberación.
* Comparar diferentes frecuencias de liberación.
* Analizar diferentes relaciones entre moscas estériles y silvestres.
* Determinar el tiempo necesario para alcanzar los criterios de control y erradicación.
* Determinar la cantidad total de moscas estériles requeridas.
* Identificar estrategias que sean factibles bajo la capacidad productiva considerada.

### 5.10.2 Estructura general de un escenario

Cada escenario estará definido mediante un conjunto de parámetros:

$$
\boxed{
S=
\{X_0,\theta,C_t,R_t,\Delta t_R,T_R,T_{sim}\}
}
$$

donde:

* \(X_0\) = condiciones iniciales;
* \(\theta\) = parámetros biológicos y epidemiológicos;
* \(C_t\) = capacidad de producción;
* \(R_t\) = estrategia de liberación;
* \(\Delta t_R\) = frecuencia o intervalo de liberación;
* \(T_R\) = duración de las liberaciones;
* \(T_{sim}\) = duración de la simulación.

Cada combinación de estos elementos podrá generar un escenario diferente.

### 5.10.3 Escenario de referencia sin TIE

Se establecerá un escenario de referencia en el que no se realicen liberaciones de moscas estériles:

$$
R_t=0
$$

durante todo el periodo de simulación.

Si:

$$
M_s(0)=0
$$

entonces:

$$
M_s(t)=0
$$

durante la simulación.

Este escenario permitirá observar el comportamiento de la población sin intervención y servirá como referencia para comparar los escenarios que incorporen la TIE.

Se identificará como:

$$
\boxed{S_0=\text{Escenario sin liberación}}
$$

### 5.10.4 Escenarios de capacidad productiva

Se considerarán inicialmente tres escenarios asociados con la capacidad de producción de la planta de Metapa:

| Escenario          |           Capacidad |
| ------------------ | ------------------: |
| \(C_1\) Inicial    |  28 millones/semana |
| \(C_2\) Proyectado | 100 millones/semana |
| \(C_3\) Futuro     | 120 millones/semana |

El escenario de 28 millones de moscas por semana representará la capacidad inicial considerada.

El escenario de 100 millones de moscas por semana representará la capacidad proyectada.

El escenario de 120 millones de moscas por semana será considerado únicamente como escenario futuro.

No se deberá interpretar el escenario futuro como capacidad actual confirmada de la planta.

### 5.10.5 Escenarios de población inicial

Debido a que la población inicial real de GBG para una escala determinada puede presentar incertidumbre, se utilizarán diferentes condiciones iniciales.

Conceptualmente:

$$
N_{w,0}^{bajo}
$$

$$
N_{w,0}^{medio}
$$

$$
N_{w,0}^{alto}
$$

Estos escenarios permitirán evaluar la sensibilidad de los resultados ante diferentes tamaños iniciales de población.

Los valores definitivos deberán ser establecidos posteriormente mediante información científica o epidemiológica.

No se deberán seleccionar valores únicamente para producir un determinado resultado de erradicación.

### 5.10.6 Escenarios de intensidad de liberación

La cantidad de moscas estériles liberadas podrá variar entre escenarios.

Se podrán definir estrategias como:

$$
R_1<R_2<R_3
$$

donde:

* \(R_1\) = liberación baja;
* \(R_2\) = liberación intermedia;
* \(R_3\) = liberación alta.

Los valores serán configurables y deberán respetar:

$$
R_t\leq C_t
$$

para que la estrategia sea factible.

### 5.10.7 Escenarios de frecuencia de liberación

Además de modificar la cantidad liberada, se podrá modificar la frecuencia.

Por ejemplo:

* liberación semanal;
* liberación cada determinado número de días;
* liberación con intervalos variables.

La frecuencia estará representada mediante:

$$
\Delta t_R
$$

Una estrategia podrá entonces definirse como:

$$
S_R=\{R_t,\Delta t_R,T_R\}
$$

Esto permitirá analizar si una cantidad determinada de moscas produce mejores resultados cuando se distribuye de manera constante o mediante diferentes frecuencias.

### 5.10.8 Escenarios de relación estéril:silvestre

También se podrá evaluar la relación:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

como indicador de la intensidad de la TIE.

Como referencia operacional se podrá evaluar:

$$
\rho_{ref}=10:1
$$

sin asumir que este valor constituye una constante biológica universal.

También podrán evaluarse otras relaciones cuando exista evidencia científica suficiente para justificarlas.

### 5.10.9 Escenarios combinados

El análisis principal no se limitará a modificar un solo parámetro.

Se podrán combinar diferentes condiciones.

Por ejemplo:

| Escenario | Población inicial | Capacidad    | Estrategia       |
| --------- | ----------------- | ------------ | ---------------- |
| S1        | Baja              | 28 M/semana  | Liberación baja  |
| S2        | Media             | 28 M/semana  | Liberación media |
| S3        | Alta              | 28 M/semana  | Liberación alta  |
| S4        | Baja              | 100 M/semana | Liberación baja  |
| S5        | Media             | 100 M/semana | Liberación media |
| S6        | Alta              | 100 M/semana | Liberación alta  |
| S7        | Baja              | 120 M/semana | Liberación alta  |
| S8        | Media             | 120 M/semana | Liberación alta  |
| S9        | Alta              | 120 M/semana | Liberación alta  |

Esta tabla representa una estructura inicial de comparación y no constituye todavía el conjunto definitivo de escenarios.

### 5.10.10 Comparación de escenarios

Cada escenario será evaluado mediante un conjunto común de indicadores.

Los principales serán:

$$
T_C
$$

$$
T_E
$$

$$
R_{total}
$$

$$
U_C
$$

$$
N_{w,f}
$$

y, cuando corresponda:

$$
N_{w,min}
$$

donde \(N_{w,min}\) representa el menor tamaño de población alcanzado durante la simulación.

Esto permitirá comparar los resultados bajo condiciones equivalentes.

### 5.10.11 Tiempo de control

Para cada escenario se calculará:

$$
T_C=\min\{t:N_w(t)\leq N_C\}
$$

El resultado permitirá identificar qué estrategias alcanzan más rápidamente el criterio de control.

Si el criterio no se alcanza durante la simulación:

$$
T_C>T_{sim}
$$

o se marcará como:

**No alcanzado**.

### 5.10.12 Tiempo de erradicación

Para cada escenario se calculará:

$$
T_E=\min\{t:N_w(t)\leq N_E\}
$$

El tiempo obtenido permitirá comparar la rapidez con la que cada estrategia alcanza el criterio de erradicación definido.

Al igual que en el caso del control, si el criterio no se alcanza:

$$
T_E>T_{sim}
$$

o se registrará como:

**No alcanzado**.

### 5.10.13 Cantidad total liberada

Se calculará:

$$
R_{total}=\sum_{t=1}^{n}R_t
$$

Este indicador permitirá determinar cuántas moscas estériles fueron utilizadas para alcanzar el resultado obtenido.

Una estrategia que alcance el criterio de erradicación con un menor \(R_{total}\) podrá considerarse más eficiente en términos de cantidad utilizada, siempre que también cumpla los demás criterios de factibilidad.

### 5.10.14 Utilización de la capacidad de Metapa

Para cada escenario se calculará:

$$
U_C=
\frac{\sum R_t}{\sum C_t}
$$

Este indicador permitirá determinar qué proporción de la capacidad disponible fue utilizada.

También se calculará, cuando sea necesario:

$$
U_{C,t}=\frac{R_t}{C_t}
$$

para identificar periodos en los que la demanda de liberación se encuentre cercana a la capacidad máxima disponible.

### 5.10.15 Factibilidad de los escenarios

Cada escenario deberá cumplir:

$$
R_t\leq A_t\leq C_t
$$

durante todo el periodo de simulación.

Si:

$$
R_t>C_t
$$

en cualquier periodo, el escenario será marcado como:

$$
\boxed{\text{No factible}}
$$

No se permitirá aumentar artificialmente \(C_t\) para hacer que una estrategia sea factible.

### 5.10.16 Escenarios que no alcanzan el criterio

Un escenario puede ser matemáticamente válido y, al mismo tiempo, no alcanzar el criterio de control o erradicación.

Por ejemplo:

$$
N_w(t)>N_E
$$

durante toda la simulación.

En este caso, el resultado no deberá interpretarse como un error.

Representará que, bajo las condiciones seleccionadas, la estrategia no fue suficiente para alcanzar el criterio establecido.

### 5.10.17 Escenarios con recuperación poblacional

También deberán identificarse escenarios en los que la población inicialmente disminuya pero posteriormente aumente.

Por ejemplo:

$$
N_w(t_1)\leq N_E
$$

pero posteriormente:

$$
N_w(t_2)>N_E
$$

con:

$$
t_2>t_1
$$

Este comportamiento indicará que la reducción obtenida no fue sostenida.

Estos casos serán importantes para evitar considerar como exitosas estrategias que únicamente producen una disminución temporal.

### 5.10.18 Análisis de sensibilidad

Además de comparar escenarios, se realizará un análisis de sensibilidad sobre los parámetros que puedan tener mayor influencia en los resultados.

Entre ellos podrán encontrarse:

* población inicial;
* mortalidad de machos silvestres;
* mortalidad de hembras;
* mortalidad de machos estériles;
* competitividad de machos estériles;
* tasa reproductiva;
* cantidad de liberación;
* frecuencia de liberación;
* capacidad de producción.

El análisis permitirá determinar cuáles parámetros producen mayores cambios en:

$$
T_E
$$

$$
R_{total}
$$

y:

$$
N_{w,f}
$$

### 5.10.19 Escenarios de incertidumbre

Cuando un parámetro no pueda determinarse mediante un valor único confiable, se podrá utilizar un intervalo:

$$
\theta\in[\theta_{min},\theta_{max}]
$$

Esto permitirá evaluar cómo cambia el resultado ante diferentes valores plausibles.

Esta metodología será especialmente importante para parámetros que todavía se encuentren pendientes de validación.

### 5.10.20 Priorización de escenarios

Los escenarios deberán priorizarse de acuerdo con la disponibilidad y calidad de la información.

Se seguirá el siguiente orden:

1. Datos oficiales de la planta de Metapa.
2. Datos científicos publicados.
3. Parámetros provenientes de modelos científicos previamente publicados.
4. Estimaciones epidemiológicas justificadas.
5. Rangos de incertidumbre.
6. Escenarios hipotéticos claramente identificados.

Los escenarios hipotéticos no deberán presentarse como datos observados.

### 5.10.21 Matriz general de escenarios

La estructura general para el análisis será:

| Dimensión                | Variable       |
| ------------------------ | -------------- |
| Población inicial        | \(X_0\)        |
| Capacidad productiva     | \(C_t\)        |
| Disponibilidad           | \(A_t\)        |
| Cantidad liberada        | \(R_t\)        |
| Frecuencia               | \(\Delta t_R\) |
| Duración                 | \(T_R\)        |
| Competitividad estéril   | \(c\)          |
| Mortalidad estéril       | \(\mu_s\)      |
| Duración de simulación   | \(T_{sim}\)    |
| Criterio de control      | \(N_C\)        |
| Criterio de erradicación | \(N_E\)        |

Esta matriz permitirá construir posteriormente configuraciones de escenarios en Python.

### 5.10.22 Identificación de escenarios

Cada escenario recibirá un identificador único.

Por ejemplo:

```text
S01
S02
S03
...
```

El identificador permitirá relacionar:

$$
\text{Escenario}
\rightarrow
\text{Parámetros}
\rightarrow
\text{Simulación}
\rightarrow
\text{Resultados}
$$

Esto facilitará la trazabilidad de los experimentos computacionales.

### 5.10.23 Resultados esperados del análisis

El análisis de escenarios deberá permitir determinar:

* qué estrategias son factibles;
* qué estrategias alcanzan el control;
* qué estrategias alcanzan el criterio de erradicación;
* cuánto tiempo requiere cada estrategia;
* cuántas moscas estériles necesita;
* qué porcentaje de la capacidad de Metapa utiliza;
* cómo cambia el resultado ante diferentes poblaciones iniciales;
* qué parámetros tienen mayor influencia sobre los resultados.

### 5.10.24 Principio de comparación

Para comparar correctamente dos estrategias, ambas deberán evaluarse bajo condiciones equivalentes, excepto por los parámetros que se desean comparar.

Por ejemplo, para estudiar el efecto de modificar la cantidad liberada, deberán mantenerse constantes:

$$
X_0,\theta,C_t,\Delta t_R,T_{sim}
$$

y modificar únicamente:

$$
R_t
$$

Esto permitirá atribuir las diferencias observadas al factor que se está evaluando.

### 5.10.25 Resultado final del análisis

El análisis de escenarios constituirá la base para identificar estrategias potencialmente viables para el control del GBG mediante TIE.

Los resultados no deberán utilizarse para afirmar que una estrategia será necesariamente efectiva en condiciones reales.

Su función será proporcionar evidencia cuantitativa obtenida mediante el modelo para posteriormente seleccionar y comparar estrategias de producción y liberación.

La interpretación final deberá considerar la incertidumbre de los parámetros, la calidad de los datos y la validación del modelo.

## 5.11 Análisis de sensibilidad e incertidumbre

El modelo matemático del GBG contiene parámetros que pueden presentar incertidumbre debido a la variabilidad biológica, las condiciones ambientales, las diferencias entre poblaciones y la disponibilidad limitada de información específica para México.

Por esta razón, los resultados de las simulaciones no deberán interpretarse únicamente a partir de un conjunto fijo de parámetros.

El análisis de sensibilidad permitirá determinar qué parámetros tienen mayor influencia sobre los resultados del modelo, mientras que el análisis de incertidumbre permitirá evaluar cómo cambia el resultado cuando los parámetros presentan diferentes valores posibles.

### 5.11.1 Objetivo del análisis de sensibilidad

El objetivo principal será identificar los parámetros cuya modificación produzca cambios importantes en los resultados de la simulación.

Entre los principales resultados a evaluar se encuentran:

$$
T_C
$$

$$
T_E
$$

$$
R_{total}
$$

$$
N_{w,f}
$$

y:

$$
U_C
$$

Esto permitirá determinar qué parámetros requieren mayor precisión y cuáles tienen menor influencia sobre el comportamiento general del modelo.

### 5.11.2 Parámetros sujetos a análisis

Inicialmente podrán considerarse los siguientes parámetros:

| Parámetro                          | Símbolo        | Posible influencia |
| ---------------------------------- | -------------- | ------------------ |
| Tasa reproductiva                  | \(b\)          | Alta               |
| Tasa de apareamiento               | \(a\)          | Alta               |
| Mortalidad de machos silvestres    | \(\mu_M\)      | Alta               |
| Mortalidad de hembras              | \(\mu_F\)      | Alta               |
| Mortalidad de machos estériles     | \(\mu_s\)      | Alta               |
| Competitividad de machos estériles | \(c\)          | Alta               |
| Población inicial                  | \(N_w(0)\)     | Alta               |
| Cantidad liberada                  | \(R_t\)        | Alta               |
| Frecuencia de liberación           | \(\Delta t_R\) | Media/Alta         |
| Capacidad de producción            | \(C_t\)        | Alta               |
| Umbral de control                  | \(N_C\)        | Media              |
| Umbral de erradicación             | \(N_E\)        | Media              |

La clasificación de influencia será inicialmente orientativa y deberá comprobarse mediante las simulaciones.

### 5.11.3 Parámetros con incertidumbre

Cuando un parámetro no pueda establecerse mediante un único valor confiable, se representará mediante un intervalo:

$$
\theta\in[\theta_{min},\theta_{max}]
$$

donde:

* \(\theta\) = parámetro;
* \(\theta_{min}\) = valor mínimo considerado;
* \(\theta_{max}\) = valor máximo considerado.

Esto permitirá representar la variabilidad o incertidumbre existente.

No se deberán establecer intervalos sin una fuente o justificación metodológica.

### 5.11.4 Fuentes de incertidumbre

La incertidumbre de los parámetros podrá originarse por diferentes causas:

* variabilidad biológica del GBG;
* diferencias entre poblaciones;
* condiciones ambientales;
* diferencias entre hospedadores;
* escala geográfica del modelo;
* limitaciones de los estudios disponibles;
* diferencias metodológicas entre investigaciones;
* falta de información específica para México;
* incertidumbre sobre la población inicial;
* incertidumbre sobre la competitividad de los machos estériles.

Estas fuentes deberán documentarse para cada parámetro.

### 5.11.5 Sensibilidad de un parámetro

De manera conceptual, un parámetro será considerado sensible cuando una modificación relativamente pequeña en su valor produzca un cambio importante en alguno de los resultados del modelo.

Por ejemplo:

$$
\theta\rightarrow\theta'
$$

y:

$$
T_E\rightarrow T_E'
$$

Si:

$$
|T_E'-T_E|
$$

es considerable respecto al cambio aplicado en \(\theta\), entonces el resultado presenta sensibilidad respecto a dicho parámetro.

### 5.11.6 Análisis de sensibilidad univariado

La primera metodología será el análisis de sensibilidad univariado.

En este procedimiento se modificará un solo parámetro mientras los demás permanecen constantes.

Conceptualmente:

$$
\theta_i\rightarrow
\{\theta_{i1},\theta_{i2},\theta_{i3},...\}
$$

manteniendo:

$$
\theta_j=\text{constante}
$$

para:

$$
j\neq i
$$

Esto permitirá observar directamente el efecto individual de cada parámetro.

### 5.11.7 Ejemplo de sensibilidad de la mortalidad estéril

Para estudiar el efecto de la mortalidad de machos estériles se podrá evaluar:

$$
\mu_s^{(1)}
$$

$$
\mu_s^{(2)}
$$

$$
\mu_s^{(3)}
$$

manteniendo constantes los demás parámetros.

Posteriormente se compararán:

$$
T_E
$$

$$
R_{total}
$$

y:

$$
N_{w,f}
$$

para cada valor.

Esto permitirá determinar si la supervivencia de los machos estériles tiene una influencia significativa sobre la estrategia de control.

### 5.11.8 Sensibilidad de la competitividad estéril

El parámetro:

$$
c
$$

representa la competitividad relativa de los machos estériles.

Debido a que interviene directamente en:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

su valor puede tener una influencia importante sobre el resultado de la TIE.

Por ello, deberá evaluarse cómo cambian los resultados cuando:

$$
c
$$

adopta diferentes valores dentro del intervalo considerado científicamente plausible.

### 5.11.9 Sensibilidad de la población inicial

La población inicial:

$$
N_w(0)
$$

puede tener una influencia considerable sobre el tiempo necesario para alcanzar el criterio de control o erradicación.

Se podrán comparar escenarios:

$$
N_{w,0}^{bajo}
$$

$$
N_{w,0}^{medio}
$$

$$
N_{w,0}^{alto}
$$

y analizar su efecto sobre:

$$
T_E
$$

y:

$$
R_{total}
$$

Esto permitirá determinar si una incertidumbre en la población inicial genera grandes diferencias en las estimaciones finales.

### 5.11.10 Sensibilidad de la cantidad de liberación

La cantidad de moscas liberadas:

$$
R_t
$$

será uno de los principales factores de análisis.

Se podrán comparar diferentes niveles:

$$
R_1<R_2<R_3
$$

y evaluar cómo cambia:

$$
N_w(t)
$$

y:

$$
T_E
$$

Esto permitirá identificar si incrementar la cantidad de moscas liberadas produce una reducción significativa del tiempo necesario para alcanzar el criterio establecido.

### 5.11.11 Sensibilidad de la frecuencia de liberación

También se evaluará:

$$
\Delta t_R
$$

para determinar el efecto de diferentes frecuencias de liberación.

Dos estrategias podrán utilizar una cantidad total similar de moscas pero distribuirlas de manera diferente en el tiempo.

Por ejemplo:

$$
S_1=\text{liberación frecuente}
$$

y:

$$
S_2=\text{liberación menos frecuente}
$$

La comparación permitirá determinar si la distribución temporal de las liberaciones afecta el resultado.

### 5.11.12 Sensibilidad de la capacidad de producción

La capacidad de la planta se analizará mediante los escenarios:

$$
C_{ini}=28\,000\,000
$$

$$
C_{max}=100\,000\,000
$$

y:

$$
C_{fut}=120\,000\,000
$$

moscas por semana.

El objetivo será determinar cómo cambia la factibilidad de las estrategias cuando aumenta la capacidad disponible.

Esto permitirá identificar estrategias que:

* son factibles con 28 millones por semana;
* requieren una capacidad mayor;
* solo son factibles bajo escenarios futuros.

### 5.11.13 Sensibilidad de los criterios de control

Los resultados también podrán depender de los valores establecidos para:

$$
N_C
$$

y:

$$
N_E
$$

Por ello, una vez que existan valores científicamente justificables, se podrá evaluar cómo cambia:

$$
T_C
$$

y:

$$
T_E
$$

cuando se modifica el criterio utilizado.

Esto evitará interpretar un único tiempo de erradicación como un valor absoluto cuando el criterio utilizado todavía presenta incertidumbre.

### 5.11.14 Indicador de sensibilidad

Como indicador básico podrá utilizarse la variación relativa del resultado.

Para un resultado \(Y\) y un parámetro \(\theta\):

$$
S_{\theta}^{Y}
=
\frac{\Delta Y/Y}{\Delta\theta/\theta}
$$

donde:

* \(S_{\theta}^{Y}\) = sensibilidad relativa;
* \(\Delta Y\) = cambio en el resultado;
* \(Y\) = resultado de referencia;
* \(\Delta\theta\) = cambio en el parámetro;
* \(\theta\) = valor de referencia.

Este indicador permitirá comparar la influencia relativa de parámetros expresados en diferentes unidades.

### 5.11.15 Interpretación del índice de sensibilidad

De manera general:

$$
|S_{\theta}^{Y}|>1
$$

indica que el resultado presenta una variación proporcionalmente mayor que el cambio aplicado al parámetro.

Mientras que:

$$
|S_{\theta}^{Y}|<1
$$

indica una respuesta proporcionalmente menor.

La interpretación definitiva dependerá del resultado analizado y del intervalo utilizado.

### 5.11.16 Análisis de incertidumbre

El análisis de incertidumbre evaluará múltiples combinaciones posibles de los parámetros que presenten rangos de valores.

En lugar de utilizar únicamente:

$$
\theta=\theta_0
$$

se considerará:

$$
\theta\in[\theta_{min},\theta_{max}]
$$

para los parámetros que correspondan.

El resultado será un conjunto de posibles valores de salida:

$$
T_E\in[T_{E,min},T_{E,max}]
$$

$$
R_{total}\in[R_{min},R_{max}]
$$

en lugar de un único valor.

### 5.11.17 Simulación de múltiples combinaciones

Posteriormente podrá implementarse un procedimiento de simulación repetida.

De manera conceptual:

```text
Definir rangos de parámetros

Para cada combinación:

    Cargar parámetros
    Ejecutar modelo
    Guardar resultados

Fin

Analizar distribución de resultados
```

Esto permitirá evaluar cómo la incertidumbre de entrada se propaga hacia los resultados del modelo.

### 5.11.18 Distribuciones de probabilidad

Cuando exista suficiente evidencia para establecer una distribución estadística de un parámetro, podrá utilizarse una distribución de probabilidad.

Por ejemplo:

$$
\theta\sim D
$$

donde \(D\) representa una distribución respaldada por información científica.

No se deberá asignar una distribución de probabilidad únicamente por conveniencia matemática.

Cuando no exista información suficiente, será preferible utilizar rangos o escenarios claramente definidos.

### 5.11.19 Simulación Monte Carlo

Como metodología posterior, podrá utilizarse una simulación Monte Carlo.

En este procedimiento se generarían múltiples combinaciones aleatorias de parámetros dentro de las distribuciones o rangos establecidos.

Conceptualmente:

$$
\theta^{(1)},\theta^{(2)},...,\theta^{(n)}
$$

y para cada combinación:

$$
X^{(i)}(t)
$$

se ejecutaría una simulación.

Los resultados podrían producir distribuciones de:

$$
T_E
$$

$$
R_{total}
$$

$$
N_{w,f}
$$

y:

$$
U_C
$$

Esta metodología no será necesaria para la primera versión funcional del modelo, pero podrá incorporarse posteriormente.

### 5.11.20 Priorización de parámetros

Los parámetros podrán clasificarse en tres grupos:

| Clasificación      | Descripción                                   |
| ------------------ | --------------------------------------------- |
| Alta sensibilidad  | Produce cambios importantes en los resultados |
| Sensibilidad media | Produce cambios moderados                     |
| Baja sensibilidad  | Produce cambios pequeños                      |

Esta clasificación permitirá identificar los parámetros que requieren mayor atención durante la etapa de búsqueda y validación de información.

### 5.11.21 Uso de los resultados de sensibilidad

Los resultados del análisis permitirán:

1. Identificar parámetros críticos.
2. Priorizar la búsqueda de información científica.
3. Identificar variables que requieren mejor estimación.
4. Evaluar la robustez de las estrategias.
5. Identificar escenarios en los que las conclusiones cambian.
6. Estimar la incertidumbre de los tiempos de control y erradicación.

### 5.11.22 Robustez de una estrategia

Una estrategia podrá considerarse más robusta cuando mantenga un comportamiento favorable bajo diferentes valores plausibles de los parámetros.

Por ejemplo, una estrategia será considerada más robusta si alcanza el criterio de control en una amplia proporción de los escenarios evaluados.

Por el contrario, una estrategia será considerada sensible si pequeñas modificaciones en los parámetros provocan que deje de alcanzar el criterio.

### 5.11.23 Relación entre sensibilidad y toma de decisiones

El análisis de sensibilidad no determinará por sí mismo cuál estrategia deberá utilizarse.

Su función será mostrar qué tan dependientes son los resultados de determinados parámetros.

Por ejemplo:

$$
\text{Estrategia A}
$$

puede presentar un menor:

$$
T_E
$$

que:

$$
\text{Estrategia B}
$$

bajo los valores centrales.

Sin embargo, si pequeñas variaciones en \(c\) hacen que la estrategia A deje de alcanzar el criterio, mientras B mantiene resultados similares, B podría presentar mayor robustez.

Por lo tanto, la comparación deberá considerar tanto el resultado central como su sensibilidad.

### 5.11.24 Registro de los análisis

Cada análisis deberá conservar:

* identificador del escenario;
* parámetros utilizados;
* valores modificados;
* condiciones iniciales;
* capacidad de producción;
* estrategia de liberación;
* resultados;
* fecha de ejecución;
* versión del modelo.

Esto permitirá reproducir posteriormente los experimentos computacionales.

### 5.11.25 Principio de no ocultar incertidumbre

Los resultados del modelo no deberán presentarse como valores exactos cuando los parámetros de entrada presenten incertidumbre significativa.

Por ejemplo, si diferentes valores plausibles producen:

$$
T_E=40,\ 55,\ 70\text{ semanas}
$$

no deberá reportarse únicamente:

$$
T_E=55\text{ semanas}
$$

sin indicar la variabilidad observada.

La incertidumbre deberá formar parte de la interpretación de los resultados.

### 5.11.26 Relación con la validación

El análisis de sensibilidad e incertidumbre estará relacionado con la etapa de validación del modelo.

Los parámetros identificados como altamente sensibles deberán recibir prioridad durante:

* revisión bibliográfica;
* selección de fuentes;
* calibración;
* validación;
* análisis de escenarios.

De esta manera:

$$
\boxed{
\text{Sensibilidad}
\rightarrow
\text{Priorización de parámetros}
\rightarrow
\text{Mejor información}
\rightarrow
\text{Modelo más robusto}
}
$$

### 5.11.27 Consideración para la primera implementación

La primera versión del modelo utilizará principalmente análisis de sensibilidad univariado.

El procedimiento inicial será:

1. Seleccionar un parámetro.
2. Definir un rango científicamente justificable.
3. Mantener constantes los demás parámetros.
4. Ejecutar la simulación para diferentes valores.
5. Registrar los resultados.
6. Comparar los cambios obtenidos.
7. Identificar la sensibilidad del resultado.

Una vez validado este procedimiento, podrán incorporarse métodos más avanzados como simulaciones Monte Carlo.

### 5.11.28 Resultado esperado

El análisis de sensibilidad e incertidumbre permitirá determinar no solamente cuánto tiempo podría requerir una estrategia, sino también qué tan confiable es esa estimación frente a las incertidumbres presentes en los parámetros.

Por lo tanto, el modelo deberá proporcionar resultados acompañados de su contexto de incertidumbre cuando la información disponible así lo requiera.

El objetivo será evitar que una estimación obtenida bajo un único conjunto de parámetros sea interpretada como una predicción exacta del comportamiento real del GBG en México.

## 5.12 Validación del modelo matemático

La validación del modelo tendrá como finalidad determinar si la formulación matemática y su implementación computacional representan de manera suficientemente adecuada la dinámica poblacional del gusano barrenador del ganado (GBG) y el efecto esperado de la liberación de machos estériles.

La validación se realizará de manera progresiva, comenzando con la comprobación matemática y computacional del modelo y avanzando posteriormente hacia la comparación con información científica y datos disponibles.

La validación no implicará demostrar que el modelo reproduce exactamente todas las condiciones reales del GBG, sino determinar si es suficientemente consistente para los objetivos definidos dentro del alcance del proyecto.

### 5.12.1 Objetivos de la validación

La validación tendrá como objetivos:

* comprobar que las ecuaciones fueron implementadas correctamente;
* verificar que las variables mantengan las unidades correspondientes;
* comprobar que las restricciones del modelo se cumplan;
* verificar que las poblaciones no adopten valores imposibles;
* comprobar el comportamiento del modelo en escenarios conocidos;
* comparar los resultados con información científica disponible;
* identificar parámetros o componentes que requieran ajustes;
* determinar las limitaciones del modelo.

### 5.12.2 Niveles de validación

La validación se dividirá en diferentes niveles:

1. Validación matemática.
2. Validación computacional.
3. Validación biológica.
4. Validación mediante literatura científica.
5. Validación de escenarios.
6. Validación de sensibilidad.

Cada nivel tendrá un propósito diferente.

### 5.12.3 Validación matemática

La primera etapa consistirá en revisar que las ecuaciones implementadas correspondan con la formulación documentada.

Se verificará que:

$$
\frac{dX}{dt}=F(X,\theta,u)
$$

esté correctamente representado en el código.

Se comprobará específicamente la implementación de:

$$
\frac{dM_w}{dt}
$$

$$
\frac{dF_v}{dt}
$$

$$
\frac{dF_m}{dt}
$$

$$
\frac{dM_s}{dt}
$$

así como las ecuaciones auxiliares:

$$
p_s(t)
$$

$$
p_w(t)
$$

$$
A_w(t)
$$

$$
A_s(t)
$$

y:

$$
B_v(t)
$$

### 5.12.4 Validación dimensional

Todas las ecuaciones deberán presentar consistencia dimensional.

Por ejemplo, si:

$$
\frac{dM_w}{dt}
$$

representa una variación de individuos por unidad de tiempo, todos los términos de la ecuación deberán tener las mismas unidades.

Para:

$$
\frac{dM_w}{dt}=r_MB_v-\mu_MM_w
$$

deberá cumplirse que:

$$
[r_MB_v]=[\mu_MM_w]
$$

y ambos términos deberán corresponder a:

$$
\text{individuos}/\text{unidad de tiempo}
$$

La comprobación dimensional será obligatoria antes de utilizar el modelo para generar resultados finales.

### 5.12.5 Validación de restricciones

La implementación deberá verificar automáticamente las restricciones definidas en la sección 5.6.

Entre ellas:

$$
M_w,F_v,F_m,M_s\geq0
$$

$$
R_t\leq A_t\leq C_t
$$

$$
0\leq p_s,p_w\leq1
$$

y:

$$
p_s+p_w=1
$$

También deberá verificarse:

$$
N_w(t)\geq0
$$

durante toda la simulación.

### 5.12.6 Validación de la población sin intervención

Se ejecutará una simulación sin liberación de moscas estériles:

$$
R_t=0
$$

Este escenario permitirá comprobar el comportamiento natural representado por el modelo.

Se analizará:

$$
N_w(t)
$$

durante todo el periodo de simulación.

El resultado deberá ser biológicamente interpretable de acuerdo con los parámetros utilizados.

### 5.12.7 Validación del efecto de la TIE

Posteriormente se incorporarán liberaciones:

$$
R_t>0
$$

y se comparará el comportamiento con el escenario sin intervención.

Se espera que, bajo condiciones en las que la TIE sea suficientemente efectiva, la liberación de machos estériles produzca una reducción en la reproducción efectiva y, consecuentemente, en la población silvestre.

El modelo no deberá asumir automáticamente que cualquier liberación produce erradicación.

El resultado dependerá de los parámetros y de las condiciones iniciales.

### 5.12.8 Prueba de aumento de liberación

Se realizará una prueba en la que se incremente la cantidad de moscas liberadas.

Por ejemplo:

$$
R_1<R_2<R_3
$$

manteniendo constantes los demás parámetros.

Se compararán:

$$
N_w(t)
$$

y:

$$
T_E
$$

para las diferentes estrategias.

Esta prueba permitirá comprobar si el modelo responde de manera coherente ante cambios en la intensidad de la intervención.

### 5.12.9 Prueba de reducción de liberación

También se realizará el procedimiento inverso.

Se reducirá progresivamente:

$$
R_t
$$

para determinar si existe un punto a partir del cual la estrategia deja de alcanzar el criterio de control o erradicación.

Esto permitirá identificar regiones de comportamiento en las que la cantidad liberada sea insuficiente.

### 5.12.10 Validación de la capacidad de producción

Se verificará que el modelo respete las capacidades consideradas para la planta de Metapa:

$$
C_{ini}=28\,000\,000
$$

$$
C_{max}=100\,000\,000
$$

y:

$$
C_{fut}=120\,000\,000
$$

moscas por semana.

Una estrategia que requiera:

$$
R_t>C_t
$$

deberá ser identificada como no factible.

El modelo no deberá aumentar automáticamente la producción para satisfacer una estrategia que exceda la capacidad seleccionada.

### 5.12.11 Validación de las liberaciones

Se comprobará que cada liberación produzca el incremento correspondiente en la población estéril.

Para una liberación discreta:

$$
M_s(t^+)=M_s(t^-)+R_t
$$

Por lo tanto, inmediatamente después del evento deberá observarse el incremento correspondiente.

Posteriormente, la población estéril deberá disminuir de acuerdo con la mortalidad:

$$
\frac{dM_s}{dt}=R(t)-\mu_sM_s(t)
$$

cuando no exista una nueva liberación.

### 5.12.12 Validación de la competencia reproductiva

Se verificará el comportamiento de:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

Cuando:

$$
M_s(t)=0
$$

deberá cumplirse:

$$
p_s(t)=0
$$

y:

$$
p_w(t)=1
$$

si existe una población de machos silvestres.

Cuando aumente la cantidad de machos estériles, la probabilidad de apareamiento con machos estériles deberá aumentar bajo la formulación utilizada.

### 5.12.13 Casos límite

El modelo deberá probarse mediante casos límite.

Entre ellos:

#### Sin población silvestre

Si:

$$
M_w=F_v=F_m=0
$$

no deberá producirse una división por cero ni generarse una población silvestre artificial.

#### Sin machos estériles

Si:

$$
M_s=0
$$

deberá cumplirse:

$$
p_s=0
$$

#### Sin liberación

Si:

$$
R_t=0
$$

no deberán incorporarse nuevos machos estériles.

#### Capacidad cero

Si:

$$
C_t=0
$$

entonces una estrategia que requiera:

$$
R_t>0
$$

deberá ser identificada como no factible.

Estos casos permitirán detectar errores de programación y problemas de formulación.

### 5.12.14 Comparación con información científica

Cuando existan datos publicados sobre parámetros o comportamientos del GBG, se utilizarán como referencia para evaluar el comportamiento del modelo.

La comparación podrá realizarse mediante:

* duración de etapas;
* tasas de supervivencia;
* tasas reproductivas;
* mortalidad;
* comportamiento de la TIE;
* respuesta a diferentes niveles de liberación.

La comparación deberá considerar que los estudios pueden corresponder a diferentes condiciones ambientales o poblaciones.

Por lo tanto, una diferencia respecto a un estudio publicado no implicará automáticamente que el modelo sea incorrecto.

### 5.12.15 Validación de comportamiento

Además de comparar valores individuales, se evaluará el comportamiento general del modelo.

Se analizará si:

* la población responde a los cambios de los parámetros;
* la liberación de machos estériles modifica la reproducción;
* una mayor presión de TIE puede generar una mayor reducción poblacional bajo los supuestos establecidos;
* la mortalidad de machos estériles afecta su permanencia;
* la capacidad de producción limita las estrategias;
* una población inicial mayor requiere, en general, un mayor esfuerzo de control.

Estas relaciones serán evaluadas como propiedades del modelo y no como reglas universales.

### 5.12.16 Validación de la estabilidad numérica

Se realizarán simulaciones utilizando diferentes configuraciones del método numérico.

Se comprobará que pequeños cambios en la resolución o en el paso de integración no produzcan variaciones desproporcionadas en los resultados.

Conceptualmente:

$$
\Delta t_1\rightarrow\Delta t_2
$$

y se compararán:

$$
T_E^{(1)}
$$

con:

$$
T_E^{(2)}
$$

así como otros indicadores principales.

Si los resultados presentan diferencias excesivas, deberá revisarse la configuración numérica o la formulación del modelo.

### 5.12.17 Validación mediante escenarios

Cada escenario deberá pasar por las pruebas básicas de validación antes de ser utilizado en comparaciones.

Se comprobará:

* condiciones iniciales;
* parámetros;
* capacidad de producción;
* estrategia de liberación;
* restricciones;
* solución numérica;
* criterios de control;
* criterios de erradicación.

Esto permitirá reducir el riesgo de interpretar como resultados biológicos errores derivados de una configuración incorrecta del escenario.

### 5.12.18 Validación de resultados

Los resultados generados deberán conservar una relación trazable:

$$
\boxed{
\text{Datos}
\rightarrow
\text{Parámetros}
\rightarrow
\text{Ecuaciones}
\rightarrow
\text{Simulación}
\rightarrow
\text{Resultados}
}
$$

Cada resultado importante deberá poder relacionarse con los parámetros que lo generaron.

Esto permitirá reproducir posteriormente cualquier simulación.

### 5.12.19 Criterios para considerar una simulación válida

Una simulación podrá considerarse válida desde el punto de vista computacional cuando:

1. Las ecuaciones se encuentren correctamente implementadas.
2. Las unidades sean consistentes.
3. Las variables respeten las restricciones.
4. No existan valores `NaN` o infinitos.
5. No existan poblaciones negativas.
6. Las probabilidades se encuentren entre 0 y 1.
7. Las restricciones de producción se cumplan.
8. Los eventos de liberación se ejecuten correctamente.
9. Los resultados sean reproducibles bajo la misma configuración.
10. El comportamiento sea razonablemente consistente con los supuestos del modelo.

Esto representa una condición de validez computacional y no una certificación de validez epidemiológica.

### 5.12.20 Validación externa

Cuando existan datos independientes adecuados, podrán utilizarse para realizar una validación externa.

Estos datos deberán ser diferentes de aquellos utilizados para ajustar los parámetros del modelo.

El objetivo será comprobar si el modelo mantiene un comportamiento adecuado cuando se enfrenta a información que no fue utilizada durante su construcción.

La disponibilidad de datos externos determinará hasta qué punto podrá realizarse esta etapa.

### 5.12.21 Calibración y validación

La calibración y la validación deberán mantenerse como procesos diferenciados.

La calibración consistirá en ajustar determinados parámetros utilizando información disponible.

La validación consistirá posteriormente en evaluar el comportamiento del modelo mediante información o pruebas independientes.

Conceptualmente:

$$
\text{Datos de calibración}
\rightarrow
\text{Ajuste}
\rightarrow
\text{Modelo calibrado}
$$

y posteriormente:

$$
\text{Datos independientes}
\rightarrow
\text{Validación}
$$

No deberán utilizarse los mismos datos como única evidencia para afirmar simultáneamente que el modelo fue calibrado y validado.

### 5.12.22 Limitaciones de la validación

La validación estará limitada por la disponibilidad de información específica sobre:

* población de GBG en México;
* población inicial;
* distribución espacial;
* tasas reproductivas;
* supervivencia;
* competitividad de machos estériles;
* infestación en bovinos;
* infestación en porcinos;
* respuesta de las poblaciones mexicanas a la TIE.

Cuando no exista información suficiente, la limitación deberá documentarse explícitamente.

No se deberán crear datos de validación artificiales para aparentar una validación que no existe.

### 5.12.23 Registro de las pruebas

Cada prueba de validación deberá registrar:

| Elemento              | Descripción                  |
| --------------------- | ---------------------------- |
| ID de prueba          | Identificador único          |
| Escenario             | Escenario utilizado          |
| Parámetros            | Valores empleados            |
| Condiciones iniciales | Estado inicial               |
| Prueba                | Descripción                  |
| Resultado esperado    | Comportamiento esperado      |
| Resultado obtenido    | Resultado de la simulación   |
| Estado                | Aprobada / Requiere revisión |
| Observaciones         | Comentarios                  |

Esto permitirá mantener un registro de las pruebas realizadas durante el desarrollo.

### 5.12.24 Resultado esperado de la validación

Al finalizar esta etapa se deberá contar con evidencia de que:

* la formulación matemática es consistente;
* la implementación computacional corresponde con las ecuaciones;
* el modelo cumple las restricciones establecidas;
* la solución numérica es estable;
* el comportamiento general es compatible con los supuestos biológicos;
* las limitaciones y fuentes de incertidumbre están identificadas.

La validación permitirá determinar si el modelo se encuentra preparado para utilizarse en la evaluación sistemática de estrategias de liberación.

### 5.12.25 Principio de interpretación

La validación del modelo no significa que los resultados sean predicciones exactas del comportamiento futuro del GBG en México.

La interpretación deberá considerar:

$$
\boxed{
\text{Validez del modelo}
\neq
\text{certeza de la predicción}
}
$$

Los resultados deberán interpretarse dentro de las condiciones, supuestos, parámetros y escenarios utilizados.

Cualquier conclusión sobre una estrategia de TIE deberá considerar las limitaciones del modelo y la calidad de la información utilizada para parametrizarlo.

## 5.13 Estructura computacional del modelo

La estructura computacional tendrá como finalidad transformar el modelo matemático definido en las secciones anteriores en un sistema organizado, reproducible y modificable mediante Python.

La implementación se dividirá en componentes independientes para evitar que las ecuaciones, los parámetros, la producción de la planta y la ejecución de los escenarios se encuentren mezclados en un único programa.

La estructura general será:

```text
Modelo matemático
       ↓
Parámetros
       ↓
Implementación de ecuaciones
       ↓
Producción de Metapa
       ↓
Estrategia de liberación
       ↓
Simulación
       ↓
Escenarios
       ↓
Resultados
```

### 5.13.1 Objetivo de la estructura computacional

La organización del código deberá permitir:

* modificar parámetros sin modificar las ecuaciones;
* cambiar la estrategia de liberación sin modificar el modelo poblacional;
* cambiar el escenario de producción sin modificar el simulador;
* ejecutar múltiples escenarios;
* almacenar los resultados;
* generar gráficas;
* repetir una simulación bajo las mismas condiciones;
* facilitar posteriormente la integración con el simulador y la plataforma web.

### 5.13.2 Estructura general del proyecto

La implementación se organizará inicialmente de la siguiente manera:

```text
modelo-gbg-mexico/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── src/
│   ├── modelo/
│   │   └── poblacion.py
│   │
│   ├── produccion/
│   │   └── planta.py
│   │
│   ├── simulacion/
│   │   └── simulador.py
│   │
│   └── escenarios/
│       └── escenarios.py
│
├── results/
│   ├── figures/
│   └── tables/
│
└── tests/
```

Esta estructura podrá ampliarse conforme avance el desarrollo.

### 5.13.3 Módulo de población

El archivo:

```text
src/modelo/poblacion.py
```

contendrá la implementación de las ecuaciones correspondientes a la dinámica poblacional del GBG.

Su función principal será recibir:

* tiempo;
* estado poblacional;
* parámetros;

y calcular las tasas de cambio:

$$
\frac{dX}{dt}
$$

El módulo deberá contener principalmente las funciones relacionadas con:

* población silvestre;
* apareamiento;
* competencia reproductiva;
* descendencia viable;
* población estéril.

Conceptualmente:

```python
def modelo_gbg(t, estado, parametros):
    ...
```

### 5.13.4 Módulo de producción

El archivo:

```text
src/produccion/planta.py
```

representará las restricciones asociadas con la planta de Metapa.

Este módulo tendrá como finalidad administrar:

$$
C_t
$$

$$
A_t
$$

y:

$$
R_t
$$

Por lo tanto, deberá permitir:

* definir escenarios de capacidad;
* comprobar disponibilidad;
* verificar si una liberación es factible;
* calcular utilización de capacidad;
* registrar la cantidad total liberada.

La producción de otras plantas no será utilizada como fuente de suministro dentro del modelo.

### 5.13.5 Módulo de simulación

El archivo:

```text
src/simulacion/simulador.py
```

será responsable de ejecutar el modelo matemático.

Este módulo integrará:

$$
\text{Modelo}
+
\text{Parámetros}
+
\text{Producción}
+
\text{Liberación}
$$

Su función será:

1. recibir la configuración;
2. comprobar los parámetros;
3. comprobar las restricciones;
4. ejecutar la integración numérica;
5. aplicar las liberaciones;
6. calcular variables derivadas;
7. evaluar los criterios de control y erradicación;
8. devolver los resultados.

### 5.13.6 Módulo de escenarios

El archivo:

```text
src/escenarios/escenarios.py
```

contendrá las configuraciones utilizadas para realizar las simulaciones.

Podrá incluir:

* escenarios de población inicial;
* escenarios de producción;
* estrategias de liberación;
* escenarios combinados;
* configuraciones de sensibilidad.

El objetivo será evitar escribir manualmente cada configuración dentro del código del simulador.

### 5.13.7 Separación entre parámetros y ecuaciones

Los parámetros no deberán encontrarse escritos directamente dentro de las ecuaciones.

Por ejemplo, se deberá evitar una implementación de este tipo:

```python
dMw_dt = 0.4 * Bv - 0.2 * Mw
```

si esos valores todavía son parámetros del modelo.

En su lugar, deberán utilizarse variables parametrizadas:

```python
dMw_dt = rM * Bv - muM * Mw
```

De esta manera, los valores podrán modificarse sin alterar la formulación matemática.

### 5.13.8 Estructura de los parámetros

Los parámetros podrán organizarse mediante una estructura de datos.

Conceptualmente:

```python
parametros = {
    "rM": ...,
    "rF": ...,
    "b": ...,
    "a": ...,
    "muM": ...,
    "muF": ...,
    "mus": ...,
    "c": ...
}
```

Los valores definitivos deberán incorporarse únicamente cuando cuenten con una fuente o justificación correspondiente.

Los valores pendientes no deberán rellenarse arbitrariamente.

### 5.13.9 Estado inicial

Las condiciones iniciales se mantendrán separadas de los parámetros.

Conceptualmente:

```python
estado_inicial = [
    Mw0,
    Fv0,
    Fm0,
    Ms0
]
```

Esto permitirá ejecutar el mismo modelo bajo diferentes condiciones iniciales.

### 5.13.10 Configuración de un escenario

Un escenario podrá representarse conceptualmente mediante:

```python
escenario = {
    "nombre": "S01",
    "estado_inicial": ...,
    "parametros": ...,
    "produccion": ...,
    "liberacion": ...,
    "duracion": ...
}
```

Esto permitirá que una misma estructura sea utilizada para diferentes simulaciones.

### 5.13.11 Flujo computacional

El flujo principal será:

```text
Cargar escenario
       ↓
Cargar parámetros
       ↓
Cargar condiciones iniciales
       ↓
Cargar capacidad de Metapa
       ↓
Definir estrategia de liberación
       ↓
Validar configuración
       ↓
Ejecutar modelo
       ↓
Aplicar liberaciones
       ↓
Calcular variables derivadas
       ↓
Evaluar control/erradicación
       ↓
Generar resultados
```

### 5.13.12 Validación previa a la simulación

Antes de ejecutar una simulación, el programa deberá comprobar:

```text
¿Existen todos los parámetros requeridos?
          ↓
¿Las unidades son compatibles?
          ↓
¿Las condiciones iniciales son válidas?
          ↓
¿La estrategia cumple R(t) ≤ C(t)?
          ↓
¿Los valores se encuentran dentro de los rangos permitidos?
          ↓
Ejecutar simulación
```

Si alguna condición no se cumple, la simulación deberá detenerse o marcarse como inválida.

### 5.13.13 Resultados de la simulación

El simulador deberá devolver los resultados de forma estructurada.

Como mínimo deberán incluir:

$$
M_w(t)
$$

$$
F_v(t)
$$

$$
F_m(t)
$$

$$
M_s(t)
$$

$$
N_w(t)
$$

$$
\rho(t)
$$

$$
p_s(t)
$$

$$
p_w(t)
$$

$$
R_t
$$

Además:

$$
T_C
$$

$$
T_E
$$

$$
R_{total}
$$

$$
U_C
$$

y:

$$
N_{w,f}
$$

### 5.13.14 Organización de resultados

Los resultados podrán organizarse mediante estructuras de datos de Python y posteriormente convertirse en tablas de `Pandas`.

Conceptualmente:

```python
resultados = {
    "tiempo": tiempo,
    "Mw": Mw,
    "Fv": Fv,
    "Fm": Fm,
    "Ms": Ms,
    "Nw": Nw,
    "rho": rho,
    "ps": ps,
    "pw": pw
}
```

Esto permitirá generar posteriormente archivos de resultados y gráficas.

### 5.13.15 Separación entre cálculo y visualización

El modelo matemático no deberá generar directamente las gráficas.

La separación será:

```text
Modelo
   ↓
Resultados
   ↓
Visualización
```

Esto permitirá modificar las gráficas sin alterar las ecuaciones.

Las gráficas podrán desarrollarse posteriormente utilizando `Matplotlib`.

### 5.13.16 Resultados gráficos

Entre las gráficas que podrán generarse se encuentran:

#### Población silvestre

$$
N_w(t)
$$

contra:

$$
t
$$

#### Machos silvestres y estériles

$$
M_w(t)
$$

y:

$$
M_s(t)
$$

contra el tiempo.

#### Relación estéril:silvestre

$$
\rho(t)
$$

contra el tiempo.

#### Liberaciones

$$
R_t
$$

contra el tiempo.

#### Comparación de estrategias

$$
N_w(t)
$$

para diferentes escenarios.

Estas visualizaciones permitirán interpretar el comportamiento del modelo.

### 5.13.17 Identificación de simulaciones

Cada ejecución deberá contar con un identificador.

Por ejemplo:

```text
SIM-0001
SIM-0002
SIM-0003
```

El identificador permitirá relacionar:

$$
\text{Simulación}
\rightarrow
\text{Escenario}
\rightarrow
\text{Parámetros}
\rightarrow
\text{Resultados}
$$

### 5.13.18 Reproducibilidad

Una simulación deberá poder reproducirse utilizando la misma configuración.

Para ello deberán conservarse:

* versión del modelo;
* parámetros;
* condiciones iniciales;
* escenario;
* capacidad de producción;
* estrategia de liberación;
* duración;
* configuración numérica.

Cuando se utilicen procedimientos aleatorios, también deberá registrarse la semilla utilizada.

### 5.13.19 Pruebas automatizadas

El directorio:

```text
tests/
```

se utilizará para almacenar pruebas automatizadas.

Las pruebas podrán verificar:

* cálculo de probabilidades;
* ecuaciones;
* restricciones;
* producción;
* liberaciones;
* casos límite;
* resultados esperados.

Por ejemplo:

```python
def test_probabilidades_apareamiento():
    ...
```

El objetivo será detectar errores antes de utilizar el modelo para análisis de escenarios.

### 5.13.20 Separación entre datos y código

Los datos utilizados para parametrizar el modelo no deberán escribirse directamente dentro de los módulos de Python cuando sea posible.

La estructura será:

```text
data/
├── raw/
└── processed/
```

`raw/` contendrá información original sin modificar.

`processed/` contendrá datos preparados para utilizarse en el modelo.

Esto permitirá mantener la trazabilidad de los datos utilizados.

### 5.13.21 Trazabilidad computacional

Cada resultado deberá poder relacionarse con su origen mediante:

$$
\boxed{
\text{Fuente}
\rightarrow
\text{Dato}
\rightarrow
\text{Parámetro}
\rightarrow
\text{Modelo}
\rightarrow
\text{Simulación}
\rightarrow
\text{Resultado}
}
$$

Esta trazabilidad será especialmente importante para los parámetros biológicos y los datos de capacidad de la planta de Metapa.

### 5.13.22 Integración futura con el simulador

La estructura desarrollada en esta fase deberá permitir que posteriormente otro componente utilice el modelo para evaluar diferentes estrategias.

La relación prevista será:

```text
Modelo matemático
       ↓
Motor de simulación
       ↓
Evaluación de estrategias
       ↓
Resultados
       ↓
Simulador
```

Por lo tanto, el modelo deberá funcionar de manera independiente de cualquier interfaz gráfica o aplicación web.

### 5.13.23 Integración futura con la plataforma web

En una fase posterior, la plataforma web podrá enviar parámetros al motor de simulación.

El flujo conceptual será:

```text
Usuario
   ↓
Plataforma web
   ↓
Configuración del escenario
   ↓
Motor de simulación
   ↓
Modelo matemático
   ↓
Resultados
   ↓
Plataforma web
   ↓
Visualización
```

La plataforma web no deberá contener directamente las ecuaciones del modelo.

Esto permitirá mantener separadas la lógica científica y la interfaz de usuario.

### 5.13.24 Ventajas de la estructura modular

La estructura modular permitirá:

* facilitar el mantenimiento;
* reducir errores;
* reutilizar las ecuaciones;
* comparar escenarios;
* realizar pruebas;
* incorporar nuevos parámetros;
* cambiar estrategias de liberación;
* agregar nuevas fuentes de datos;
* integrar posteriormente el simulador;
* integrar posteriormente la plataforma web.

### 5.13.25 Principio de diseño

La implementación seguirá el principio:

$$
\boxed{
\text{Una responsabilidad principal por módulo}
}
$$

Por lo tanto:

| Módulo                     | Responsabilidad                     |
| -------------------------- | ----------------------------------- |
| `modelo/poblacion.py`      | Ecuaciones poblacionales            |
| `produccion/planta.py`     | Capacidad y restricciones de Metapa |
| `simulacion/simulador.py`  | Ejecución de simulaciones           |
| `escenarios/escenarios.py` | Configuración de escenarios         |
| `tests/`                   | Verificación del comportamiento     |
| `results/`                 | Resultados generados                |
| `data/`                    | Datos utilizados                    |
| `docs/`                    | Documentación                       |

### 5.13.26 Estado de implementación

La estructura de archivos del proyecto ya se encuentra preparada para comenzar la implementación del modelo.

Los módulos existentes son:

```text
src/modelo/poblacion.py
src/produccion/planta.py
src/simulacion/simulador.py
src/escenarios/escenarios.py
```

Sin embargo, la existencia de estos archivos no implica que el modelo matemático esté completamente implementado.

La implementación deberá realizarse después de validar los parámetros necesarios y revisar la consistencia de las ecuaciones.

### 5.13.27 Resultado esperado

Al finalizar esta etapa se deberá contar con una arquitectura computacional que permita:

1. Definir parámetros.
2. Definir condiciones iniciales.
3. Seleccionar un escenario.
4. Seleccionar una capacidad de producción de Metapa.
5. Definir una estrategia de liberación.
6. Ejecutar el modelo matemático.
7. Obtener la evolución de la población.
8. Evaluar los criterios de control y erradicación.
9. Calcular indicadores.
10. Almacenar los resultados.
11. Comparar diferentes escenarios.

Esta estructura constituirá la base computacional sobre la cual posteriormente se desarrollará el simulador de estrategias y, en una fase posterior, la plataforma web.

## 5.14 Flujo general de ejecución del modelo

El flujo general de ejecución establece la secuencia mediante la cual los datos, parámetros, condiciones iniciales, capacidad de producción y estrategias de liberación serán procesados para obtener los resultados de la simulación.

El modelo seguirá una estructura secuencial en la que cada etapa proporciona información a la siguiente.

### 5.14.1 Flujo general

El proceso completo se representa de la siguiente manera:

```text
Fuentes de información
        ↓
Datos y parámetros
        ↓
Condiciones iniciales
        ↓
Configuración del escenario
        ↓
Capacidad de producción de Metapa
        ↓
Estrategia de liberación
        ↓
Validación de restricciones
        ↓
Ejecución del modelo matemático
        ↓
Dinámica de la población
        ↓
Competencia reproductiva
        ↓
Actualización de la población
        ↓
Evaluación de criterios
        ↓
Cálculo de indicadores
        ↓
Almacenamiento de resultados
        ↓
Análisis y comparación de escenarios
```

### 5.14.2 Etapa 1. Fuentes de información

El proceso comienza con la recopilación de información necesaria para parametrizar el modelo.

Las fuentes podrán incluir:

* información oficial de la planta de Metapa;
* documentación de SENASICA;
* información de la Secretaría de Agricultura;
* literatura científica;
* documentos técnicos;
* modelos matemáticos publicados;
* información epidemiológica disponible.

Cada dato utilizado deberá conservar su referencia para mantener la trazabilidad del modelo.

La prioridad de las fuentes será:

$$
\text{Fuente oficial}
>
\text{Literatura científica}
>
\text{Modelo publicado}
>
\text{Estimación epidemiológica}
>
\text{Escenario hipotético}
$$

### 5.14.3 Etapa 2. Carga de parámetros

Los parámetros obtenidos de las fuentes serán incorporados al modelo.

Entre ellos se encuentran:

$$
b,\quad a,\quad \mu_M,\quad \mu_F,\quad \mu_s,\quad c
$$

así como los parámetros relacionados con:

* producción;
* liberación;
* condiciones iniciales;
* criterios de control;
* criterios de erradicación.

Los parámetros que todavía no cuenten con una fuente suficiente deberán permanecer identificados como pendientes.

### 5.14.4 Etapa 3. Definición de condiciones iniciales

Posteriormente se establecerá el estado inicial de la población:

$$
X(0)=
\begin{bmatrix}
M_w(0)\\
F_v(0)\\
F_m(0)\\
M_s(0)
\end{bmatrix}
$$

Estas condiciones representan el estado de la población al inicio de la simulación.

Cuando la simulación represente un momento previo a la liberación de moscas estériles:

$$
M_s(0)=0
$$

Las demás variables deberán definirse mediante información disponible o escenarios debidamente justificados.

### 5.14.5 Etapa 4. Configuración del escenario

Se seleccionará el escenario que será evaluado.

La configuración podrá incluir:

* población inicial;
* parámetros biológicos;
* capacidad de producción;
* cantidad de liberación;
* frecuencia de liberación;
* duración de la estrategia;
* tiempo total de simulación;
* criterio de control;
* criterio de erradicación.

Conceptualmente:

$$
S=
\{X_0,\theta,C_t,R_t,\Delta t_R,T_R,T_{sim}\}
$$

### 5.14.6 Etapa 5. Selección de capacidad de producción

Se establecerá la capacidad de producción correspondiente al escenario.

Para la planta de Metapa se consideran inicialmente:

$$
C_{ini}=28\,000\,000
$$

moscas por semana como capacidad inicial de referencia.

También se podrán evaluar:

$$
C_{max}=100\,000\,000
$$

moscas por semana como escenario proyectado y:

$$
C_{fut}=120\,000\,000
$$

moscas por semana como escenario futuro sujeto a expansión.

Estos valores representan escenarios de capacidad y no necesariamente cantidades que deban liberarse en su totalidad.

### 5.14.7 Etapa 6. Definición de la estrategia de liberación

Se establecerá la cantidad de moscas estériles que se pretende liberar:

$$
R_t
$$

junto con su frecuencia:

$$
\Delta t_R
$$

y duración:

$$
T_R
$$

La estrategia podrá ser:

* constante;
* periódica;
* proporcional a la población;
* basada en una relación estéril:silvestre;
* otra estrategia que posteriormente sea incorporada al modelo.

### 5.14.8 Etapa 7. Validación de restricciones

Antes de ejecutar la simulación se comprobará que la estrategia sea factible.

La principal restricción de producción será:

$$
R_t\le A_t\le C_t
$$

donde:

* \(C_t\) representa la capacidad disponible de Metapa;
* \(A_t\) representa la cantidad disponible para la estrategia;
* \(R_t\) representa la cantidad efectivamente liberada.

También deberán comprobarse las restricciones matemáticas y biológicas establecidas en la sección 5.6.

Si una estrategia supera la capacidad disponible, deberá identificarse como:

$$
\boxed{\text{Estrategia no factible}}
$$

y no deberá interpretarse como un resultado operativo válido.

### 5.14.9 Etapa 8. Ejecución del modelo matemático

Una vez validada la configuración se ejecutará el sistema de ecuaciones:

$$
\frac{dX(t)}{dt}=F(X(t),\theta,u(t))
$$

El integrador numérico calculará la evolución de las variables de estado durante el periodo de simulación.

El estado será actualizado progresivamente:

$$
X(t_0)\rightarrow X(t_1)\rightarrow X(t_2)\rightarrow\cdots\rightarrow X(t_n)
$$

### 5.14.10 Etapa 9. Aplicación de las liberaciones

Durante la simulación se aplicará la estrategia de liberación definida.

La incorporación de moscas estériles podrá representarse mediante:

$$
M_s(t^+)=M_s(t^-)+R_t
$$

cuando la liberación se realice de forma discreta.

Posteriormente, los machos estériles estarán sujetos a su dinámica de supervivencia:

$$
\frac{dM_s}{dt}=R(t)-\mu_sM_s(t)
$$

según la representación temporal utilizada.

### 5.14.11 Etapa 10. Competencia reproductiva

La presencia de machos estériles modificará la probabilidad de apareamiento de las hembras con machos silvestres.

La probabilidad conceptual de apareamiento con machos estériles será:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

mientras que:

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

Por lo tanto:

$$
p_s(t)+p_w(t)=1
$$

La competencia reproductiva afectará la cantidad de apareamientos capaces de generar descendencia viable.

### 5.14.12 Etapa 11. Actualización de la población

A partir de los apareamientos y la descendencia viable, el modelo actualizará las variables poblacionales.

La población silvestre será representada mediante:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

La evolución de esta población permitirá determinar si la estrategia de liberación produce una disminución sostenida.

### 5.14.13 Etapa 12. Cálculo de variables derivadas

Durante o después de la simulación se calcularán variables auxiliares.

Entre ellas:

#### Población silvestre

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

#### Relación estéril:silvestre

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

#### Probabilidad de apareamiento estéril

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

#### Probabilidad de apareamiento silvestre

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

Estas variables permitirán interpretar el comportamiento del sistema.

### 5.14.14 Etapa 13. Evaluación del control

Se comprobará si la población alcanza el criterio de control establecido:

$$
N_w(t)\le N_C
$$

El tiempo de control será:

$$
T_C=
\min\{t:N_w(t)\le N_C\}
$$

Si la población nunca alcanza el criterio dentro del periodo de simulación:

$$
T_C=\text{No alcanzado}
$$

### 5.14.15 Etapa 14. Evaluación de la erradicación

De manera similar se evaluará el criterio de erradicación:

$$
N_w(t)\le N_E
$$

con:

$$
T_E=
\min\{t:N_w(t)\le N_E\}
$$

Si el criterio no se alcanza durante la simulación:

$$
T_E=\text{No alcanzado}
$$

Esto permitirá distinguir entre una estrategia que solamente reduce la población y una que alcanza el criterio definido como erradicación dentro del modelo.

### 5.14.16 Etapa 15. Cálculo de indicadores

Al finalizar la simulación se calcularán los principales indicadores:

$$
T_C
$$

$$
T_E
$$

$$
R_{total}
$$

$$
U_C
$$

$$
N_{w,f}
$$

donde:

* \(T_C\): tiempo hasta alcanzar el criterio de control;
* \(T_E\): tiempo hasta alcanzar el criterio de erradicación;
* \(R_{total}\): cantidad total de moscas estériles liberadas;
* \(U_C\): utilización de la capacidad de producción;
* \(N_{w,f}\): población silvestre al finalizar la simulación.

### 5.14.17 Etapa 16. Almacenamiento de resultados

Los resultados serán almacenados de manera estructurada para permitir su análisis posterior.

Un registro de simulación deberá conservar como mínimo:

```text
ID de simulación
Escenario
Parámetros
Condiciones iniciales
Capacidad de producción
Estrategia de liberación
Tiempo de simulación
Resultados
Criterios alcanzados
```

Esto permitirá reproducir y comparar las simulaciones.

### 5.14.18 Etapa 17. Comparación de escenarios

Finalmente, los resultados podrán compararse entre diferentes escenarios.

Por ejemplo:

```text
             Escenario
                 ↓
       ┌─────────┼─────────┐
       ↓         ↓         ↓
      S01       S02       S03
       ↓         ↓         ↓
      T_C       T_C       T_C
      T_E       T_E       T_E
   R_total   R_total   R_total
       ↓         ↓         ↓
      Comparación
```

La comparación permitirá identificar qué estrategias presentan mejores resultados bajo las condiciones consideradas.

### 5.14.19 Flujo computacional resumido

El procedimiento completo puede resumirse como:

$$
\boxed{
\text{Datos}
\rightarrow
\text{Parámetros}
\rightarrow
\text{Condiciones iniciales}
\rightarrow
\text{Escenario}
\rightarrow
\text{Producción}
\rightarrow
\text{Liberación}
\rightarrow
\text{Simulación}
\rightarrow
\text{Población}
\rightarrow
\text{Criterios}
\rightarrow
\text{Indicadores}
\rightarrow
\text{Resultados}
}
$$

### 5.14.20 Consideraciones del flujo

El flujo de ejecución deberá mantener separadas tres funciones principales:

1. **Modelo matemático:** representa la dinámica poblacional.
2. **Producción y liberación:** establece las restricciones y estrategias de intervención.
3. **Simulación:** ejecuta el modelo y calcula los resultados.

Esta separación permitirá que el modelo matemático pueda utilizarse posteriormente por el simulador y, finalmente, por la plataforma web.

Asimismo, ningún resultado deberá interpretarse como una predicción absoluta de erradicación del GBG en México. Los resultados representarán el comportamiento del sistema bajo los parámetros, condiciones iniciales, restricciones y escenarios utilizados.

La confiabilidad de los resultados dependerá directamente de la calidad de los datos utilizados para parametrizar el modelo.

## 5.15 Indicadores y resultados esperados del modelo

Los indicadores permitirán evaluar cuantitativamente el comportamiento de la población de *Cochliomyia hominivorax* y determinar el efecto de diferentes estrategias de liberación de machos estériles.

Los resultados obtenidos dependerán de los parámetros, condiciones iniciales, capacidad de producción de la planta de Metapa de Domínguez y estrategia de liberación utilizada.

### 5.15.1 Población silvestre

El principal indicador poblacional será:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

donde \(N_w(t)\) representa la población silvestre total en el tiempo \(t\).

Este indicador permitirá observar si la población:

* aumenta;
* disminuye;
* permanece aproximadamente estable;
* alcanza el criterio de control;
* alcanza el criterio de erradicación;
* vuelve a crecer después de una reducción.

La evolución de \(N_w(t)\) será uno de los principales resultados gráficos del modelo.

### 5.15.2 Población de machos estériles

Se registrará:

$$
M_s(t)
$$

Esta variable permitirá conocer la cantidad de machos estériles presentes en la población durante la simulación.

Su comportamiento dependerá de:

* cantidad liberada;
* frecuencia de liberación;
* supervivencia de los machos estériles;
* duración de la estrategia.

La comparación entre \(M_s(t)\) y \(M_w(t)\) permitirá analizar la presión reproductiva ejercida por los machos estériles.

### 5.15.3 Relación estéril:silvestre

Se calculará:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

cuando \(M_w(t)>0\).

Esta relación permitirá medir la proporción de machos estériles respecto a los machos silvestres.

También permitirá comparar la simulación con referencias operativas como:

$$
\rho=10:1
$$

Sin embargo, esta relación no será considerada por sí misma como un criterio de erradicación.

Cuando:

$$
M_w(t)=0
$$

la razón deberá manejarse mediante una condición especial para evitar una división entre cero.

### 5.15.4 Probabilidad de apareamiento con machos estériles

Se calculará:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

Este indicador representa, dentro de la formulación simplificada del modelo, la probabilidad de que una hembra virgen se aparee con un macho estéril.

Su valor deberá encontrarse entre:

$$
0\le p_s(t)\le1
$$

Un incremento de \(M_s(t)\), bajo los demás parámetros constantes, deberá incrementar la competencia reproductiva de los machos estériles dentro del modelo.

### 5.15.5 Probabilidad de apareamiento con machos silvestres

Se calculará:

$$
p_w(t)=
\frac{M_w(t)}
{M_w(t)+cM_s(t)}
$$

cumpliéndose:

$$
p_s(t)+p_w(t)=1
$$

Este indicador permitirá analizar qué proporción de los apareamientos corresponde a machos silvestres bajo las condiciones simuladas.

### 5.15.6 Apareamientos efectivos

Se registrarán los apareamientos asociados con cada tipo de macho:

$$
A_w(t)=aF_v(t)p_w(t)
$$

y:

$$
A_s(t)=aF_v(t)p_s(t)
$$

Estos indicadores permitirán observar cómo cambia la distribución de apareamientos conforme se modifica la cantidad de machos estériles.

### 5.15.7 Descendencia viable

La descendencia viable se calculará mediante:

$$
B_v(t)=bA_w(t)
$$

donde \(B_v(t)\) representa la cantidad de descendencia viable generada por los apareamientos con machos silvestres bajo la formulación actual.

La reducción de \(B_v(t)\) será uno de los mecanismos mediante los cuales el modelo representará el efecto de la Técnica del Insecto Estéril.

### 5.15.8 Cantidad de moscas estériles liberadas

Se registrará la cantidad liberada durante cada periodo:

$$
R_t
$$

y la cantidad acumulada:

$$
R_{total}=\sum_tR_t
$$

Este indicador permitirá conocer cuántas moscas estériles fueron necesarias para ejecutar una determinada estrategia.

### 5.15.9 Utilización de la capacidad de producción

Se calculará la utilización de la capacidad disponible de la planta:

$$
U_{C,t}=\frac{R_t}{C_t}
$$

y, para el periodo total:

$$
U_C=
\frac{\sum_tR_t}{\sum_tC_t}
$$

Este indicador permitirá determinar qué proporción de la capacidad disponible de Metapa fue utilizada por una estrategia.

Un escenario que requiera una cantidad superior a la capacidad disponible será considerado no factible bajo las condiciones establecidas.

### 5.15.10 Tiempo hasta alcanzar el control

El tiempo de control será:

$$
T_C=
\min\{t:N_w(t)\le N_C\}
$$

Este indicador representa el tiempo requerido para que la población alcance el criterio definido como control.

Si el criterio no se alcanza durante la simulación:

$$
T_C=\text{No alcanzado}
$$

### 5.15.11 Tiempo hasta alcanzar la erradicación

El tiempo de erradicación será:

$$
T_E=
\min\{t:N_w(t)\le N_E\}
$$

Este indicador permitirá determinar cuándo la población alcanza el umbral definido para la erradicación dentro del modelo.

Si el criterio no se alcanza:

$$
T_E=\text{No alcanzado}
$$

Este resultado no deberá interpretarse como certificación de erradicación real del GBG en México.

### 5.15.12 Población final

Al terminar la simulación se registrará:

$$
N_{w,f}=N_w(T_{sim})
$$

Este indicador permitirá conocer el tamaño de la población silvestre al finalizar el periodo analizado.

Será especialmente útil cuando una estrategia no alcance los criterios \(N_C\) o \(N_E\).

### 5.15.13 Reducción de la población

Podrá calcularse la reducción relativa respecto a la población inicial:

$$
D_N=
1-\frac{N_{w,f}}{N_w(0)}
$$

o expresada como porcentaje:

$$
D_N(\%)=
\left(
1-\frac{N_{w,f}}{N_w(0)}
\right)100
$$

Este indicador permitirá comparar la efectividad relativa de diferentes estrategias.

### 5.15.14 Mínimo poblacional alcanzado

Se registrará:

$$
N_{w,min}=\min_tN_w(t)
$$

Este indicador permitirá conocer el nivel mínimo de población alcanzado durante la simulación.

Será útil para distinguir entre:

* reducción temporal;
* reducción sostenida;
* recuperación posterior;
* acercamiento al criterio de erradicación.

### 5.15.15 Comportamiento posterior al control

No será suficiente comprobar que una estrategia alcanza temporalmente un criterio.

También se deberá observar el comportamiento posterior de:

$$
N_w(t)
$$

Esto permitirá determinar si la población:

```text
Alcanza el criterio
       ↓
Se mantiene baja
```

o:

```text
Alcanza el criterio
       ↓
Vuelve a aumentar
```

Cuando los datos y la formulación lo permitan, podrá incorporarse un criterio de permanencia durante un periodo \(T_S\).

### 5.15.16 Clasificación de resultados

Cada escenario podrá clasificarse mediante categorías como:

| Clasificación           | Condición                                          |
| ----------------------- | -------------------------------------------------- |
| No controlado           | No alcanza \(N_C\)                                 |
| Controlado              | Alcanza \(N_C\)                                    |
| Erradicación alcanzada  | Alcanza \(N_E\)                                    |
| Control temporal        | Alcanza \(N_C\), pero posteriormente aumenta       |
| No factible             | Incumple las restricciones de producción           |
| Resultado indeterminado | No puede evaluarse por falta de parámetros o datos |

La clasificación dependerá de los criterios establecidos y deberá quedar registrada junto con los resultados numéricos.

### 5.15.17 Indicadores principales

Los indicadores principales del modelo serán:

| Indicador                  | Símbolo       | Función                                     |
| -------------------------- | ------------- | ------------------------------------------- |
| Población silvestre        | \(N_w(t)\)    | Evaluar dinámica poblacional                |
| Machos estériles           | \(M_s(t)\)    | Evaluar presencia de individuos liberados   |
| Relación estéril:silvestre | \(\rho(t)\)   | Evaluar presión reproductiva                |
| Apareamiento estéril       | \(p_s(t)\)    | Evaluar competencia reproductiva            |
| Apareamiento silvestre     | \(p_w(t)\)    | Evaluar reproducción potencial              |
| Descendencia viable        | \(B_v(t)\)    | Evaluar generación de nueva población       |
| Liberación                 | \(R_t\)       | Evaluar estrategia                          |
| Liberación acumulada       | \(R_{total}\) | Cuantificar requerimiento total             |
| Utilización de capacidad   | \(U_C\)       | Evaluar uso de Metapa                       |
| Tiempo de control          | \(T_C\)       | Medir tiempo hasta control                  |
| Tiempo de erradicación     | \(T_E\)       | Medir tiempo hasta criterio de erradicación |
| Población final            | \(N_{w,f}\)   | Evaluar estado al final                     |
| Reducción poblacional      | \(D_N\)       | Comparar reducción                          |
| Mínimo poblacional         | \(N_{w,min}\) | Evaluar reducción máxima                    |

### 5.15.18 Resultados gráficos esperados

El modelo deberá permitir generar, como mínimo, las siguientes visualizaciones:

#### Gráfica 1. Evolución de la población silvestre

$$
N_w(t)
$$

contra el tiempo.

#### Gráfica 2. Machos silvestres y estériles

Comparación de:

$$
M_w(t)
$$

y:

$$
M_s(t)
$$

#### Gráfica 3. Relación estéril:silvestre

$$
\rho(t)
$$

contra el tiempo.

#### Gráfica 4. Liberaciones

$$
R_t
$$

contra el tiempo.

#### Gráfica 5. Comparación de escenarios

Comparación de:

$$
N_w(t)
$$

para diferentes estrategias.

#### Gráfica 6. Capacidad de producción y liberación

Comparación entre:

$$
C_t
$$

y:

$$
R_t
$$

para comprobar visualmente la utilización de la capacidad de Metapa.

### 5.15.19 Tabla comparativa de escenarios

Los resultados podrán concentrarse en una tabla como:

| Escenario | Capacidad | Liberación | \(T_C\) | \(T_E\) | \(R_{total}\) | \(U_C\) | \(N_{w,f}\) | Clasificación |
| --------- | --------: | ---------: | ------: | ------: | ------------: | ------: | ----------: | ------------- |
| S01       |       ... |        ... |     ... |     ... |           ... |     ... |         ... | ...           |
| S02       |       ... |        ... |     ... |     ... |           ... |     ... |         ... | ...           |
| S03       |       ... |        ... |     ... |     ... |           ... |     ... |         ... | ...           |

Los valores se generarán automáticamente a partir de las simulaciones.

### 5.15.20 Criterio para identificar una estrategia favorable

Una estrategia podrá considerarse favorable cuando, bajo las condiciones establecidas:

1. sea factible respecto a la capacidad de Metapa;
2. produzca una reducción de la población silvestre;
3. alcance el criterio de control o erradicación definido;
4. mantenga el resultado durante el periodo establecido, cuando corresponda;
5. requiera una cantidad de moscas estériles compatible con la capacidad disponible;
6. presente un comportamiento consistente bajo escenarios plausibles.

No se seleccionará una estrategia únicamente porque produzca el menor tiempo de erradicación.

También deberán considerarse el consumo de moscas estériles, la utilización de capacidad y la robustez ante incertidumbre.

### 5.15.21 Interpretación de los resultados

Los resultados deberán interpretarse como estimaciones condicionadas al modelo.

Por lo tanto:

$$
\boxed{
\text{Resultado del modelo}
\neq
\text{Predicción absoluta de la realidad}
}
$$

Una estrategia que alcance \(T_E\) dentro de la simulación significa que, bajo los parámetros y supuestos utilizados, se alcanzó el criterio matemático definido.

No significa por sí misma que el GBG haya sido erradicado en México.

La interpretación final deberá considerar:

* calidad de los parámetros;
* incertidumbre;
* condiciones iniciales;
* estructura del modelo;
* capacidad real de producción;
* comportamiento de la población;
* limitaciones descritas en la sección correspondiente.

### 5.15.22 Resultado esperado de esta etapa

Al finalizar la implementación, cada simulación deberá producir información suficiente para responder:

* ¿Cómo evoluciona la población de GBG?
* ¿Qué efecto tiene la liberación de machos estériles?
* ¿Cuántas moscas estériles se liberan?
* ¿La estrategia es compatible con la capacidad de Metapa?
* ¿Qué relación estéril:silvestre se alcanza?
* ¿Cuánto tarda en alcanzarse el control?
* ¿Cuánto tarda en alcanzarse el criterio de erradicación?
* ¿Cuál es la población al finalizar la simulación?
* ¿Qué estrategia presenta mejores resultados bajo las condiciones analizadas?
* ¿Qué tan sensible es el resultado ante cambios en los parámetros?

Estos indicadores constituirán la base para la evaluación posterior de estrategias de producción y liberación y para el desarrollo del simulador computacional.
