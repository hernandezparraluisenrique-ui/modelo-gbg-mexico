# 1. Delimitación del proyecto

## 1.1 Organismo de estudio

El organismo de estudio es el gusano barrenador del ganado (GBG), correspondiente a la especie *Cochliomyia hominivorax*. Se trata de un díptero cuyas larvas pueden desarrollarse en heridas de animales de sangre caliente, provocando miasis y afectaciones a la salud y productividad pecuaria.

El modelo se enfocará en representar la dinámica de la población silvestre de *Cochliomyia hominivorax* y su respuesta ante la aplicación de la Técnica del Insecto Estéril (TIE), mediante la liberación de machos estériles.

## 1.2 Hospedadores considerados

El modelo considerará únicamente a los bovinos y porcinos como hospedadores dentro del alcance del proyecto. Esta delimitación permitirá analizar la relación entre la presencia del gusano barrenador del ganado y las infestaciones registradas en estas dos especies.

La población de hospedadores se considerará como un componente asociado a la dinámica del gusano barrenador, particularmente para representar la ocurrencia de infestaciones y su posible relación con la población silvestre del parásito.

No se establecerá de manera inicial una cantidad fija de individuos de *Cochliomyia hominivorax* por animal, debido a que dicha relación deberá determinarse posteriormente a partir de información epidemiológica y biológica disponible.


## 1.3 Ámbito geográfico

El modelo se desarrollará para el contexto de México, considerando la dinámica poblacional del gusano barrenador del ganado asociada con infestaciones en bovinos y porcinos.

Para el componente de producción de moscas estériles se considerará exclusivamente la planta productora de mosca estéril de gusano barrenador del ganado ubicada en Metapa de Domínguez, Chiapas, México. La capacidad de producción y disponibilidad de moscas estériles de esta planta constituirán una restricción para las estrategias de liberación evaluadas por el modelo.

El alcance geográfico específico de las liberaciones y la distribución espacial de la población del gusano barrenador serán definidos posteriormente, de acuerdo con la disponibilidad de información epidemiológica y espacial necesaria para la construcción del modelo.


## 1.4 Estrategia de control

La estrategia de control considerada en el modelo será la Técnica del Insecto Estéril (TIE), mediante la liberación de machos estériles de *Cochliomyia hominivorax* en áreas donde se encuentre presente la población silvestre.

La estrategia se basa en que los machos estériles compitan con los machos silvestres por el apareamiento con las hembras de la población objetivo. Los apareamientos entre hembras silvestres y machos estériles no generan descendencia viable, lo que permite reducir progresivamente la capacidad reproductiva de la población silvestre.

El modelo evaluará diferentes cantidades y estrategias de liberación de machos estériles, considerando como restricción la disponibilidad de moscas producidas por la planta de Metapa de Domínguez, Chiapas.

La efectividad de cada estrategia será evaluada mediante su efecto sobre la dinámica de la población silvestre y el tiempo requerido para alcanzar el criterio de control o erradicación establecido para el modelo.


## 1.5 Planta de producción considerada

El componente de producción de moscas estériles del modelo estará basado exclusivamente en la planta productora de mosca estéril de gusano barrenador del ganado ubicada en Metapa de Domínguez, Chiapas, México.

La planta será considerada como la fuente de suministro de los machos estériles utilizados en las estrategias de control evaluadas. Su proceso productivo comprende las etapas necesarias para la cría del gusano barrenador, desarrollo de las fases inmaduras, obtención de pupas, esterilización mediante irradiación y preparación de los insectos para su posterior liberación.

La capacidad de producción de la planta será incorporada al modelo como una restricción sobre la cantidad de moscas estériles que pueden estar disponibles para las estrategias de liberación. Los valores específicos de producción, disponibilidad y demás parámetros asociados con la planta serán documentados posteriormente a partir de fuentes oficiales y utilizados en la parametrización del modelo.

No se considerará la producción de moscas estériles proveniente de otras plantas como fuente de suministro para las simulaciones del proyecto.


## 1.6 Objetivo del modelo

El objetivo del modelo matemático y computacional es representar la dinámica de la población silvestre de *Cochliomyia hominivorax* en bovinos y porcinos, así como evaluar el efecto de diferentes estrategias de liberación de machos estériles producidos en la planta de Metapa de Domínguez, Chiapas.

El modelo deberá permitir analizar la evolución de la población objetivo a lo largo del tiempo bajo diferentes condiciones de infestación y estrategias de liberación de moscas estériles.

A partir de las simulaciones, se buscará estimar:

* La evolución de la población silvestre de *Cochliomyia hominivorax*.
* La cantidad de machos estériles requerida para las estrategias de control evaluadas.
* La frecuencia y cantidad de las liberaciones.
* El efecto de las restricciones de producción de la planta de Metapa sobre las estrategias de liberación.
* El tiempo requerido para que la población alcance el criterio de control o erradicación definido para el modelo.

