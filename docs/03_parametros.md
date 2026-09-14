# 3. Parámetros del modelo

## 3.1 Definición de parámetros

Los parámetros del modelo representan valores o características que permiten describir el comportamiento biológico de *Cochliomyia hominivorax*, las condiciones de producción de moscas estériles y las características de las estrategias de control mediante la Técnica del Insecto Estéril.

A diferencia de las variables de estado, que pueden cambiar durante el desarrollo de una simulación, los parámetros representan características utilizadas para definir las relaciones matemáticas del modelo. Algunos parámetros podrán mantenerse constantes durante una simulación, mientras que otros podrán depender del tiempo o variar entre escenarios.

Los parámetros serán utilizados para establecer las relaciones entre la población silvestre del gusano barrenador, la producción y disponibilidad de moscas estériles y las estrategias de liberación.

Para mantener la trazabilidad de la información, cada parámetro deberá contar con una definición, símbolo, unidad de medida, valor o rango, fuente de información y clasificación.

Los parámetros serán obtenidos prioritariamente de fuentes oficiales, literatura científica y documentos técnicos especializados. Cuando un parámetro no pueda determinarse mediante información disponible, será identificado como pendiente o podrá establecerse temporalmente como un parámetro de escenario.

No se asignarán valores numéricos sin una justificación documental o metodológica.

## 3.2 Parámetros de producción de la planta

Los parámetros de producción representan las características de la planta de producción de moscas estériles de gusano barrenador del ganado ubicada en Metapa de Domínguez, Chiapas. Estos parámetros permitirán representar la cantidad de moscas estériles que puede producir la planta y establecer las restricciones correspondientes para las estrategias de liberación.

Debido a que la planta inició operaciones durante 2026 y su producción se ha incrementado de manera progresiva, se deberá diferenciar entre valores proyectados de capacidad y registros reales de producción.

### Parámetros considerados

| Parámetro                      | Símbolo      | Unidad         |  Valor inicial | Tipo      |
| ------------------------------ | ------------ | -------------- | -------------: | --------- |
| Producción semanal             | \(C_t\)      | moscas/semana  |       Variable | Planta    |
| Capacidad proyectada           | \(C_{\max}\) | moscas/semana  |    100,000,000 | Planta    |
| Producción inicial reportada   | \(C_{ini}\)  | moscas/semana  |     28,000,000 | Planta    |
| Posible capacidad futura       | \(C_{fut}\)  | moscas/semana  |    120,000,000 | Escenario |
| Disponibilidad para liberación | \(A_t\)      | moscas/periodo | Por determinar | Control   |
| Cantidad liberada              | \(R_t\)      | moscas/periodo |       Variable | Control   |

La producción semanal \(C_t\) será considerada como un parámetro dependiente del tiempo, debido a que la capacidad de producción de la planta no necesariamente permanece constante durante todo el periodo de simulación.

La información oficial indica que la planta comenzó su operación a finales de junio de 2026 y que la producción se incrementaría gradualmente hasta alcanzar una meta de 100 millones de insectos estériles. En julio de 2026 se realizó el primer ciclo de producción y esterilización de pupas en la planta de Metapa, seguido de la primera liberación de 2.5 millones de moscas producidas en Chiapas.

Por esta razón, el modelo deberá permitir representar una producción variable durante el periodo inicial de operación.

### Producción semanal

El parámetro \(C_t\) representará la cantidad de moscas estériles producidas por la planta durante el periodo \(t\):

$$
C_t = \text{producción de moscas estériles durante el periodo }t
$$

Cuando se disponga de registros oficiales para una semana determinada, estos valores tendrán prioridad sobre las capacidades proyectadas.

SENASICA mantiene una publicación específica con registros semanales de producción de moscas estériles y parasitoides, incluyendo documentos correspondientes a diferentes semanas de 2026. Estos registros serán utilizados posteriormente para construir la serie temporal de producción de Metapa.

### Capacidad máxima de referencia

La capacidad proyectada de la planta será representada mediante:

$$
C_{\max}=100\,000\,000
$$

moscas estériles por semana.

Este valor será utilizado como referencia de capacidad de producción y no deberá interpretarse automáticamente como producción real para todas las semanas de la simulación.

### Posible ampliación

La posibilidad de una capacidad superior a la operación base podrá representarse mediante un escenario independiente. En este caso se podrá evaluar:

$$
C_{\max,fut}=120\,000\,000
$$

moscas estériles por semana.

Este valor no será utilizado en el escenario base mientras no exista evidencia de que dicha ampliación forma parte de la capacidad operativa efectiva de la planta.

### Relación con la liberación

La producción de la planta no será equivalente automáticamente a la cantidad liberada. Para representar esta diferencia se utilizarán los parámetros:

$$
A_t \leq C_t
$$

y:

$$
R_t \leq A_t
$$

donde:

* \(C_t\) representa la producción disponible de la planta durante el periodo \(t\).
* \(A_t\) representa la cantidad disponible para una estrategia determinada.
* \(R_t\) representa la cantidad efectivamente asignada a la liberación.

Los valores de disponibilidad efectiva, pérdidas, proporción de machos y otros factores que puedan modificar la cantidad de insectos utilizables serán determinados posteriormente cuando exista información suficiente.

### Criterio de procedencia

Cada valor utilizado para parametrizar la producción deberá indicar si corresponde a:

* **Dato observado:** obtenido de registros oficiales de producción.
* **Capacidad proyectada:** valor establecido oficialmente como meta o capacidad esperada.
* **Escenario:** valor utilizado para analizar una posible condición futura.
* **Pendiente:** parámetro que todavía requiere información adicional.

De esta manera, el modelo podrá distinguir entre la producción real de la planta y las capacidades utilizadas únicamente para realizar simulaciones prospectivas.

## 3.3 Parámetros biológicos del gusano barrenador

Los parámetros biológicos representan las características naturales de *Cochliomyia hominivorax* necesarias para describir la dinámica de su población silvestre.

Estos parámetros permitirán representar procesos como la reproducción, desarrollo, supervivencia y mortalidad de los individuos. Debido a que el modelo busca evaluar el efecto de la Técnica del Insecto Estéril sobre la población silvestre, los parámetros relacionados con la reproducción y supervivencia tendrán una importancia particular.

El gusano barrenador del ganado presenta metamorfosis completa y su ciclo biológico comprende las etapas de huevo, larva, pupa y adulto. La fase larvaria se desarrolla como parásito obligado en el tejido vivo del hospedador. Posteriormente, las larvas maduras abandonan al hospedador y forman pupas en el ambiente, de las cuales emergen los adultos. La duración de algunas etapas puede variar de acuerdo con las condiciones ambientales.

Para la construcción del modelo se considerarán inicialmente los siguientes grupos de parámetros:

### Parámetros de desarrollo

| Parámetro                        | Símbolo | Unidad | Estado         |
| -------------------------------- | ------- | ------ | -------------- |
| Duración del desarrollo larvario | \(d_L\) | días   | Por determinar |
| Duración de la fase pupal        | \(d_P\) | días   | Por determinar |
| Duración de la etapa adulta      | \(d_A\) | días   | Por determinar |
| Tiempo de desarrollo huevo-larva | \(d_E\) | días   | Por determinar |

Como referencia biológica, las larvas completan aproximadamente su desarrollo en siete días antes de abandonar al hospedador y pasar a la fase de pupa. La emergencia de adultos puede ocurrir entre aproximadamente 7 y 54 días después de la formación de la pupa, dependiendo de las condiciones de temperatura y humedad.

Estos valores serán utilizados únicamente como referencia inicial. Para el modelo definitivo se determinará qué representación temporal resulta más adecuada y qué valores deben utilizarse bajo las condiciones consideradas.

### Parámetros reproductivos

| Parámetro                                  | Símbolo   | Unidad            | Estado         |
| ------------------------------------------ | --------- | ----------------- | -------------- |
| Fecundidad de la hembra                    | \(b\)     | huevos/hembra     | Por determinar |
| Proporción de hembras en la descendencia   | \(r\)     | proporción        | Por determinar |
| Tasa de reproducción                       | \(\beta\) | individuos/tiempo | Por determinar |
| Proporción de hembras que logran aparearse | \(p_m\)   | proporción        | Por determinar |

Las hembras de *Cochliomyia hominivorax* se aparean normalmente una sola vez y pueden producir hasta aproximadamente 3,000 huevos durante su vida adulta. La fecundidad efectiva utilizada en el modelo no deberá establecerse únicamente a partir de este valor máximo, ya que deberá considerarse la información disponible sobre condiciones ambientales y supervivencia.

### Parámetros de supervivencia y mortalidad

| Parámetro                       | Símbolo   | Unidad     | Estado         |
| ------------------------------- | --------- | ---------- | -------------- |
| Mortalidad de machos silvestres | \(\mu_M\) | 1/día      | Por determinar |
| Mortalidad de hembras vírgenes  | \(\mu_V\) | 1/día      | Por determinar |
| Mortalidad de hembras apareadas | \(\mu_F\) | 1/día      | Por determinar |
| Supervivencia larvaria          | \(S_L\)   | proporción | Por determinar |
| Supervivencia pupal             | \(S_P\)   | proporción | Por determinar |
| Supervivencia adulta            | \(S_A\)   | proporción | Por determinar |

Estos parámetros permitirán representar las pérdidas naturales de individuos durante las diferentes etapas del ciclo biológico.

Cuando sea posible, las tasas de mortalidad y supervivencia deberán obtenerse de estudios realizados bajo condiciones comparables con las del escenario que se desea representar. Cuando un único valor no sea suficiente para describir la variabilidad biológica, podrá utilizarse un rango de valores para realizar análisis de sensibilidad.

### Parámetros relacionados con la población adulta

Debido a que el objetivo principal del modelo es analizar la reproducción de la población silvestre y el efecto de la liberación de machos estériles, será necesario determinar qué etapas del ciclo deben representarse explícitamente.

Como referencia metodológica, un modelo matemático publicado en 2026 para el control del gusano barrenador mediante la Técnica del Insecto Estéril utiliza una representación centrada en la etapa adulta, diferenciando machos fértiles, hembras vírgenes, hembras apareadas, hospedadores infestados y machos estériles.

Esta estructura será considerada como referencia para el presente proyecto, pero la selección definitiva de las variables y parámetros se realizará después de analizar la información disponible y los objetivos específicos del modelo.

### Criterio de utilización de los parámetros

Los parámetros biológicos serán clasificados de acuerdo con su procedencia:

* **Dato científico:** obtenido de literatura especializada.
* **Dato experimental:** obtenido de estudios o mediciones experimentales.
* **Dato oficial:** obtenido de instituciones sanitarias o gubernamentales.
* **Rango biológico:** intervalo reportado en la literatura.
* **Supuesto de escenario:** valor utilizado temporalmente cuando no exista información suficiente.

No se asignarán valores definitivos a los parámetros biológicos únicamente para completar la tabla. Cada valor deberá contar con una fuente o ser identificado explícitamente como supuesto de escenario.

