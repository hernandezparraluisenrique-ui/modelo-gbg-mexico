# 2. Caracterización de la planta de producción de Metapa

## 2.1 Identificación y ubicación de la planta

La planta considerada en este proyecto es la Planta de Producción de Moscas Estériles de Gusano Barrenador del Ganado (GBG), ubicada en Metapa de Domínguez, Chiapas, México.

La instalación fue inaugurada el 27 de junio de 2026 y comenzó operaciones el 28 de junio del mismo año. Cuenta con una superficie aproximada de 3,000 m², de los cuales alrededor de 2,000 m² corresponden a infraestructura de biocontención.

La planta fue desarrollada para producir moscas estériles de *Cochliomyia hominivorax* y fortalecer las acciones de prevención, control y erradicación del gusano barrenador del ganado en México.

## 2.2 Función de la planta dentro del proyecto

La planta de producción de Metapa de Domínguez será considerada dentro del modelo como el componente encargado de proporcionar las moscas estériles necesarias para las estrategias de control mediante la Técnica del Insecto Estéril.

Su función dentro del proyecto será representar la disponibilidad de moscas estériles que pueden ser utilizadas para las liberaciones, de acuerdo con la capacidad productiva y las condiciones de operación documentadas para la planta.

La producción disponible será utilizada como una restricción del modelo, de manera que la cantidad de moscas estériles asignada a una estrategia de liberación no pueda superar la cantidad disponible durante el periodo correspondiente.

De esta forma, el modelo integrará el componente de producción de la planta con la dinámica de la población silvestre de *Cochliomyia hominivorax*, permitiendo evaluar estrategias de liberación bajo condiciones de disponibilidad realista de moscas estériles.

## 2.3 Proceso de producción

La planta de Metapa de Domínguez reproduce las diferentes etapas del ciclo biológico del gusano barrenador del ganado con el propósito de obtener insectos destinados a la aplicación de la Técnica del Insecto Estéril.

De manera general, el proceso comprende las siguientes etapas:

1. Cría y desarrollo de las fases inmaduras del gusano barrenador bajo condiciones controladas.
2. Desarrollo larvario mediante el suministro de una dieta formulada para el crecimiento de las larvas.
3. Obtención de larvas maduras y preparación para la etapa de pupación.
4. Formación y desarrollo de las pupas en condiciones controladas.
5. Irradiación de las pupas mediante Cobalto-60 para afectar su capacidad reproductiva.
6. Preparación de las pupas irradiadas para su traslado a los sitios donde se realizará la emergencia de los adultos.
7. Emergencia de las moscas adultas y suministro de alimento y agua durante su preparación.
8. Enfriamiento, empaquetado y preparación de los insectos para su posterior liberación.

El proceso productivo será representado en el proyecto como una cadena de etapas que permite relacionar la producción de la planta con la cantidad de moscas estériles disponibles para las estrategias de liberación.

Los tiempos de desarrollo, tasas de supervivencia, pérdidas y demás características cuantitativas de cada etapa serán determinados posteriormente a partir de información oficial y literatura científica disponible. No se asignarán valores numéricos sin una fuente que los respalde.

## 2.4 Cría y desarrollo larvario

La etapa de cría y desarrollo larvario constituye una parte fundamental del proceso de producción de la planta de Metapa de Domínguez. Durante esta etapa se mantienen condiciones ambientales controladas con el propósito de reproducir las condiciones necesarias para el desarrollo del gusano barrenador del ganado.

La planta cuenta con sistemas para controlar variables ambientales como la temperatura y la humedad. De acuerdo con la información oficial de SENASICA, en algunos espacios estratégicos de la instalación se pueden alcanzar temperaturas de hasta 39 °C y una humedad ambiental de aproximadamente 80 %.

La alimentación de las larvas se realiza mediante una dieta formulada a partir de plasma, hemoglobina, huevo y leche. Esta dieta permite proporcionar los componentes necesarios para el desarrollo de las larvas bajo las condiciones controladas de la planta.