El modelo servirá como base matemática y computacional para el desarrollo posterior de un simulador de estrategias de producción y liberación de moscas estériles.


## 1.7 Variables generales de interés

Para representar la dinámica poblacional del gusano barrenador y evaluar las estrategias de control mediante la Técnica del Insecto Estéril, el modelo considerará un conjunto de variables relacionadas con la población silvestre, la población de insectos estériles, las infestaciones en los hospedadores y la producción disponible para las liberaciones.

De manera general, se consideran las siguientes variables de interés:

* Población de machos silvestres de *Cochliomyia hominivorax*.
* Población de hembras silvestres de *Cochliomyia hominivorax*.
* Población de machos estériles disponibles para el control.
* Cantidad de machos estériles liberados durante cada periodo.
* Número de bovinos infestados.
* Número de porcinos infestados.
* Cantidad de moscas estériles producidas o disponibles por la planta de Metapa.
* Tiempo transcurrido durante la simulación.
* Tamaño de la población silvestre.
* Tiempo requerido para alcanzar el criterio de control o erradicación.

Estas variables serán definidas formalmente mediante símbolos, unidades de medida y relaciones matemáticas en las etapas posteriores del proyecto. Su inclusión definitiva dependerá de la estructura del modelo y de la disponibilidad de información científica y epidemiológica suficiente para su parametrización.

## 1.8 Alcance del modelo

El modelo tendrá como alcance la representación matemática y computacional de la dinámica de la población silvestre de *Cochliomyia hominivorax* y la evaluación de estrategias de control mediante la liberación de machos estériles.

El modelo permitirá simular diferentes condiciones iniciales de la población objetivo y diferentes estrategias de liberación, considerando la disponibilidad de moscas estériles producidas por la planta de Metapa de Domínguez, Chiapas.

La simulación permitirá analizar la evolución de la población a lo largo del tiempo y comparar el comportamiento de diferentes estrategias de control. Entre los principales resultados se considerarán la cantidad de moscas estériles utilizadas, la frecuencia de liberación, la evolución de la población silvestre y el tiempo necesario para alcanzar el criterio de control o erradicación establecido.

Los parámetros utilizados en el modelo serán obtenidos, siempre que sea posible, de fuentes oficiales, literatura científica y datos epidemiológicos disponibles. Los parámetros para los cuales no exista información suficiente serán identificados como supuestos o variables de escenario y serán sometidos a análisis de sensibilidad cuando corresponda.

## 1.9 Elementos fuera del alcance

El modelo no contemplará los siguientes elementos dentro de su alcance:

* Otras especies de hospedadores diferentes de bovinos y porcinos.
* Producción de moscas estériles en plantas diferentes a la ubicada en Metapa de Domínguez, Chiapas.
* Utilización de plantas de producción de otros países como fuente de suministro para las estrategias de liberación.
* Modelación detallada de los procesos industriales y operativos internos de la planta de Metapa que no sean necesarios para determinar la disponibilidad de moscas estériles.
* Modelación económica detallada de los costos de producción, transporte, liberación o control.
* Modelación detallada de las rutas de transporte aéreo o terrestre utilizadas para la distribución de las moscas.
* Factores ambientales o climáticos a escala nacional que no puedan ser incorporados de manera sustentada mediante parámetros disponibles.
* Análisis genético o evolutivo detallado de la población de *Cochliomyia hominivorax*.
* Modelación de enfermedades diferentes a las infestaciones ocasionadas por el gusano barrenador del ganado.
* Desarrollo de una plataforma web o interfaz de usuario dentro del modelo matemático.

Estos elementos podrán considerarse como posibles extensiones futuras del proyecto, pero no formarán parte de la primera versión del modelo.

## 1.10 Productos esperados del modelo

Como resultado del desarrollo del modelo matemático y computacional se espera obtener una herramienta capaz de representar y analizar la dinámica poblacional de *Cochliomyia hominivorax* bajo diferentes condiciones y estrategias de control mediante la Técnica del Insecto Estéril.

Los principales productos esperados son:

* Un modelo matemático que represente la dinámica de la población silvestre del gusano barrenador del ganado.
* Un modelo computacional implementado en Python que permita ejecutar simulaciones.
* La representación del efecto de la liberación de machos estériles sobre la población silvestre.
* La estimación de la cantidad de moscas estériles necesarias para las estrategias evaluadas.
* La evaluación de diferentes frecuencias y cantidades de liberación.
* La incorporación de la capacidad de producción de la planta de Metapa de Domínguez como restricción para las estrategias de liberación.
* La estimación del tiempo requerido para alcanzar el criterio de control o erradicación establecido.
* La comparación de diferentes escenarios de infestación y estrategias de control.
* Datos y gráficas que permitan analizar la evolución de la población y los resultados de cada simulación.
* Una base computacional que pueda ser utilizada posteriormente para el desarrollo del simulador y de la plataforma web contemplados en las siguientes etapas del proyecto.