Los parámetros biológicos podrán ser modificados posteriormente durante el análisis de sensibilidad para determinar cuáles tienen mayor influencia sobre el crecimiento o disminución de la población silvestre.

## 3.4 Parámetros de la Técnica del Insecto Estéril

Los parámetros de la Técnica del Insecto Estéril (TIE) representan las características que determinan la capacidad de los machos estériles para competir con los machos silvestres y reducir la reproducción de la población objetivo.

La TIE consiste en la liberación sistemática de machos esterilizados dentro de la población silvestre. Cuando una hembra silvestre se aparea con un macho estéril, el apareamiento no produce descendencia viable. Por lo tanto, el efecto de la técnica depende de mantener una presencia suficiente de machos estériles en relación con los machos fértiles de la población silvestre.

Para el modelo será necesario representar no solamente la cantidad de machos estériles liberados, sino también su capacidad efectiva para competir por apareamientos y sobrevivir durante el periodo en que permanecen disponibles en el ambiente.

### Parámetros considerados

| Parámetro                                        | Símbolo   | Unidad         | Estado         |
| ------------------------------------------------ | --------- | -------------- | -------------- |
| Cantidad de machos estériles liberados           | \(R_t\)   | machos/periodo | Variable       |
| Supervivencia de machos estériles                | \(S_s\)   | proporción     | Por determinar |
| Mortalidad de machos estériles                   | \(\mu_s\) | 1/tiempo       | Por determinar |
| Competitividad relativa del macho estéril        | \(c\)     | adimensional   | Por determinar |
| Proporción de apareamientos con machos estériles | \(p_s\)   | proporción     | Variable       |
| Relación estériles:silvestres                    | \(S:W\)   | razón          | Variable       |
| Eficacia de esterilización                       | \(E_s\)   | proporción     | Por determinar |

### Competitividad de los machos estériles

La competitividad relativa representa la capacidad de un macho estéril para competir por una hembra en comparación con un macho silvestre.

Este parámetro será representado mediante:

$$
c = \frac{\text{aptitud de apareamiento del macho estéril}}
{\text{aptitud de apareamiento del macho silvestre}}
$$

Un valor de \(c=1\) representaría, de manera conceptual, una capacidad de competencia equivalente entre ambos tipos de machos. Un valor menor que uno representaría una menor competitividad del macho estéril.

La competitividad no será considerada automáticamente como igual a uno. La literatura sobre TIE muestra que la calidad biológica y la competitividad de los insectos irradiados son factores importantes para el éxito del programa. Una dosis de irradiación excesiva puede afectar características necesarias para la competencia reproductiva.

Como referencia metodológica, un modelo matemático reciente específico para *Cochliomyia hominivorax* utiliza una aptitud de apareamiento de los machos estériles inferior a la de los machos silvestres. Este valor será considerado como referencia para la selección del parámetro, pero no será incorporado automáticamente al modelo sin analizar previamente su fuente y aplicabilidad al contexto de Metapa.

### Probabilidad de apareamiento con un macho estéril

La proporción de hembras que se aparean con machos estériles dependerá de la cantidad relativa de machos estériles y machos silvestres, así como de su competitividad.

Como formulación conceptual inicial, podrá utilizarse una función de competencia:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

donde:

* \(p_s(t)\) representa la proporción o probabilidad de apareamiento con un macho estéril.
* \(M_s(t)\) representa la cantidad de machos estériles disponibles.
* \(M_w(t)\) representa la cantidad de machos silvestres fértiles.
* \(c\) representa la competitividad relativa de los machos estériles.

La expresión anterior se considera únicamente una formulación conceptual inicial. La ecuación definitiva será establecida después de revisar la estructura matemática completa del modelo y los parámetros disponibles.

La probabilidad complementaria de apareamiento con un macho silvestre podrá representarse como:

$$
p_w(t)=1-p_s(t)
$$

siempre que se mantengan los supuestos necesarios para utilizar esta formulación.

### Relación entre machos estériles y silvestres

La relación entre machos estériles y machos silvestres será una variable importante para evaluar la intensidad de las estrategias de liberación:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

Un incremento de esta relación aumenta, bajo los supuestos del modelo, la probabilidad de que una hembra silvestre encuentre un macho estéril en lugar de un macho fértil.

Sin embargo, una relación mayor de machos estériles no implica necesariamente una reducción proporcional de la población, debido a que también intervienen la competitividad, supervivencia, distribución espacial y dinámica reproductiva de la población silvestre.

### Eficacia de esterilización

La eficacia de esterilización representa la capacidad del tratamiento aplicado a los insectos para impedir la producción de descendencia viable.

Para el modelo podrá definirse:

$$
E_s = 1-P_v
$$

donde \(P_v\) representa la proporción de apareamientos con machos tratados que todavía producen descendencia viable.

La esterilización deberá considerarse como una característica diferente de la competitividad. Un macho puede estar esterilizado correctamente y, al mismo tiempo, presentar una capacidad de competencia reproductiva diferente a la de un macho silvestre.

### Supervivencia de los machos estériles

La cantidad de machos estériles disponible para competir con los machos silvestres disminuirá con el tiempo debido a la mortalidad posterior a la liberación.

Por esta razón, la cantidad de machos estériles presentes en el ambiente no necesariamente será igual a la cantidad liberada:

$$
M_s(t) \neq R_t
$$

La variable \(R_t\) representa la cantidad liberada durante un periodo, mientras que \(M_s(t)\) representa los machos estériles que permanecen disponibles para interactuar con la población silvestre.

El modelo deberá determinar posteriormente una función de supervivencia o mortalidad que permita relacionar ambas cantidades.

### Relación con la producción de Metapa

Los parámetros de la TIE estarán vinculados con los parámetros de producción de la planta mediante la cantidad de machos estériles efectivamente disponibles para las liberaciones.

De manera conceptual:

$$
R_t \leq A_t \leq C_t
$$

donde \(C_t\) representa la producción disponible de la planta, \(A_t\) la cantidad asignable a una estrategia y \(R_t\) la cantidad liberada.

Por lo tanto, una estrategia de control no podrá utilizar una cantidad de machos estériles superior a la disponibilidad proporcionada por la planta de Metapa durante el periodo correspondiente.

### Parámetros que requieren investigación adicional

Los siguientes parámetros deberán obtenerse posteriormente mediante literatura científica, documentos técnicos o datos específicos del programa:

* Competitividad relativa de los machos estériles de *Cochliomyia hominivorax*.
* Supervivencia de los machos después de la liberación.
* Mortalidad de machos estériles.
* Efecto de la irradiación sobre la aptitud reproductiva.
* Eficacia de esterilización.
* Relación adecuada de machos estériles respecto de machos silvestres.
* Distribución espacial de los machos liberados.
* Posibles diferencias entre individuos criados en laboratorio y población silvestre.

Estos parámetros no serán establecidos mediante valores arbitrarios. Cuando exista más de un valor reportado, se podrá utilizar un rango y posteriormente realizar un análisis de sensibilidad.

La selección definitiva de estos parámetros se realizará después de completar la revisión bibliográfica y definir la estructura matemática del modelo.

## 3.5 Parámetros epidemiológicos

Los parámetros epidemiológicos representan las características relacionadas con la presencia del gusano barrenador del ganado en los hospedadores considerados dentro del proyecto: bovinos y porcinos.

Estos parámetros permitirán relacionar la dinámica de la población de *Cochliomyia hominivorax* con la ocurrencia de infestaciones observadas en los animales. La inclusión de los hospedadores permitirá utilizar información epidemiológica como referencia para establecer las condiciones iniciales y validar el comportamiento general del modelo.