Una vez que las larvas alcanzan la madurez, son trasladadas a cámaras especiales en las que se simula su caída al suelo, reproduciendo la condición natural que precede a la formación de las pupas.

Para el modelo matemático, esta etapa será considerada como parte del proceso de producción que determina la cantidad de individuos que pueden avanzar hacia la fase de pupa. Los tiempos de desarrollo, tasas de supervivencia, rendimiento y posibles pérdidas durante esta etapa deberán determinarse posteriormente mediante información científica y datos de producción disponibles.

No se asignarán valores numéricos de rendimiento o supervivencia a esta etapa hasta contar con una fuente que los respalde.

## 2.5 Formación de pupas

Después de alcanzar la madurez, las larvas son trasladadas a cámaras en las que se simula la condición natural de caída al suelo. Esta etapa permite que las larvas completen su transición hacia la fase de pupa dentro del proceso controlado de producción de la planta de Metapa de Domínguez.

La formación de pupas constituye una etapa intermedia entre el desarrollo larvario y la esterilización. Una vez obtenidas, las pupas continúan dentro del proceso de producción hasta llegar a la etapa de irradiación.

Para efectos del modelo, esta etapa permitirá establecer la cantidad de individuos que avanzan desde la fase larvaria hacia la fase de pupa y, posteriormente, hacia la esterilización. Los tiempos de desarrollo y las tasas de supervivencia o rendimiento correspondientes serán determinados posteriormente a partir de información científica o datos de producción disponibles.

No se establecerán valores numéricos de supervivencia, rendimiento o duración de esta etapa sin contar previamente con una fuente que los respalde.

## 2.6 Esterilización mediante irradiación

Una vez obtenidas las pupas, estas son sometidas a un proceso de irradiación con el propósito de afectar su capacidad reproductiva y obtener insectos estériles para su utilización en la Técnica del Insecto Estéril.

De acuerdo con la información oficial sobre la planta de Metapa de Domínguez, la irradiación se realiza mediante Cobalto-60. El tratamiento busca impedir que los insectos puedan producir descendencia viable después del apareamiento, manteniendo al mismo tiempo las funciones necesarias para que los machos puedan sobrevivir, emerger y participar en la competencia reproductiva con los machos silvestres.

La irradiación constituye, por lo tanto, una etapa fundamental del proceso de producción, ya que permite transformar las pupas obtenidas durante la cría en material destinado a la obtención de moscas estériles.

Para efectos del modelo matemático, esta etapa será representada como parte del proceso de transformación de la producción de la planta. La cantidad de pupas que ingresan al proceso de irradiación y la cantidad que posteriormente se encuentra disponible para las etapas de emergencia y liberación podrán utilizarse para determinar el rendimiento de producción de moscas estériles.

La información oficial de la planta reporta una dosis de irradiación de entre 55 y 70 Gy mediante Cobalto-60. Este intervalo será registrado como un parámetro documentado del proceso de esterilización, pero no se asumirá inicialmente que toda la producción recibe exactamente la misma dosis.

Los parámetros relacionados con supervivencia después de la irradiación, proporción de machos obtenidos, emergencia de adultos y eficacia de la esterilización serán incorporados posteriormente únicamente cuando se disponga de información científica o datos de producción que permitan sustentarlos.

## 2.7 Preparación de las moscas para liberación

Después del proceso de irradiación, las pupas son trasladadas a centros de empaque, donde continúa el proceso de preparación de las moscas estériles para su posterior liberación en campo.

En estos centros se produce la emergencia de los adultos a partir de las pupas irradiadas. Una vez que las moscas emergen, reciben alimento y agua durante el periodo de preparación, con el propósito de que lleguen en condiciones adecuadas al momento de su liberación. De acuerdo con la información oficial de SENASICA, la preparación busca que, al ser liberadas, las moscas tengan como principal necesidad biológica el apareamiento.