El gusano barrenador afecta principalmente a mamíferos durante la fase larvaria y las infestaciones generalmente se presentan en heridas abiertas. Entre los animales afectados se encuentran los bovinos y los cerdos, que corresponden a los dos hospedadores considerados en el alcance del presente proyecto. ([woah.org](https://www.woah.org/es/enfermedad/miasis-por-cochliomyia-hominivorax/?utm_source=chatgpt.com))

### Parámetros relacionados con bovinos

| Parámetro                          | Símbolo       | Unidad     | Estado         |
| ---------------------------------- | ------------- | ---------- | -------------- |
| Población bovina susceptible       | \(B\)         | animales   | Por determinar |
| Bovinos infestados                 | \(I_b\)       | animales   | Variable       |
| Tasa de infestación bovina         | \(\lambda_b\) | 1/tiempo   | Por determinar |
| Tasa de recuperación bovina        | \(\gamma_b\)  | 1/tiempo   | Por determinar |
| Probabilidad de infestación bovina | \(p_b\)       | proporción | Por determinar |

### Parámetros relacionados con porcinos

| Parámetro                           | Símbolo       | Unidad     | Estado         |
| ----------------------------------- | ------------- | ---------- | -------------- |
| Población porcina susceptible       | \(P\)         | animales   | Por determinar |
| Porcinos infestados                 | \(I_p\)       | animales   | Variable       |
| Tasa de infestación porcina         | \(\lambda_p\) | 1/tiempo   | Por determinar |
| Tasa de recuperación porcina        | \(\gamma_p\)  | 1/tiempo   | Por determinar |
| Probabilidad de infestación porcina | \(p_p\)       | proporción | Por determinar |

Estas variables no deberán interpretarse inicialmente como una población epidemiológica clásica de tipo susceptible-infectado-recuperado. El gusano barrenador no se transmite entre animales como una enfermedad contagiosa convencional, sino que las hembras adultas depositan huevos en heridas y las larvas se desarrollan en el tejido del hospedador.

Por esta razón, la relación entre población de moscas e infestaciones deberá establecerse mediante una formulación específica para el ciclo biológico del GBG y no mediante un modelo epidemiológico estándar sin modificaciones.

### Población de hospedadores

La cantidad de bovinos y porcinos presentes en una región podrá influir sobre la disponibilidad de hospedadores susceptibles a infestación. Sin embargo, no se asumirá que todos los animales tienen la misma probabilidad de ser infestados.

La susceptibilidad efectiva podrá depender de factores como:

* cantidad de animales presentes;
* disponibilidad de heridas;
* condiciones de manejo;
* distribución geográfica de los animales;
* presencia de moscas adultas;
* condiciones ambientales;
* movimiento de animales.

Cuando no exista información suficiente para representar estos factores individualmente, podrán incorporarse mediante parámetros agregados o escenarios.

### Relación entre infestaciones y población de GBG

El número de animales infestados podrá utilizarse como una medida indirecta de la presencia de la población silvestre.

De manera conceptual, se podrá representar una relación entre la población de moscas adultas y la ocurrencia de nuevas infestaciones:

$$
\lambda_b(t)=f(M_w(t),F(t),B(t))
$$

para bovinos, y:

$$
\lambda_p(t)=f(M_w(t),F(t),P(t))
$$

para porcinos.

donde:

* \(M_w(t)\) representa la población de machos silvestres.
* \(F(t)\) representa la población de hembras silvestres.
* \(B(t)\) representa la población bovina susceptible.
* \(P(t)\) representa la población porcina susceptible.
* \(\lambda_b(t)\) representa la intensidad de infestación en bovinos.
* \(\lambda_p(t)\) representa la intensidad de infestación en porcinos.

Estas expresiones son únicamente conceptuales y no constituyen todavía las ecuaciones definitivas del modelo.

### Uso de los registros epidemiológicos

Los registros oficiales de casos podrán utilizarse para establecer condiciones iniciales, identificar zonas afectadas y comparar el comportamiento general del modelo con la situación observada.

Los registros disponibles muestran que los eventos epidemiológicos pueden distinguirse por especie hospedadora. Por ejemplo, en un informe oficial de México se notificaron casos de miasis por *Cochliomyia hominivorax* en bovinos y un suino, además de casos en equinos. ([senasica.gob.mx](https://prod.senasica.gob.mx/ALERTAS/inicio/pages/single.php?noticia=22477))

Para este proyecto solamente se utilizarán los registros correspondientes a bovinos y porcinos, de acuerdo con el alcance establecido en la delimitación.

Los datos epidemiológicos deberán conservar información sobre:

* fecha del evento;
* ubicación;
* especie hospedadora;
* número de animales afectados;
* número de casos;
* fuente del registro.

Cuando sea posible, también se deberá conservar la información espacial asociada con cada evento para determinar posteriormente si resulta viable incorporar una dimensión geográfica al modelo.

### Parámetros que requieren investigación adicional

Para utilizar los hospedadores como parte cuantitativa del modelo será necesario investigar:

* Población de bovinos en las zonas consideradas.
* Población de porcinos en las zonas consideradas.
* Número de casos registrados en cada especie.
* Distribución temporal de los casos.
* Distribución espacial de los casos.
* Relación entre presencia de hembras adultas y aparición de nuevas infestaciones.
* Probabilidad o tasa de infestación.
* Disponibilidad de heridas susceptibles.
* Tiempo de desarrollo de las larvas dentro del hospedador.
* Relación entre casos observados y población silvestre de moscas.

Estos parámetros no serán asignados mediante valores arbitrarios.

### Consideración para la estructura definitiva del modelo

Los hospedadores podrán cumplir una de dos funciones dentro del modelo definitivo:

1. **Variable de estado:** cuando exista suficiente información para representar dinámicamente la población de animales infestados.

2. **Variable de observación o validación:** cuando los registros de animales infestados sean más adecuados como evidencia indirecta de la presencia de la población silvestre que como componente dinámico del sistema.

La decisión entre ambas alternativas se realizará después de revisar la disponibilidad y calidad de los datos epidemiológicos.

Esta consideración permitirá evitar que el modelo establezca una relación artificial entre el número de animales infestados y el número de moscas presentes cuando dicha relación no pueda sustentarse científicamente.

## 3.6 Parámetros de control y liberación

Los parámetros de control y liberación representan las condiciones bajo las cuales se aplicará la Técnica del Insecto Estéril (TIE) sobre la población silvestre del gusano barrenador del ganado.

Estos parámetros permiten definir la cantidad de machos estériles que serán liberados, la frecuencia de las liberaciones, la duración de la estrategia y los límites establecidos por la disponibilidad de moscas producidas en la planta de Metapa de Domínguez, Chiapas.

La TIE se basa en la liberación sistemática y repetida de machos estériles para aumentar la probabilidad de apareamiento con hembras silvestres y reducir progresivamente la reproducción de la población objetivo.

### 3.6.1 Cantidad de moscas estériles liberadas

La cantidad de moscas estériles liberadas durante un periodo determinado se representa mediante:

\[
R_t
\]

donde:

- \(R_t\) = cantidad de moscas estériles liberadas durante el periodo \(t\).
- Unidad: moscas/periodo.

Este parámetro constituye una de las principales variables de decisión del modelo, debido a que la cantidad liberada deberá ser suficiente para generar un efecto sobre la reproducción de la población silvestre, pero también deberá respetar la capacidad de producción disponible de la planta.

La cantidad de liberación no será considerada como un valor fijo para todos los escenarios. El modelo permitirá modificarla para evaluar diferentes estrategias.

### 3.6.2 Frecuencia de liberación

La frecuencia de liberación representa el número de eventos de liberación realizados durante un periodo determinado.

Se representa mediante:

\[
f_R
\]

donde:

- \(f_R\) = frecuencia de liberación.
- Unidad: liberaciones/semana o liberaciones/periodo.

También puede utilizarse el intervalo entre liberaciones:

\[
\Delta t_R
\]

donde:

- \(\Delta t_R\) = tiempo transcurrido entre dos liberaciones consecutivas.
- Unidad: días o semanas.

La frecuencia será importante debido a que los machos estériles liberados no permanecen indefinidamente en la población. Por lo tanto, el modelo deberá considerar la supervivencia de los machos estériles y la necesidad de realizar nuevas liberaciones.

### 3.6.3 Duración de la estrategia de liberación

La duración de la estrategia representa el periodo durante el cual se mantienen las liberaciones de moscas estériles.

Se representa mediante:

\[
T_R
\]

donde:

- \(T_R\) = duración de la estrategia de liberación.
- Unidad: semanas o meses.

Este parámetro podrá utilizarse para comparar estrategias de corta, media o larga duración.

### 3.6.4 Moscas disponibles para liberación

La cantidad disponible para liberación se representa mediante:

\[
A_t
\]

donde:

- \(A_t\) = cantidad de moscas estériles disponibles para ser asignadas a una estrategia durante el periodo \(t\).
- Unidad: moscas/periodo.

La disponibilidad dependerá de la producción de la planta y de las condiciones consideradas en el modelo.

Se establece la siguiente restricción:

\[
A_t \leq C_t
\]

donde \(C_t\) representa la producción disponible de la planta de Metapa durante el periodo correspondiente.

### 3.6.5 Restricción de liberación

La cantidad efectivamente liberada deberá cumplir:

\[
R_t \leq A_t
\]

Por lo tanto, la cantidad liberada nunca podrá superar la cantidad de moscas disponibles para la estrategia.

Combinando las restricciones de producción, disponibilidad y liberación:

\[
R_t \leq A_t \leq C_t
\]

Esta relación permitirá incorporar la capacidad real o proyectada de la planta de Metapa dentro del modelo matemático.

### 3.6.6 Relación entre moscas estériles y moscas silvestres

La proporción entre machos estériles y machos silvestres constituye una variable fundamental para evaluar la intensidad de la estrategia de liberación.

Se representa mediante:

\[
\rho_t = \frac{M_s(t)}{M_w(t)}
\]

donde:

- \(\rho_t\) = proporción de machos estériles respecto a machos silvestres.
- \(M_s(t)\) = cantidad de machos estériles disponibles en el ambiente.
- \(M_w(t)\) = cantidad de machos silvestres.
- Unidad: razón o proporción.

El valor de \(\rho_t\) no se considerará necesariamente constante, debido a que tanto la población silvestre como la población de machos estériles cambiarán con el tiempo.

### 3.6.7 Referencia de proporción estéril:silvestre

Para el contexto mexicano, la Secretaría de Agricultura y Desarrollo Rural ha señalado que en zonas de baja densidad de GBG se requieren al menos 10 machos estériles por cada mosca silvestre.

Por lo tanto, se podrá utilizar:

\[
\rho_{ref}=10:1
\]

como referencia operativa para determinados escenarios del modelo.

Este valor no se establecerá como una constante biológica universal. Se utilizará como un escenario o referencia de control, debido a que la proporción necesaria puede depender de la densidad de la población silvestre, la competitividad de los machos estériles, su supervivencia y las condiciones del área tratada.

### 3.6.8 Nivel objetivo de control

El modelo deberá establecer un nivel de población a partir del cual se considere que se ha alcanzado un estado de control.

Se representa mediante:

\[
N_C
\]

donde:

- \(N_C\) = población objetivo para considerar alcanzado el nivel de control.
- Unidad: individuos o población estimada.

El valor de \(N_C\) deberá establecerse posteriormente con base en criterios epidemiológicos y operativos disponibles.

No se asignará un valor arbitrario en esta etapa.

### 3.6.9 Criterio de erradicación

El modelo deberá establecer un criterio matemático para determinar cuándo se considera que la población silvestre ha sido erradicada o reducida al nivel establecido por el proyecto.

Se representa mediante:

\[
N_E
\]

donde:

- \(N_E\) = umbral de población utilizado como criterio de erradicación.
- Unidad: individuos o población estimada.

En una primera formulación, el criterio podrá expresarse como:

\[
N(t) \leq N_E
\]

donde \(N(t)\) representa la población silvestre total en el tiempo \(t\).

El valor definitivo de \(N_E\) deberá definirse posteriormente con base en criterios técnicos, epidemiológicos y de vigilancia.

### 3.6.10 Tiempo para alcanzar el objetivo

El tiempo necesario para alcanzar el criterio de control o erradicación se representará mediante:

\[
T_E
\]

donde:

- \(T_E\) = tiempo requerido para alcanzar el criterio establecido.
- Unidad: semanas o meses.

Este parámetro será calculado por el modelo y no será introducido inicialmente como un valor fijo.

El objetivo será determinar cómo cambia \(T_E\) ante diferentes cantidades y frecuencias de liberación.

### 3.6.11 Parámetros de control considerados

| Parámetro | Símbolo | Unidad | Valor inicial | Tipo |
|---|---|---|---|---|
| Cantidad liberada | \(R_t\) | moscas/periodo | Variable | CONTROL |
| Frecuencia de liberación | \(f_R\) | liberaciones/periodo | TBD | CONTROL |
| Intervalo de liberación | \(\Delta t_R\) | días/semanas | TBD | CONTROL |
| Duración de la estrategia | \(T_R\) | semanas/meses | Variable | CONTROL |
| Moscas disponibles | \(A_t\) | moscas/periodo | Variable | CONTROL |
| Proporción estéril:silvestre | \(\rho_t\) | razón | Variable | CONTROL |
| Proporción de referencia | \(\rho_{ref}\) | razón | 10:1 | ESCENARIO |
| Nivel objetivo de control | \(N_C\) | individuos | TBD | CONTROL |
| Umbral de erradicación | \(N_E\) | individuos | TBD | CONTROL |
| Tiempo para alcanzar el objetivo | \(T_E\) | semanas/meses | Calculado | RESULTADO |

### 3.6.12 Restricciones principales del modelo

Las estrategias de liberación deberán respetar las siguientes restricciones:

\[
A_t \leq C_t
\]

\[
R_t \leq A_t
\]

por lo que:

\[
R_t \leq A_t \leq C_t
\]

Además, la estrategia deberá considerar la relación entre machos estériles y machos silvestres:

\[
\rho_t = \frac{M_s(t)}{M_w(t)}
\]

y evaluar cómo esta proporción modifica la probabilidad de apareamiento de las hembras silvestres con machos estériles.

### 3.6.13 Consideraciones para los escenarios

Los parámetros de control podrán modificarse para construir diferentes escenarios de simulación.

Entre los escenarios que podrán evaluarse posteriormente se encuentran:

- liberación limitada por la producción inicial de la planta;
- liberación considerando una producción de 28 millones de moscas por semana;
- liberación progresiva conforme aumente la producción;
- liberación considerando una capacidad de 100 millones de moscas por semana;
- diferentes frecuencias de liberación;
- diferentes proporciones estéril:silvestre;
- diferentes niveles iniciales de infestación;
- diferentes criterios de control;
- diferentes criterios de erradicación.

La capacidad de 28 millones de moscas estériles por semana corresponde a la producción prevista para mediados de julio de 2026, mientras que la capacidad proyectada para finales de 2026 es de 100 millones semanales. Estos valores se utilizarán como condiciones de producción de la planta de Metapa y no como valores biológicos del GBG. :contentReference[oaicite:2]{index=2}

### 3.6.14 Datos confirmados y datos pendientes

**Datos confirmados o utilizables como referencia:**

- Producción inicial reportada para la planta de Metapa: 28 millones de moscas estériles por semana.
- Capacidad proyectada para finales de 2026: 100 millones de moscas estériles por semana.
- Referencia operativa de al menos 10 machos estériles por cada mosca silvestre en zonas de baja densidad.

**Datos pendientes de determinar:**

- frecuencia óptima de liberación;
- cantidad óptima por liberación;
- supervivencia de los machos estériles después de la liberación;
- competitividad de los machos estériles;
- proporción real de machos dentro del material disponible para liberación;
- pérdidas entre producción, disponibilidad y liberación;
- criterio cuantitativo de control;
- criterio cuantitativo de erradicación;
- tiempo esperado para alcanzar dichos criterios.

Estos valores deberán obtenerse de fuentes científicas, datos oficiales o mediante análisis de escenarios. No se asignarán valores arbitrarios cuando no exista evidencia suficiente.

## 3.7 Parámetros de escenario

Los parámetros de escenario permiten representar diferentes condiciones iniciales y estrategias de control dentro del modelo matemático.

A diferencia de los parámetros biológicos y de producción, los parámetros de escenario no necesariamente representan una característica fija del gusano barrenador o de la planta. Su función es permitir modificar las condiciones de una simulación para analizar cómo responde el sistema ante diferentes situaciones.

El uso de escenarios permitirá comparar diferentes niveles de infestación, capacidades de producción y estrategias de liberación de moscas estériles.

### 3.7.1 Población inicial de GBG

La población inicial representa la cantidad estimada de individuos silvestres existentes al inicio de una simulación.

Se representa mediante:

\[
N_0
\]

donde:

- \(N_0\) = población inicial de GBG.
- Unidad: individuos.

Dependiendo de la estructura final del modelo, esta población podrá estar distribuida entre diferentes grupos, por ejemplo:

- machos silvestres;
- hembras vírgenes;
- hembras apareadas.

El valor de \(N_0\) deberá establecerse a partir de datos disponibles o mediante escenarios cuando no exista una estimación directa suficientemente confiable.

No se deberá asumir que el número de animales infestados equivale directamente al número de moscas presentes.

### 3.7.2 Nivel inicial de infestación

Para representar diferentes situaciones epidemiológicas se podrán establecer distintos niveles iniciales de infestación.

Se utilizará:

\[
I_0
\]

donde:

- \(I_0\) = nivel inicial de infestación.
- Unidad: animales infestados o indicador epidemiológico, dependiendo de la estructura final del modelo.

Los hospedadores considerados serán únicamente bovinos y porcinos.

Los escenarios podrán diferenciarse, por ejemplo, en:

- infestación baja;
- infestación media;
- infestación alta.

Los valores numéricos deberán definirse posteriormente con base en datos epidemiológicos disponibles o mediante una metodología explícita de construcción de escenarios.

### 3.7.3 Producción inicial de la planta

La producción inicial de la planta se representa mediante:

\[
C_{ini}
\]

donde:

- \(C_{ini}\) = producción semanal inicial considerada para el escenario.
- Unidad: moscas estériles/semana.

Para el escenario correspondiente al inicio de operaciones se podrá utilizar como referencia:

\[
C_{ini}=28\,000\,000
\]

moscas estériles por semana.

Este valor corresponde a la producción reportada para la planta de Metapa durante su etapa inicial de operación.

### 3.7.4 Capacidad proyectada de producción

Para representar el incremento de producción previsto para la planta se utilizará:

\[
C_{max}
\]

donde:

- \(C_{max}\) = capacidad semanal máxima considerada en el escenario.
- Unidad: moscas estériles/semana.

Como escenario de referencia se utilizará:

\[
C_{max}=100\,000\,000
\]

moscas estériles por semana.

Este valor corresponde a la capacidad proyectada para finales de 2026.

### 3.7.5 Capacidad futura de producción

También podrá considerarse una capacidad superior como escenario exploratorio:

\[
C_{fut}
\]

donde:

- \(C_{fut}\) = capacidad futura de producción.
- Unidad: moscas estériles/semana.

Se podrá considerar:

\[
C_{fut}=120\,000\,000
\]

moscas estériles por semana como escenario futuro de análisis.

Este valor no representa la capacidad operativa actual de la planta, por lo que únicamente deberá utilizarse como escenario de expansión.

### 3.7.6 Estrategia de liberación

La estrategia de liberación determina cómo se distribuye la cantidad disponible de moscas estériles a lo largo del tiempo.

La estrategia podrá definirse mediante:

\[
S_R = \{R_t,\Delta t_R,T_R\}
\]

donde:

- \(R_t\) = cantidad liberada durante el periodo \(t\);
- \(\Delta t_R\) = intervalo entre liberaciones;
- \(T_R\) = duración de la estrategia.

Esto permitirá comparar estrategias que utilicen cantidades y frecuencias diferentes de liberación.

### 3.7.7 Intensidad de liberación

La intensidad de liberación representa la cantidad de moscas estériles liberadas en relación con la población silvestre.

Se podrá expresar mediante:

\[
\rho_t=\frac{M_s(t)}{M_w(t)}
\]

donde:

- \(M_s(t)\) = machos estériles presentes;
- \(M_w(t)\) = machos silvestres presentes;
- \(\rho_t\) = proporción estéril:silvestre.

Para los escenarios se podrán evaluar diferentes proporciones.

Por ejemplo:

| Escenario | Proporción estéril:silvestre |
|---|---:|
| Bajo | 5:1 |
| Referencia | 10:1 |
| Alto | 20:1 |

Los valores utilizados para estos escenarios deberán considerarse valores de simulación y no necesariamente recomendaciones operativas.

La proporción 10:1 podrá utilizarse como escenario de referencia debido a la referencia operativa reportada para zonas de baja densidad de GBG.

### 3.7.8 Escenarios de producción

Se plantean inicialmente los siguientes escenarios:

| Escenario | Producción considerada | Descripción |
|---|---:|---|
| P1 | 28 millones/semana | Etapa inicial de producción |
| P2 | Producción progresiva | Incremento gradual de la producción |
| P3 | 100 millones/semana | Capacidad proyectada para finales de 2026 |
| P4 | 120 millones/semana | Escenario futuro de expansión |

Estos escenarios permitirán analizar cómo la disponibilidad de moscas estériles modifica las estrategias de control.

### 3.7.9 Escenarios de infestación

Se podrán establecer diferentes condiciones iniciales de la población objetivo:

| Escenario | Nivel de infestación | Población inicial |
|---|---|---|
| I1 | Baja | \(N_{0,bajo}\) |
| I2 | Media | \(N_{0,medio}\) |
| I3 | Alta | \(N_{0,alto}\) |

Los valores de población deberán determinarse posteriormente mediante datos epidemiológicos o mediante una metodología de generación de escenarios.

### 3.7.10 Escenarios de liberación

Las estrategias podrán combinar diferentes cantidades y frecuencias de liberación.

Por ejemplo:

| Escenario | Cantidad liberada | Frecuencia | Objetivo |
|---|---|---|---|
| R1 | Baja | Alta | Evaluar estrategia de baja cantidad |
| R2 | Media | Alta | Evaluar estrategia intermedia |
| R3 | Alta | Alta | Evaluar estrategia intensiva |
| R4 | Variable | Variable | Evaluar estrategia adaptativa |

La cantidad exacta de moscas liberadas será determinada por las restricciones de producción y por los resultados del modelo.

### 3.7.11 Combinación de escenarios

Los escenarios de población, producción y liberación podrán combinarse para formar experimentos de simulación.

Conceptualmente:

\[
Escenario = \{N_0,C_t,R_t,\Delta t_R,T_R,\rho_t\}
\]

Por ejemplo, una simulación podrá combinar:

- población inicial alta;
- producción de 28 millones de moscas por semana;
- liberaciones semanales;
- proporción estéril:silvestre determinada;
- duración variable de la estrategia.

Otra simulación podrá utilizar:

- población inicial media;
- producción progresiva;
- liberaciones semanales;
- aumento progresivo de la cantidad liberada;
- capacidad máxima de 100 millones de moscas por semana.

### 3.7.12 Variables de salida para comparar escenarios

Cada escenario deberá generar resultados que permitan realizar comparaciones.

Las principales variables de salida serán:

- población silvestre a lo largo del tiempo;
- cantidad de machos silvestres;
- cantidad de hembras;
- cantidad de machos estériles disponibles;
- cantidad de moscas liberadas;
- proporción estéril:silvestre;
- tiempo para alcanzar el nivel de control;
- tiempo para alcanzar el criterio de erradicación;
- cantidad total de moscas estériles utilizadas;
- porcentaje de utilización de la capacidad de producción.

### 3.7.13 Criterio de comparación

Los escenarios serán comparados principalmente mediante:

\[
T_E
\]

\[
R_{total}=\sum_t R_t
\]

y

\[
U_C=\frac{\sum_t R_t}{\sum_t C_t}
\]

donde:

- \(T_E\) = tiempo para alcanzar el criterio de erradicación;
- \(R_{total}\) = cantidad total de moscas estériles liberadas;
- \(U_C\) = utilización acumulada de la capacidad de producción.

Esto permitirá evaluar no solamente qué estrategia reduce más rápidamente la población, sino también qué cantidad de moscas requiere y qué porcentaje de la capacidad disponible de Metapa utiliza.

### 3.7.14 Clasificación de los parámetros de escenario

Los parámetros de escenario se clasificarán de la siguiente manera:

| Parámetro | Símbolo | Tipo |
|---|---|---|
| Población inicial | \(N_0\) | ESCENARIO |
| Nivel inicial de infestación | \(I_0\) | ESCENARIO |
| Producción inicial | \(C_{ini}\) | ESCENARIO |
| Capacidad máxima | \(C_{max}\) | ESCENARIO |
| Capacidad futura | \(C_{fut}\) | ESCENARIO |
| Cantidad liberada | \(R_t\) | CONTROL/ESCENARIO |
| Intervalo de liberación | \(\Delta t_R\) | CONTROL/ESCENARIO |
| Duración de liberación | \(T_R\) | CONTROL/ESCENARIO |
| Proporción estéril:silvestre | \(\rho_t\) | CONTROL/ESCENARIO |

### 3.7.15 Consideraciones metodológicas

Los escenarios no deberán utilizarse para sustituir datos reales cuando existan datos confiables disponibles.

Se seguirá la siguiente prioridad:

1. Datos oficiales de la planta de Metapa.
2. Datos epidemiológicos oficiales de México.
3. Parámetros obtenidos de literatura científica.
4. Rangos reportados en estudios científicos.
5. Escenarios hipotéticos claramente identificados.

Cada valor utilizado en una simulación deberá indicar si corresponde a:

- dato observado;
- dato reportado en literatura;
- estimación;
- supuesto;
- escenario.

De esta manera se evitará presentar como dato real un valor utilizado únicamente para explorar el comportamiento del modelo.

## 3.8 Clasificación y procedencia de los parámetros

Para garantizar la trazabilidad de los valores utilizados en el modelo matemático, cada parámetro deberá registrar su procedencia y clasificación.

Esto permitirá distinguir entre valores obtenidos directamente de fuentes oficiales, valores obtenidos de literatura científica, estimaciones y valores utilizados únicamente para construir escenarios de simulación.

La procedencia de cada parámetro será especialmente importante cuando un valor tenga una influencia significativa sobre los resultados del modelo.

### 3.8.1 Clasificación de los parámetros

Los parámetros se clasificarán en las siguientes categorías:

| Clasificación | Descripción |
|---|---|
| PLANTA | Parámetros relacionados con la producción y capacidad de la planta de Metapa |
| BIOLÓGICO | Parámetros relacionados con la biología y dinámica del GBG |
| TIE | Parámetros relacionados con la Técnica del Insecto Estéril |
| EPIDEMIOLÓGICO | Parámetros relacionados con la infestación en bovinos y porcinos |
| CONTROL | Parámetros relacionados con las estrategias de liberación |
| ESCENARIO | Valores utilizados para representar condiciones hipotéticas o de análisis |
| RESULTADO | Valores calculados por el modelo a partir de otros parámetros |

### 3.8.2 Procedencia de los parámetros

Cada parámetro deberá clasificarse también de acuerdo con la fuente de la que se obtuvo.

Se utilizarán las siguientes categorías:

#### a) Datos oficiales

Corresponden a valores obtenidos de instituciones oficiales relacionadas con la producción, vigilancia o control del GBG.

Ejemplos:

- SENASICA;
- Secretaría de Agricultura y Desarrollo Rural;
- Gobierno de México;
- organismos oficiales internacionales cuando corresponda.

Estos datos tendrán prioridad cuando describan directamente las condiciones de la planta de Metapa o la situación epidemiológica de México.

#### b) Literatura científica

Corresponden a parámetros obtenidos de artículos científicos, libros, revisiones o modelos matemáticos publicados.

Estos valores podrán utilizarse para representar características biológicas del GBG o parámetros de la TIE cuando no exista información específica para México.

Cuando un parámetro provenga de otro estudio, deberá indicarse claramente la población, región o condiciones bajo las cuales fue estimado.

#### c) Fuente técnica especializada

Incluye documentos técnicos elaborados por organismos especializados, manuales y documentos metodológicos.

Estos documentos podrán utilizarse para complementar los datos científicos y oficiales.

#### d) Estimación

Corresponde a un valor calculado o aproximado a partir de información disponible.

Las estimaciones deberán indicar el método mediante el cual fueron obtenidas.

No deberán presentarse como datos observados.

#### e) Supuesto

Corresponde a un valor establecido temporalmente debido a la ausencia de información suficiente.

Los supuestos deberán identificarse explícitamente y deberán poder modificarse posteriormente.

#### f) Escenario

Corresponde a un valor establecido específicamente para analizar una situación hipotética.

Los valores de escenario no representan necesariamente condiciones reales.

### 3.8.3 Nivel de confianza

Además de la procedencia, cada parámetro podrá recibir un nivel de confianza.

Se utilizarán inicialmente tres categorías:

| Nivel | Descripción |
|---|---|
| Alto | Existe una fuente oficial o científica directamente aplicable al parámetro |
| Medio | Existe evidencia disponible, pero requiere adaptación o presenta incertidumbre |
| Bajo | El valor corresponde principalmente a una estimación, supuesto o escenario |

El nivel de confianza no significa que el parámetro sea verdadero o falso. Representa el grado de respaldo disponible para utilizarlo dentro del modelo.

### 3.8.4 Prioridad de las fuentes

Cuando existan diferentes valores para un mismo parámetro, se seguirá el siguiente orden de prioridad:

1. Datos oficiales específicos de la planta de Metapa.
2. Datos oficiales de México relacionados con GBG.
3. Estudios científicos específicos de *Cochliomyia hominivorax*.
4. Estudios científicos sobre TIE aplicables al GBG.
5. Documentos técnicos de organismos especializados.
6. Estimaciones derivadas de datos disponibles.
7. Supuestos y escenarios.

Esta jerarquía permitirá evitar que un valor hipotético sea utilizado en lugar de un dato oficial disponible.

### 3.8.5 Registro de procedencia

Cada parámetro deberá documentarse mediante una estructura que permita conocer su origen.

La información mínima será:

| Campo | Descripción |
|---|---|
| Parámetro | Nombre del parámetro |
| Símbolo | Símbolo utilizado en el modelo |
| Unidad | Unidad de medida |
| Valor | Valor utilizado |
| Fuente | Documento, institución o estudio |
| Tipo de fuente | Oficial, científica, técnica, estimación, supuesto o escenario |
| Año | Año de publicación o actualización |
| Aplicabilidad | Qué tan directamente puede aplicarse al modelo |
| Confianza | Alta, media o baja |
| Observaciones | Notas relevantes |

### 3.8.6 Ejemplo de registro

Un parámetro de producción de la planta puede registrarse de la siguiente manera:

| Parámetro | Símbolo | Unidad | Valor | Fuente | Tipo | Confianza |
|---|---|---|---:|---|---|---|
| Producción inicial reportada | \(C_{ini}\) | moscas/semana | 28,000,000 | SENASICA | Oficial | Alta |
| Capacidad proyectada | \(C_{max}\) | moscas/semana | 100,000,000 | SENASICA | Oficial | Alta |
| Capacidad futura | \(C_{fut}\) | moscas/semana | 120,000,000 | SENASICA | Oficial/escenario | Media |

Estos valores deberán conservar su contexto temporal. Una capacidad proyectada no deberá interpretarse automáticamente como producción real.

### 3.8.7 Diferencia entre dato, parámetro y supuesto

Dentro del proyecto se distinguirán tres conceptos:

**Dato:** información observada o reportada por una fuente.

**Parámetro:** valor utilizado por el modelo para representar una característica del sistema.

**Supuesto:** condición establecida por el equipo cuando no existe información suficiente.

Por ejemplo, una fuente puede reportar una producción semanal de la planta. Ese valor constituye un dato de la fuente y puede convertirse en un parámetro \(C_t\) dentro del modelo.

En cambio, si no se conoce la supervivencia de los machos estériles después de la liberación y se utiliza temporalmente un valor para realizar una simulación, dicho valor deberá identificarse como supuesto.

### 3.8.8 Parámetros variables y parámetros fijos

Los parámetros también podrán clasificarse según su comportamiento durante la simulación.

#### Parámetros fijos

Son aquellos que permanecen constantes durante una simulación.

Ejemplo:

\[
C_{max}=100\,000\,000
\]

si el escenario utiliza una capacidad máxima fija de producción.

#### Parámetros variables

Son aquellos cuyo valor puede cambiar durante la simulación.

Ejemplo:

\[
C_t
\]

cuando la producción de la planta aumenta progresivamente con el tiempo.

Otro ejemplo es:

\[
R_t
\]

cuando la cantidad liberada cambia de acuerdo con la estrategia de control.

### 3.8.9 Parámetros observados, estimados y de escenario

Para facilitar el análisis posterior, se utilizará la siguiente clasificación:

\[
Tipo \in \{OBSERVADO, ESTIMADO, SUPUESTO, ESCENARIO, CALCULADO\}
\]

Donde:

- **OBSERVADO:** obtenido de registros o mediciones;
- **ESTIMADO:** calculado a partir de información disponible;
- **SUPUESTO:** establecido temporalmente por falta de información;
- **ESCENARIO:** utilizado para explorar una condición hipotética;
- **CALCULADO:** obtenido directamente mediante las ecuaciones del modelo.

### 3.8.10 Trazabilidad de los parámetros

Cada parámetro utilizado en el modelo deberá poder rastrearse hasta su fuente o justificación.

La trazabilidad tendrá la siguiente estructura conceptual:

\[
Fuente \rightarrow Parámetro \rightarrow Modelo \rightarrow Resultado
\]

Por ejemplo:

\[
SENASICA
\rightarrow C_{max}
\rightarrow Restricción\ de\ producción
\rightarrow R_t
\rightarrow T_E
\]

Esto permitirá identificar cómo un dato externo termina influyendo en los resultados obtenidos por el modelo.

### 3.8.11 Manejo de incertidumbre

Cuando un parámetro presente incertidumbre, no se deberá forzar necesariamente a utilizar un único valor.

En estos casos podrá utilizarse un intervalo:

\[
p \in [p_{min},p_{max}]
\]

o diferentes escenarios:

\[
p_1,\ p_2,\ p_3
\]

Esto permitirá evaluar cómo cambia el resultado del modelo cuando existe incertidumbre en un parámetro.

Por ejemplo, si la competitividad de los machos estériles no puede establecerse mediante un único valor, podrá analizarse mediante diferentes escenarios de competitividad.

### 3.8.12 Sensibilidad de los parámetros

Posteriormente se podrá realizar un análisis de sensibilidad para identificar cuáles parámetros tienen mayor influencia sobre los resultados.

De manera conceptual:

\[
\text{Sensibilidad}(p_i)
=
\frac{\Delta Resultado}{\Delta p_i}
\]

El análisis de sensibilidad permitirá determinar qué parámetros deben investigarse con mayor precisión.

Esto será especialmente importante para parámetros relacionados con:

- competitividad de machos estériles;
- supervivencia;
- fecundidad;
- población inicial;
- cantidad de liberación;
- frecuencia de liberación;
- capacidad de producción.

### 3.8.13 Regla para incorporación de nuevos parámetros

Antes de incorporar un nuevo parámetro al modelo deberá verificarse:

1. qué representa;
2. cuál es su símbolo;
3. cuál es su unidad;
4. cuál es su valor;
5. cuál es su fuente;
6. qué tipo de dato representa;
7. qué nivel de confianza tiene;
8. qué ecuación utiliza el parámetro;
9. qué resultado afecta.

Si no existe información suficiente, el parámetro deberá marcarse como pendiente, supuesto o escenario según corresponda.

De esta manera se evitará introducir valores sin justificación dentro del modelo matemático.

## 3.9 Parámetros confirmados

Los parámetros confirmados son aquellos valores o características del sistema que cuentan con respaldo documental suficiente y que pueden incorporarse al proyecto sin necesidad de establecerlos como supuestos.

La confirmación de un parámetro se refiere a que existe una fuente que respalda su existencia o valor. Esto no significa necesariamente que el parámetro sea completamente representativo de todas las condiciones del modelo.

Cuando un parámetro corresponda a una capacidad proyectada, referencia operativa o condición particular, deberá conservarse esta característica en su documentación.

### 3.9.1 Parámetros confirmados de la planta

La planta considerada para el modelo es la Planta de Producción de Moscas Estériles del Gusano Barrenador del Ganado ubicada en Metapa de Domínguez, Chiapas.

La planta fue inaugurada el 27 de junio de 2026 y comenzó operaciones el 28 de junio de 2026. :contentReference[oaicite:1]{index=1}

Los siguientes parámetros de producción cuentan con respaldo oficial:

| Parámetro | Símbolo | Unidad | Valor | Procedencia | Estado |
|---|---|---|---:|---|---|
| Producción inicial reportada | \(C_{ini}\) | moscas/semana | 28,000,000 | Agricultura/SENASICA | Confirmado |
| Capacidad proyectada | \(C_{max}\) | moscas/semana | 100,000,000 | Agricultura/SENASICA | Confirmado |
| Posible capacidad futura | \(C_{fut}\) | moscas/semana | 120,000,000 | Agricultura/SENASICA | Referencia futura |

La producción de 28 millones de moscas estériles por semana fue reportada como la producción prevista para mediados de julio de 2026. La producción aumentaría gradualmente hasta alcanzar 100 millones de moscas estériles por semana a finales de 2026. Posteriormente se planteó analizar una posible ampliación a 120 millones semanales. :contentReference[oaicite:2]{index=2}

Por lo tanto, para el modelo:

\[
C_{ini}=28\,000\,000
\]

\[
C_{max}=100\,000\,000
\]

Mientras que:

\[
C_{fut}=120\,000\,000
\]

se mantendrá como escenario de expansión y no como capacidad operativa confirmada.

### 3.9.2 Ubicación de la planta

El origen de la producción de moscas estériles considerado en el proyecto será exclusivamente:

**Metapa de Domínguez, Chiapas, México.**

La planta cuenta con aproximadamente 3,000 m² de superficie, de los cuales alrededor de 2,000 m² corresponden a infraestructura de biocontención. :contentReference[oaicite:3]{index=3}

Estos datos se consideran información descriptiva de la infraestructura y no representan directamente parámetros de la dinámica poblacional.

### 3.9.3 Producción y esterilización en México

SENASICA confirmó que el primer ciclo de producción y esterilización de pupas estériles realizado en la planta de Metapa se completó el 24 de julio de 2026.

Posteriormente, el 27 de julio de 2026 se liberaron en el sur de Chihuahua las primeras 2.5 millones de moscas estériles producidas en la planta de Metapa. :contentReference[oaicite:4]{index=4}

Este dato permite confirmar que la producción de Metapa pasó de una capacidad proyectada a una operación efectiva durante 2026.

Por lo tanto:

| Parámetro | Símbolo | Unidad | Valor | Estado |
|---|---|---|---:|---|
| Primer lote liberado producido en Metapa | \(R_{obs}\) | moscas | 2,500,000 | Observado |

Este valor no deberá interpretarse como una tasa semanal de liberación ni como una cantidad óptima de liberación. Corresponde a un evento observado y podrá utilizarse principalmente para validación o comparación.

### 3.9.4 Proporción de referencia para la TIE

Agricultura señala que las liberaciones se realizan en zonas con baja densidad de la plaga y que se requieren al menos 10 machos estériles por cada mosca silvestre. :contentReference[oaicite:5]{index=5}

Por lo tanto, se establece:

\[
\rho_{ref}=10:1
\]

Este valor se clasificará como:

**Tipo:** referencia operativa.

No deberá considerarse como una constante biológica universal del GBG.

La proporción efectiva necesaria dependerá, entre otros factores, de la población silvestre, supervivencia y competitividad de los machos estériles y de la estrategia de liberación.

### 3.9.5 Técnica de control

La estrategia de control considerada para el proyecto es la Técnica del Insecto Estéril (TIE).

La estrategia consiste en utilizar machos estériles para interferir con la reproducción de la población silvestre mediante apareamientos que no producen descendencia viable.

Por lo tanto, el modelo deberá representar la interacción entre:

\[
M_w(t)
\]

machos silvestres,

y

\[
M_s(t)
\]

machos estériles.

La proporción entre ambos será:

\[
\rho_t=\frac{M_s(t)}{M_w(t)}
\]

### 3.9.6 Hospedadores considerados

El proyecto considera exclusivamente:

- bovinos;
- porcinos.

Los registros de animales infestados podrán utilizarse como información epidemiológica para representar o validar el comportamiento del modelo.

Sin embargo, no se establecerá una equivalencia directa entre:

\[
1\ animal\ infestado = X\ moscas
\]

sin contar con evidencia científica que permita realizar dicha conversión.

### 3.9.7 Parámetros biológicos confirmados

La literatura científica y técnica disponible permite confirmar determinadas características generales de la biología del GBG.

Entre ellas:

- la especie presenta un ciclo de vida con huevo, larva, pupa y adulto;
- las larvas se desarrollan en heridas de animales hospedadores;
- existen tres estadios larvarios;
- las hembras adultas se aparean y posteriormente depositan huevos en heridas;
- la duración del desarrollo depende de las condiciones ambientales.

Estos datos permiten establecer la estructura conceptual del modelo biológico.

Sin embargo, una característica biológica confirmada no necesariamente significa que ya se tenga un valor numérico listo para introducir en una ecuación.

Por ejemplo:

\[
\text{Existe desarrollo larvario}
\]

no implica que ya se haya establecido:

\[
d_L = X\ días
\]

para las condiciones específicas del modelo.

Los valores numéricos deberán documentarse individualmente.

### 3.9.8 Parámetros confirmados para utilizar directamente

La siguiente matriz resume los valores que actualmente pueden utilizarse directamente como referencias del proyecto:

| Parámetro | Símbolo | Valor | Unidad | Clasificación | Estado |
|---|---|---:|---|---|---|
| Producción inicial | \(C_{ini}\) | 28,000,000 | moscas/semana | PLANTA | Confirmado |
| Capacidad proyectada | \(C_{max}\) | 100,000,000 | moscas/semana | PLANTA | Confirmado |
| Capacidad futura | \(C_{fut}\) | 120,000,000 | moscas/semana | ESCENARIO | Referencia |
| Primer lote producido y liberado en México | \(R_{obs}\) | 2,500,000 | moscas | PLANTA/CONTROL | Observado |
| Proporción estéril:silvestre de referencia | \(\rho_{ref}\) | 10:1 | razón | TIE/CONTROL | Referencia operativa |

### 3.9.9 Parámetros confirmados sin valor numérico

Existen características del sistema que están confirmadas, pero cuyo valor numérico todavía no se incorporará al modelo.

Entre ellas:

- existencia de la planta de Metapa;
- producción de moscas estériles mediante cría y esterilización;
- utilización de irradiación para afectar la capacidad reproductiva;
- liberación de moscas estériles;
- utilización de la TIE como estrategia de control;
- presencia del GBG en bovinos y porcinos;
- relación entre la cantidad de machos estériles y la población silvestre;
- dependencia de la estrategia respecto a la densidad de la población silvestre.

Estos elementos forman parte de la estructura conceptual del modelo.

### 3.9.10 Diferencia entre confirmado y listo para el modelo

Un parámetro puede estar confirmado documentalmente y aun así requerir procesamiento antes de incorporarse a las ecuaciones.

Por ejemplo:

\[
C_{max}=100\,000\,000
\]

puede utilizarse directamente como capacidad semanal en un escenario.

En cambio, un dato epidemiológico de animales infestados podría requerir:

1. revisión temporal;
2. revisión geográfica;
3. depuración;
4. transformación;
5. estimación de la población de GBG;
6. incorporación al modelo.

Por lo tanto:

\[
Dato\ confirmado \neq Parámetro\ listo
\]

La incorporación definitiva dependerá de la estructura matemática y de la unidad requerida.

### 3.9.11 Regla de actualización

Los parámetros confirmados deberán actualizarse cuando se disponga de nueva información oficial o científica.

En particular, deberán revisarse periódicamente:

- producción real semanal de Metapa;
- capacidad efectiva de producción;
- cantidades realmente liberadas;
- distribución temporal de las liberaciones;
- información epidemiológica;
- nuevos estudios sobre la biología del GBG;
- nuevos estudios sobre la eficacia de la TIE.

Cuando un nuevo dato oficial sustituya a una proyección anterior, deberá conservarse el valor anterior como antecedente y registrarse el nuevo valor como dato actualizado.

### 3.9.12 Estado actual de los parámetros

El estado general de los parámetros del proyecto se resume de la siguiente manera:

**Confirmados:**

- ubicación y existencia de la planta de Metapa;
- producción inicial reportada;
- capacidad proyectada;
- primer lote producido y liberado en México;
- referencia operativa de 10:1;
- estrategia de control mediante TIE;
- hospedadores considerados.

**Pendientes de cuantificación:**

- población inicial de GBG;
- mortalidad de adultos;
- supervivencia de adultos;
- fecundidad efectiva;
- supervivencia de estadios inmaduros;
- competitividad de machos estériles;
- supervivencia de machos estériles después de la liberación;
- frecuencia óptima de liberación;
- cantidad óptima de liberación;
- criterio cuantitativo de control;
- criterio cuantitativo de erradicación.

Estos parámetros pendientes deberán investigarse antes de realizar simulaciones definitivas.

## 3.10 Parámetros pendientes

Los parámetros pendientes corresponden a valores necesarios para completar la formulación y calibración del modelo, pero para los cuales todavía no se cuenta con información suficiente, específica o directamente aplicable al contexto del proyecto.

La existencia de un parámetro pendiente no significa que no exista información científica sobre el tema. Significa que todavía es necesario localizar, evaluar y seleccionar el valor o rango que pueda utilizarse de manera justificada dentro del modelo.

Los parámetros pendientes deberán investigarse antes de considerar definitiva la simulación.

### 3.10.1 Parámetros biológicos pendientes

Los principales parámetros biológicos pendientes son aquellos relacionados con el desarrollo, reproducción y supervivencia del GBG.

| Parámetro | Símbolo | Unidad | Estado | Acción requerida |
|---|---|---|---|---|
| Duración del desarrollo larvario | \(d_L\) | días | Pendiente | Buscar valor o rango científicamente respaldado |
| Duración del estado pupal | \(d_P\) | días | Pendiente | Buscar valor o rango |
| Duración del estado adulto | \(d_A\) | días | Pendiente | Buscar valor o rango |
| Duración del desarrollo embrionario | \(d_E\) | días | Pendiente | Buscar valor o rango |
| Fecundidad efectiva | \(b\) | huevos/hembra | Pendiente | Determinar valor representativo |
| Proporción sexual | \(r\) | proporción | Pendiente | Determinar proporción de machos y hembras |
| Mortalidad de machos silvestres | \(\mu_M\) | 1/día | Pendiente | Determinar valor o rango |
| Mortalidad de hembras | \(\mu_F\) | 1/día | Pendiente | Determinar valor o rango |
| Supervivencia larvaria | \(S_L\) | proporción | Pendiente | Determinar valor o rango |
| Supervivencia pupal | \(S_P\) | proporción | Pendiente | Determinar valor o rango |
| Supervivencia adulta | \(S_A\) | proporción | Pendiente | Determinar valor o rango |

Los valores deberán seleccionarse considerando, cuando sea posible, las condiciones biológicas del GBG y no únicamente datos de otras especies de moscas.

### 3.10.2 Parámetros reproductivos pendientes

La reproducción constituye uno de los componentes centrales del modelo debido a que la TIE busca reducir la reproducción de la población silvestre.

Se encuentran pendientes:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Tasa reproductiva | \(\beta\) | individuos/tiempo | Pendiente |
| Probabilidad de apareamiento | \(p_m\) | proporción | Pendiente |
| Fecundidad efectiva | \(b\) | huevos/hembra | Pendiente |
| Proporción de hembras apareadas | \(p_f\) | proporción | Pendiente |
| Mortalidad de hembras | \(\mu_F\) | 1/tiempo | Pendiente |

Estos parámetros deberán analizarse conjuntamente, ya que no todos necesariamente serán necesarios en la formulación final.

La estructura definitiva dependerá del tipo de modelo seleccionado.

### 3.10.3 Parámetros de la TIE pendientes

La eficacia de la Técnica del Insecto Estéril depende de características de los machos liberados y de su interacción con la población silvestre.

Los principales parámetros pendientes son:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Supervivencia de machos estériles | \(S_s\) | proporción | Pendiente |
| Mortalidad de machos estériles | \(\mu_s\) | 1/tiempo | Pendiente |
| Competitividad relativa | \(c\) | adimensional | Pendiente |
| Eficacia de esterilización | \(E_s\) | proporción | Pendiente |
| Proporción efectiva de apareamientos estériles | \(p_s\) | proporción | Calculado |
| Proporción de apareamientos fértiles | \(p_w\) | proporción | Calculado |

La proporción de apareamientos con machos estériles podrá calcularse conceptualmente mediante:

\[
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
\]

donde:

- \(M_s(t)\) = machos estériles;
- \(M_w(t)\) = machos silvestres;
- \(c\) = competitividad relativa de los machos estériles.

Sin embargo, el valor de \(c\) deberá ser determinado mediante evidencia científica antes de utilizar la ecuación para una simulación definitiva.

### 3.10.4 Parámetros epidemiológicos pendientes

Los parámetros epidemiológicos permitirán relacionar la dinámica de la población de GBG con los hospedadores considerados en el proyecto.

Se encuentran pendientes:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Población bovina considerada | \(B\) | animales | Pendiente |
| Población porcina considerada | \(P\) | animales | Pendiente |
| Bovinos infestados | \(I_b\) | animales | Pendiente/variable |
| Porcinos infestados | \(I_p\) | animales | Pendiente/variable |
| Tasa de infestación bovina | \(\lambda_b\) | 1/tiempo | Pendiente |
| Tasa de infestación porcina | \(\lambda_p\) | 1/tiempo | Pendiente |
| Probabilidad de infestación bovina | \(p_b\) | proporción | Pendiente |
| Probabilidad de infestación porcina | \(p_p\) | proporción | Pendiente |
| Tasa de recuperación bovina | \(\gamma_b\) | 1/tiempo | Pendiente |
| Tasa de recuperación porcina | \(\gamma_p\) | 1/tiempo | Pendiente |

Estos parámetros deberán analizarse con especial cuidado porque la infestación por GBG no debe tratarse automáticamente como una enfermedad de transmisión directa entre animales.

Las hembras adultas depositan huevos en heridas de los hospedadores, por lo que la relación entre la población de moscas y los casos en animales deberá establecerse mediante una formulación biológicamente justificada.

### 3.10.5 Población inicial de GBG

Uno de los parámetros más importantes que permanece pendiente es la población inicial de GBG:

\[
N_0
\]

El modelo necesita conocer o estimar la condición inicial de la población antes de iniciar la estrategia de liberación.

Sin embargo, el número de animales infestados no deberá convertirse directamente en un número de moscas mediante una relación arbitraria.

Se deberá investigar una metodología que permita:

1. utilizar datos de vigilancia;
2. relacionarlos con la dinámica de GBG;
3. estimar la población silvestre;
4. definir condiciones iniciales razonables;
5. expresar la incertidumbre de la estimación.

Si no es posible obtener una estimación directa, podrán construirse diferentes escenarios de población inicial.

### 3.10.6 Parámetros de producción pendientes

Aunque la capacidad general de la planta está documentada, todavía pueden ser necesarios parámetros adicionales para representar con mayor precisión la disponibilidad de moscas.

Entre ellos:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Producción real semanal | \(C_t\) | moscas/semana | Pendiente/variable |
| Porcentaje de machos | \(r_M\) | proporción | Pendiente |
| Pérdidas durante producción | \(L_P\) | proporción | Pendiente |
| Pérdidas durante preparación | \(L_A\) | proporción | Pendiente |
| Pérdidas antes de liberación | \(L_R\) | proporción | Pendiente |
| Cantidad efectivamente disponible | \(A_t\) | moscas/periodo | Pendiente |
| Cantidad efectivamente liberada | \(R_t\) | moscas/periodo | Variable |

Estos parámetros permitirán diferenciar entre:

\[
Producción
\neq
Disponibilidad
\neq
Liberación
\]

Esta diferencia es importante porque el modelo debe representar la capacidad real de la planta y no asumir que toda mosca producida termina necesariamente liberada.

### 3.10.7 Parámetros de control pendientes

También deberán determinarse:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Frecuencia de liberación | \(f_R\) | liberaciones/periodo | Pendiente |
| Intervalo de liberación | \(\Delta t_R\) | días/semanas | Pendiente |
| Cantidad óptima por liberación | \(R_t\) | moscas/periodo | Calculado/variable |
| Duración de la estrategia | \(T_R\) | semanas/meses | Variable |
| Nivel de control | \(N_C\) | individuos | Pendiente |
| Umbral de erradicación | \(N_E\) | individuos | Pendiente |

Estos valores no deberán establecerse únicamente por conveniencia computacional.

Deberán estar sustentados por evidencia científica, criterios epidemiológicos, criterios operativos o una metodología explícita de construcción de escenarios.

### 3.10.8 Parámetros ambientales pendientes

La dinámica del GBG está influenciada por condiciones ambientales, especialmente temperatura y humedad.

Sin embargo, antes de incluir variables ambientales en el modelo nacional deberá determinarse si existe suficiente información espacial y temporal para hacerlo de manera consistente.

Los posibles parámetros incluyen:

| Parámetro | Símbolo | Unidad | Estado |
|---|---|---|---|
| Temperatura | \(T\) | °C | Pendiente |
| Humedad relativa | \(H\) | % | Pendiente |
| Efecto de temperatura sobre desarrollo | \(f_T\) | función | Pendiente |
| Efecto ambiental sobre supervivencia | \(f_E\) | función | Pendiente |

Estos parámetros no se incorporarán automáticamente.

Primero deberá determinarse si el modelo utilizará:

- condiciones ambientales constantes;
- valores promedio;
- escenarios ambientales;
- datos espaciales;
- datos temporales.

La decisión dependerá de la disponibilidad y calidad de la información.

### 3.10.9 Parámetros de dispersión pendientes

Si el modelo incorpora posteriormente un componente espacial, deberán investigarse parámetros relacionados con la dispersión de adultos.

Entre ellos:

- distancia de dispersión;
- velocidad o patrón de desplazamiento;
- distribución espacial;
- conectividad entre áreas;
- efecto de barreras geográficas.

Estos parámetros se consideran fuera de la primera formulación si no existe información suficiente.

Por lo tanto, inicialmente se podrá trabajar con un modelo poblacional agregado.

### 3.10.10 Criterio para cerrar un parámetro pendiente

Un parámetro pendiente podrá considerarse listo para incorporarse al modelo cuando se cumplan las siguientes condiciones:

1. Se conoce qué representa.
2. Tiene una unidad definida.
3. Existe un valor o rango.
4. Se conoce su fuente.
5. Se conoce la población o condiciones donde fue estimado.
6. Se ha evaluado su aplicabilidad al modelo.
7. Se conoce su nivel de incertidumbre.
8. Se ha documentado cómo será utilizado en las ecuaciones.

Si alguna de estas condiciones no se cumple, el parámetro deberá permanecer identificado como pendiente, estimado o supuesto.

### 3.10.11 Priorización de la investigación

No todos los parámetros pendientes tendrán la misma prioridad.

Se propone la siguiente clasificación:

#### Prioridad alta

Parámetros necesarios para que el modelo pueda representar la dinámica básica de la población:

- \(N_0\): población inicial;
- \(b\): fecundidad;
- \(\mu_M\): mortalidad de machos;
- \(\mu_F\): mortalidad de hembras;
- \(c\): competitividad de machos estériles;
- \(S_s\): supervivencia de machos estériles;
- \(E_s\): eficacia de esterilización.

#### Prioridad media

Parámetros necesarios para mejorar el realismo del modelo:

- \(d_L\): duración larvaria;
- \(d_P\): duración pupal;
- \(S_L\): supervivencia larvaria;
- \(S_P\): supervivencia pupal;
- proporción sexual;
- frecuencia de liberación;
- pérdidas antes de liberación.

#### Prioridad baja o posterior

Parámetros que podrán incorporarse en versiones posteriores:

- dispersión espacial;
- variables ambientales detalladas;
- heterogeneidad regional;
- efectos espaciales;
- variaciones temporales complejas.

### 3.10.12 Estado actual

El estado de los parámetros pendientes será actualizado conforme avance la investigación.

La clasificación inicial será:

**Pendientes de investigación científica:**

- fecundidad;
- mortalidad;
- supervivencia;
- competitividad;
- eficacia de esterilización;
- desarrollo por etapas;
- proporción sexual.

**Pendientes de información epidemiológica:**

- población inicial;
- distribución de casos;
- tasas de infestación;
- relación entre casos en hospedadores y población de GBG.

**Pendientes de información operativa:**

- producción real semanal;
- proporción de machos;
- pérdidas;
- disponibilidad efectiva;
- frecuencia real de liberación.

**Pendientes de definición metodológica:**

- criterio de control;
- criterio de erradicación;
- escala temporal;
- escala espacial;
- estructura definitiva del modelo.

Estos parámetros no deberán ser sustituidos por valores arbitrarios. En caso de no encontrar un valor único, se utilizarán rangos o escenarios y se documentará la incertidumbre correspondiente.

## 3.11 Matriz maestra de parámetros

La matriz maestra de parámetros concentra los valores, variables y referencias que serán utilizados durante el desarrollo del modelo matemático y computacional.

Su finalidad es mantener un registro único y organizado de los parámetros utilizados en el proyecto, evitando duplicidad de información y permitiendo identificar cuáles valores están confirmados, cuáles requieren investigación y cuáles serán definidos mediante escenarios.

La matriz será actualizada conforme avance la investigación y se incorporen nuevas fuentes de información.

### 3.11.1 Estructura de la matriz

Cada parámetro deberá registrarse con los siguientes campos:

| Campo | Descripción |
|---|---|
| Parámetro | Nombre descriptivo |
| Símbolo | Símbolo utilizado en el modelo |
| Unidad | Unidad de medida |
| Valor | Valor o rango utilizado |
| Categoría | PLANTA, BIOLÓGICO, TIE, EPIDEMIOLÓGICO, CONTROL o ESCENARIO |
| Tipo | OBSERVADO, CONFIRMADO, ESTIMADO, SUPUESTO, ESCENARIO o CALCULADO |
| Fuente | Documento o institución de procedencia |
| Confianza | Alta, media o baja |
| Estado | Confirmado, pendiente o calculado |
| Observaciones | Información adicional |

### 3.11.2 Matriz maestra actual

| Parámetro | Símbolo | Unidad | Valor | Categoría | Tipo | Estado |
|---|---|---|---:|---|---|---|
| Producción inicial reportada | \(C_{ini}\) | moscas/semana | 28,000,000 | PLANTA | CONFIRMADO | Confirmado |
| Capacidad proyectada | \(C_{max}\) | moscas/semana | 100,000,000 | PLANTA | CONFIRMADO | Confirmado |
| Capacidad futura | \(C_{fut}\) | moscas/semana | 120,000,000 | ESCENARIO | ESCENARIO | Escenario |
| Producción durante el periodo | \(C_t\) | moscas/periodo | Variable | PLANTA | VARIABLE | Pendiente |
| Moscas disponibles | \(A_t\) | moscas/periodo | Variable | CONTROL | CALCULADO | Pendiente |
| Moscas liberadas | \(R_t\) | moscas/periodo | Variable | CONTROL | VARIABLE | Pendiente |
| Intervalo de liberación | \(\Delta t_R\) | días/semanas | TBD | CONTROL | PENDIENTE | Pendiente |
| Frecuencia de liberación | \(f_R\) | liberaciones/periodo | TBD | CONTROL | PENDIENTE | Pendiente |
| Duración de liberación | \(T_R\) | semanas/meses | Variable | CONTROL | ESCENARIO | Pendiente |
| Proporción estéril:silvestre | \(\rho_t\) | razón | Variable | TIE | CALCULADO | Pendiente |
| Proporción de referencia | \(\rho_{ref}\) | razón | 10:1 | TIE | REFERENCIA | Confirmado |
| Población inicial de GBG | \(N_0\) | individuos | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Nivel inicial de infestación | \(I_0\) | indicador | TBD | EPIDEMIOLÓGICO | ESCENARIO | Pendiente |
| Duración larvaria | \(d_L\) | días | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Duración pupal | \(d_P\) | días | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Duración adulta | \(d_A\) | días | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Desarrollo embrionario | \(d_E\) | días | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Fecundidad | \(b\) | huevos/hembra | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Proporción sexual | \(r\) | proporción | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Mortalidad de machos silvestres | \(\mu_M\) | 1/tiempo | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Mortalidad de hembras | \(\mu_F\) | 1/tiempo | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Supervivencia larvaria | \(S_L\) | proporción | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Supervivencia pupal | \(S_P\) | proporción | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Supervivencia adulta | \(S_A\) | proporción | TBD | BIOLÓGICO | PENDIENTE | Pendiente |
| Supervivencia de machos estériles | \(S_s\) | proporción | TBD | TIE | PENDIENTE | Pendiente |
| Mortalidad de machos estériles | \(\mu_s\) | 1/tiempo | TBD | TIE | PENDIENTE | Pendiente |
| Competitividad relativa | \(c\) | adimensional | TBD | TIE | PENDIENTE | Pendiente |
| Eficacia de esterilización | \(E_s\) | proporción | TBD | TIE | PENDIENTE | Pendiente |
| Probabilidad de apareamiento estéril | \(p_s\) | proporción | Calculado | TIE | CALCULADO | Pendiente |
| Probabilidad de apareamiento silvestre | \(p_w\) | proporción | Calculado | TIE | CALCULADO | Pendiente |
| Población bovina | \(B\) | animales | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Población porcina | \(P\) | animales | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Bovinos infestados | \(I_b\) | animales | Variable | EPIDEMIOLÓGICO | VARIABLE | Pendiente |
| Porcinos infestados | \(I_p\) | animales | Variable | EPIDEMIOLÓGICO | VARIABLE | Pendiente |
| Tasa de infestación bovina | \(\lambda_b\) | 1/tiempo | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Tasa de infestación porcina | \(\lambda_p\) | 1/tiempo | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Probabilidad de infestación bovina | \(p_b\) | proporción | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Probabilidad de infestación porcina | \(p_p\) | proporción | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Tasa de recuperación bovina | \(\gamma_b\) | 1/tiempo | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Tasa de recuperación porcina | \(\gamma_p\) | 1/tiempo | TBD | EPIDEMIOLÓGICO | PENDIENTE | Pendiente |
| Nivel de control | \(N_C\) | individuos | TBD | CONTROL | PENDIENTE | Pendiente |
| Umbral de erradicación | \(N_E\) | individuos | TBD | CONTROL | PENDIENTE | Pendiente |
| Tiempo para alcanzar el objetivo | \(T_E\) | semanas/meses | Calculado | RESULTADO | CALCULADO | Pendiente |
| Cantidad total liberada | \(R_{total}\) | moscas | Calculado | RESULTADO | CALCULADO | Pendiente |
| Utilización de capacidad | \(U_C\) | proporción | Calculado | RESULTADO | CALCULADO | Pendiente |

### 3.11.3 Parámetros confirmados

Actualmente se consideran respaldados para el proyecto los siguientes valores:

| Parámetro | Símbolo | Valor | Unidad | Procedencia |
|---|---|---:|---|---|
| Producción inicial reportada | \(C_{ini}\) | 28,000,000 | moscas/semana | SENASICA / Agricultura |
| Capacidad proyectada | \(C_{max}\) | 100,000,000 | moscas/semana | SENASICA / Agricultura |
| Capacidad futura considerada | \(C_{fut}\) | 120,000,000 | moscas/semana | SENASICA / Agricultura |
| Referencia estéril:silvestre | \(\rho_{ref}\) | 10:1 | razón | Agricultura / SENASICA |
| Primer lote producido en Metapa y liberado | \(R_{obs}\) | 2,500,000 | moscas | SENASICA |

Los valores de 28 y 100 millones corresponden a condiciones de producción reportadas para la planta, mientras que 120 millones corresponde a una posible expansión y deberá mantenerse identificado como escenario futuro.

El lote de 2.5 millones corresponde a un evento observado y no deberá utilizarse como capacidad semanal.

### 3.11.4 Parámetros pendientes de investigación

Los parámetros que requieren investigación antes de cerrar el modelo incluyen principalmente:

#### Biología

- \(d_L\): duración larvaria;
- \(d_P\): duración pupal;
- \(d_A\): duración adulta;
- \(d_E\): duración embrionaria;
- \(b\): fecundidad;
- \(r\): proporción sexual;
- \(\mu_M\): mortalidad de machos;
- \(\mu_F\): mortalidad de hembras;
- \(S_L\): supervivencia larvaria;
- \(S_P\): supervivencia pupal;
- \(S_A\): supervivencia adulta.

#### TIE

- \(S_s\): supervivencia de machos estériles;
- \(\mu_s\): mortalidad de machos estériles;
- \(c\): competitividad relativa;
- \(E_s\): eficacia de esterilización.

#### Epidemiología

- \(N_0\): población inicial;
- \(B\): población bovina;
- \(P\): población porcina;
- \(I_b\): bovinos infestados;
- \(I_p\): porcinos infestados;
- \(\lambda_b\): tasa de infestación bovina;
- \(\lambda_p\): tasa de infestación porcina;
- \(p_b\): probabilidad de infestación bovina;
- \(p_p\): probabilidad de infestación porcina.

#### Control

- \(f_R\): frecuencia de liberación;
- \(\Delta t_R\): intervalo de liberación;
- \(T_R\): duración de la estrategia;
- \(N_C\): nivel objetivo de control;
- \(N_E\): criterio de erradicación.

### 3.11.5 Parámetros calculados

Algunos valores no deberán introducirse directamente como datos, debido a que serán calculados por el modelo.

Por ejemplo:

\[
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
\]

\[
p_w(t)=1-p_s(t)
\]

\[
\rho_t=\frac{M_s(t)}{M_w(t)}
\]

Además, una vez ejecutada una simulación se podrán obtener:

\[
T_E
\]

\[
R_{total}=\sum_t R_t
\]

y

\[
U_C=
\frac{\sum_tR_t}
{\sum_tC_t}
\]

Estos resultados dependerán de los parámetros de entrada y de las ecuaciones utilizadas.

### 3.11.6 Reglas de actualización de la matriz

La matriz maestra deberá mantenerse actualizada durante todo el desarrollo del proyecto.

Cuando se encuentre nueva información:

1. Se identificará el parámetro correspondiente.
2. Se registrará la nueva fuente.
3. Se verificará la unidad.
4. Se evaluará la aplicabilidad del valor.
5. Se asignará un nivel de confianza.
6. Se determinará si sustituye o complementa el valor anterior.
7. Se actualizará el estado del parámetro.
8. Se documentará cualquier cambio relevante.

No deberán eliminarse valores anteriores sin conservar su antecedente.

### 3.11.7 Regla de trazabilidad

Todo valor utilizado en una simulación deberá poder relacionarse con:

\[
Fuente
\rightarrow
Parámetro
\rightarrow
Ecuación
\rightarrow
Resultado
\]

Esto permitirá reproducir las simulaciones y justificar los resultados obtenidos.

### 3.11.8 Relación con la implementación computacional

La matriz maestra será utilizada posteriormente como referencia para definir los parámetros de entrada del programa.

Conceptualmente, los parámetros podrán organizarse en Python de acuerdo con su categoría:

```text
parametros/
│
├── planta
├── biologicos
├── tie
├── epidemiologicos
├── control
└── escenarios