Horas antes de la liberación, las moscas son trasladadas a cuartos fríos para provocar un estado de aletargamiento temporal. Este procedimiento facilita su manipulación y permite su colocación en cajas especiales destinadas al transporte y dispersión en campo.

Las cajas son posteriormente preparadas para su traslado en aeronaves encargadas de realizar la liberación de las moscas estériles en las zonas seleccionadas.

Para efectos del modelo matemático, esta etapa representa la transición entre la producción de moscas estériles y su disponibilidad efectiva para las estrategias de liberación. Por ello, posteriormente será necesario determinar si existen datos suficientes para representar pérdidas, proporción de adultos emergidos y disponibilidad efectiva para liberación.

No se asignarán valores numéricos de emergencia, supervivencia, pérdidas durante el empaque o disponibilidad efectiva hasta contar con información oficial o científica que permita sustentarlos.

## 2.8 Capacidad de producción

La capacidad de producción de la planta de Metapa de Domínguez constituye una de las principales restricciones que deberán considerarse en el modelo matemático, debido a que determina la cantidad máxima de moscas estériles que puede estar disponible para las estrategias de liberación.

De acuerdo con información oficial del Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria (SENASICA), la planta inició operaciones el 28 de junio de 2026 y fue diseñada para incrementar progresivamente su producción. Para mediados de julio de 2026 se contemplaba alcanzar una producción de aproximadamente 28 millones de moscas estériles por semana.

La producción deberá incrementarse gradualmente hasta alcanzar una capacidad proyectada de 100 millones de moscas estériles por semana hacia finales de 2026. Una vez alcanzada esta capacidad, SENASICA contempla analizar la posibilidad de ampliar la producción hasta 120 millones de moscas estériles semanales.

Para el modelo, la capacidad de producción no se considerará inicialmente como un valor constante, debido a que durante el periodo de puesta en operación de la planta existe un incremento progresivo de la producción. Por esta razón, se podrá representar mediante una función dependiente del tiempo o mediante una serie de valores correspondientes a diferentes periodos de producción.

De manera conceptual, la cantidad de moscas estériles que pueden asignarse a una estrategia de liberación deberá cumplir la restricción:

$$
R_t \leq C_t
$$

donde:

* \(R_t\) representa la cantidad de moscas estériles destinadas a la liberación durante el periodo \(t\).
* \(C_t\) representa la cantidad de moscas estériles disponibles de acuerdo con la capacidad de producción de la planta durante el periodo \(t\).

Como referencia inicial para la parametrización del modelo, se considerarán los siguientes valores documentados:

| Periodo                   | Producción semanal reportada o proyectada |
| ------------------------- | ----------------------------------------: |
| Mediados de julio de 2026 |           28 millones de moscas estériles |
| Finales de 2026           |          100 millones de moscas estériles |
| Posible ampliación futura |    Hasta 120 millones de moscas estériles |

Estos valores deberán diferenciarse entre producción observada y capacidad proyectada. Para las simulaciones que requieran representar la producción real de la planta, se priorizarán los registros oficiales de producción publicados por SENASICA.

La información semanal de producción podrá utilizarse posteriormente para construir una serie temporal de disponibilidad de moscas estériles y mejorar la representación de la capacidad real de la planta dentro del modelo.

No se utilizará la capacidad de producción de otras plantas como fuente de suministro para las simulaciones de este proyecto.

## 2.9 Disponibilidad de moscas para las estrategias de liberación

La disponibilidad de moscas estériles para las estrategias de control dependerá de la producción de la planta de Metapa de Domínguez y de la cantidad que pueda ser destinada efectivamente a las zonas de liberación durante cada periodo.

La cantidad producida por la planta no será considerada automáticamente como cantidad disponible para una estrategia específica. El modelo deberá distinguir entre la producción de moscas estériles y la cantidad que puede ser asignada o liberada en un periodo determinado.

Esta distinción permitirá representar de manera más realista la operación de las estrategias de control, ya que una parte de la producción puede ser destinada a diferentes zonas de intervención de acuerdo con las necesidades de control establecidas por las autoridades sanitarias.

Como referencia de la operación real, SENASICA reportó que entre el 26 de julio y el 21 de agosto de 2026 se liberaron 40.4 millones de moscas estériles en 14 municipios de Chihuahua, de las cuales 38.7 millones provinieron de la planta de Metapa de Domínguez, Chiapas. Estos datos muestran que la producción de Metapa puede relacionarse directamente con las cantidades destinadas a las estrategias de liberación, aunque ambas variables deben mantenerse diferenciadas dentro del modelo.

Para efectos de la simulación, se definirá una variable de disponibilidad de moscas estériles para cada periodo:

$$
A_t = \text{cantidad de moscas estériles disponibles para liberación en el periodo } t
$$

La cantidad efectivamente liberada se representará mediante:

$$
R_t \leq A_t
$$

donde:

* \(A_t\) representa la cantidad de moscas estériles disponibles para una estrategia durante el periodo \(t\).
* \(R_t\) representa la cantidad de moscas estériles que el modelo asigna a la liberación durante ese periodo.

La disponibilidad podrá depender de la producción registrada por la planta, de las cantidades destinadas a las diferentes estrategias y de otros factores operativos que puedan ser documentados posteriormente.

En una primera versión del modelo, cuando no existan datos suficientes para representar pérdidas o restricciones operativas adicionales, se podrá considerar que la cantidad disponible corresponde a la producción destinada a la estrategia evaluada. Esta condición deberá identificarse como un supuesto del escenario y podrá modificarse posteriormente.

Para la parametrización del modelo se priorizarán los registros oficiales de producción publicados por SENASICA, así como los datos oficiales de liberación disponibles. Estos registros permitirán construir una representación temporal de la disponibilidad de moscas estériles producidas en Metapa.

No se incorporará como fuente de suministro la producción de otras plantas. Las cantidades provenientes de instalaciones diferentes a Metapa podrán aparecer únicamente en registros oficiales utilizados para distinguirlas de la producción mexicana, pero no serán consideradas dentro de la capacidad disponible para las simulaciones del proyecto.

## 2.10 Restricciones de producción consideradas en el modelo

La capacidad de producción de la planta de Metapa de Domínguez será incorporada al modelo como una restricción sobre la cantidad de moscas estériles que pueden estar disponibles para las estrategias de liberación.

Esta restricción permitirá evitar que una simulación considere cantidades de moscas estériles superiores a las que pueden ser proporcionadas por la planta durante un periodo determinado.

La producción de la planta deberá representarse de acuerdo con el periodo de operación correspondiente. De acuerdo con SENASICA, la planta inició operaciones el 28 de junio de 2026 y se estableció un incremento progresivo de la producción, desde aproximadamente 28 millones de moscas estériles por semana a mediados de julio hasta alcanzar una capacidad proyectada de 100 millones de moscas estériles por semana hacia finales de 2026.

Por lo tanto, la capacidad disponible será representada mediante una variable dependiente del tiempo:

$$
C_t = \text{capacidad de producción de la planta durante el periodo } t
$$

La cantidad de moscas estériles asignada a una estrategia de liberación deberá cumplir:

$$
R_t \leq C_t
$$

donde:

* \(R_t\) representa la cantidad de moscas estériles asignadas a la liberación durante el periodo \(t\).
* \(C_t\) representa la cantidad máxima disponible de acuerdo con la producción de la planta durante ese periodo.

Cuando se incorporen datos reales de producción semanal, la variable \(C_t\) podrá ser sustituida por los valores registrados para cada semana. De esta manera, el modelo podrá representar las variaciones reales de producción en lugar de utilizar únicamente una capacidad máxima teórica.

También deberá considerarse que la cantidad producida y la cantidad liberada son variables diferentes. Por esta razón, cuando existan datos suficientes, podrá utilizarse una variable intermedia de disponibilidad:

$$
A_t \leq C_t
$$

y posteriormente:

$$
R_t \leq A_t
$$

donde \(A_t\) representa la cantidad de moscas estériles disponibles para una estrategia específica durante el periodo \(t\).

En una primera versión del modelo, si no existen datos suficientes para representar pérdidas, almacenamiento u otras restricciones operativas, podrá asumirse que la disponibilidad para la estrategia corresponde a la cantidad de producción asignada durante ese periodo. Este supuesto deberá quedar identificado y podrá modificarse posteriormente.

Las restricciones relacionadas con la producción de la planta serán independientes de las restricciones biológicas de la población silvestre. Es decir, una estrategia puede requerir una cantidad determinada de moscas estériles desde el punto de vista biológico, pero solamente podrá utilizar la cantidad que se encuentre disponible de acuerdo con la capacidad de producción de Metapa.

De esta forma, el modelo permitirá identificar situaciones en las que una estrategia de control sea biológicamente adecuada pero no sea factible debido a las limitaciones de producción.

La capacidad máxima proyectada de 100 millones de moscas estériles por semana será considerada como referencia de operación de la planta. La posibilidad de una ampliación posterior hasta 120 millones semanales se mantendrá como un escenario futuro y no como capacidad disponible automáticamente en la simulación base.

No se incorporará como capacidad de producción del proyecto la producción proveniente de otras plantas. El suministro considerado para las simulaciones corresponderá exclusivamente a la planta de Metapa de Domínguez, Chiapas.

## 2.11 Datos confirmados y datos pendientes

La información disponible sobre la planta de Metapa de Domínguez permite establecer algunos elementos del proceso productivo y de su capacidad de producción. Sin embargo, todavía existen parámetros que deberán determinarse mediante la revisión de fuentes científicas, documentos técnicos y registros oficiales de producción.

Para evitar la incorporación de valores no sustentados, los datos utilizados en el modelo serán clasificados de acuerdo con su nivel de disponibilidad y respaldo documental.

### Datos confirmados

Entre los datos que actualmente cuentan con respaldo oficial se encuentran:

* Ubicación de la planta: Metapa de Domínguez, Chiapas, México.
* Inicio de operaciones: 28 de junio de 2026.
* Producción proyectada de 28 millones de moscas estériles por semana para mediados de julio de 2026.
* Incremento progresivo de la producción hasta alcanzar una capacidad proyectada de 100 millones de moscas estériles por semana hacia finales de 2026.
* Posibilidad de analizar posteriormente una ampliación hasta 120 millones de moscas estériles semanales.
* Utilización de Cobalto-60 para la irradiación de las pupas.
* Intervalo de dosis de irradiación reportado de 55 a 70 Gy.
* Existencia de registros semanales oficiales de producción publicados por SENASICA.

La información semanal publicada por SENASICA será considerada una fuente prioritaria para construir posteriormente la serie temporal de producción de la planta. Actualmente se encuentran disponibles registros correspondientes a diferentes semanas de 2026.

### Datos pendientes de determinar

Para completar la parametrización del componente de producción todavía será necesario determinar, cuando exista información disponible:

* Número de pupas procesadas por periodo.
* Proporción de pupas que sobreviven al proceso de irradiación.
* Porcentaje de emergencia de adultos.
* Proporción de machos y hembras obtenidos.
* Cantidad efectiva de machos estériles disponibles para liberación.
* Pérdidas durante las diferentes etapas del proceso.
* Tiempo requerido entre las etapas de producción.
* Capacidad de procesamiento de cada etapa.
* Variaciones de producción entre periodos.
* Cantidad de moscas que puede ser destinada a una estrategia específica de liberación.
* Posibles restricciones operativas que reduzcan la disponibilidad respecto de la producción registrada.
* Parámetros relacionados con la calidad y competitividad de los machos estériles.

Estos parámetros no serán asignados mediante estimaciones arbitrarias. Cuando no exista información suficiente, serán identificados como parámetros pendientes, supuestos de escenario o variables sujetas a análisis de sensibilidad.

### Clasificación para el modelo

Los datos utilizados posteriormente podrán clasificarse en tres categorías:

**Datos observados:** valores obtenidos directamente de registros oficiales de producción o liberación.

**Datos científicos:** valores obtenidos de literatura científica o documentos técnicos relacionados con la biología y aplicación de la Técnica del Insecto Estéril.

**Supuestos de escenario:** valores utilizados únicamente cuando no exista información suficiente y que deberán ser modificables durante las simulaciones.

Esta clasificación permitirá identificar el origen de cada parámetro y evitar que un valor supuesto sea interpretado como un dato real de operación de la planta.

La información de la planta de Metapa será utilizada como fuente exclusiva para representar la producción disponible dentro del proyecto. Las instalaciones de otros países no serán utilizadas para establecer la capacidad productiva de las simulaciones.

## 2.12 Fuentes de información

La caracterización de la planta de producción de moscas estériles de gusano barrenador del ganado de Metapa de Domínguez, Chiapas, se realizará utilizando principalmente información oficial publicada por instituciones gubernamentales y, posteriormente, fuentes científicas y técnicas especializadas cuando sea necesario complementar los parámetros del modelo.

La principal fuente de información utilizada para describir la planta será el Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria (SENASICA), debido a que es la institución responsable de la información oficial relacionada con la operación de la planta y las acciones de control del gusano barrenador del ganado en México.

Entre las fuentes principales consideradas se encuentran:

### Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria (SENASICA)

**Planta productora de mosca estéril de gusano barrenador del ganado**

Esta fuente proporciona información general sobre la ubicación, características e infraestructura de la planta de Metapa de Domínguez, Chiapas, así como información relacionada con el proceso de producción y las condiciones utilizadas para la cría del gusano barrenador.

**Producción de Moscas Estériles y Parasitoides**

Esta fuente será utilizada para consultar los registros semanales de producción publicados por SENASICA. Los documentos disponibles permitirán construir posteriormente una serie temporal de producción y disponibilidad de moscas estériles producidas en México.

**Comunicados de prensa de la Planta productora de mosca estéril de gusano barrenador del ganado**

Los comunicados oficiales serán utilizados para complementar la información relacionada con el inicio de operaciones de la planta, producción, liberaciones y avances de la infraestructura.

**Lista y en operación, la planta de producción de moscas estériles del gusano barrenador en Chiapas**

Esta publicación será utilizada como referencia para documentar la puesta en operación de la planta y su función dentro de la estrategia de prevención, control y erradicación del gusano barrenador del ganado en México.

### Fuentes científicas y técnicas complementarias

Cuando los registros oficiales de la planta no proporcionen algún parámetro necesario para la construcción del modelo, se recurrirá a literatura científica, documentos técnicos y fuentes especializadas relacionadas con:

* Biología y ciclo de vida de *Cochliomyia hominivorax*.
* Desarrollo y supervivencia de las diferentes etapas del insecto.
* Producción masiva de insectos.
* Técnica del Insecto Estéril.
* Irradiación y esterilización de insectos.
* Emergencia y supervivencia de machos estériles.
* Competitividad reproductiva de machos estériles.
* Estrategias de liberación.
* Modelación matemática de poblaciones de gusano barrenador.

Cada parámetro incorporado posteriormente al modelo deberá registrar su fuente de procedencia, unidad de medida y, cuando sea posible, nivel de confianza o tipo de dato.

La información obtenida de fuentes oficiales será diferenciada de los parámetros obtenidos de literatura científica y de los valores utilizados como supuestos de escenario. Esta clasificación permitirá mantener la trazabilidad de los datos y facilitará la validación y actualización del modelo.

No se utilizarán datos de otras plantas de producción como sustituto de información faltante de la planta de Metapa. Cuando un parámetro específico de la planta mexicana no se encuentre disponible, será identificado como dato pendiente o supuesto de escenario hasta contar con evidencia suficiente para incorporarlo.
