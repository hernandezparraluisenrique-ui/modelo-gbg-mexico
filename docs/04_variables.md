# 4. Variables del modelo

## 4.1 Definición de variables

Las variables del modelo representan las cantidades que pueden cambiar durante el periodo de simulación como consecuencia de la dinámica poblacional del gusano barrenador del ganado (GBG), la reproducción de la población silvestre y la aplicación de la Técnica del Insecto Estéril (TIE).

A diferencia de los parámetros, que representan características biológicas, epidemiológicas, productivas o de control que se consideran constantes o definidas para un escenario determinado, las variables pueden modificar su valor conforme avanza el tiempo de simulación.

Las variables se expresarán como funciones del tiempo, utilizando \(t\) como referencia temporal. Dependiendo de la estructura definitiva del modelo, algunas variables formarán parte directamente del sistema de ecuaciones diferenciales, mientras que otras serán utilizadas como entradas, variables de observación o resultados derivados.

Para evitar confusiones, las variables del proyecto se clasifican en cuatro grupos principales:

1. **Variables de estado:** representan cantidades de la población que cambian con el tiempo y que forman parte de la dinámica del modelo.
2. **Variables de entrada o control:** representan acciones externas que pueden ser definidas para cada escenario, principalmente las cantidades y frecuencia de liberación de moscas estériles.
3. **Variables epidemiológicas u observacionales:** representan información relacionada con la infestación de bovinos y porcinos y pueden utilizarse para relacionar o validar la dinámica de la población de GBG.
4. **Variables de salida:** representan resultados calculados a partir de la simulación, como la población restante, la proporción de moscas estériles respecto a las silvestres y el tiempo necesario para alcanzar el criterio de control o erradicación.

La clasificación definitiva de cada variable se establecerá conforme se complete la formulación matemática del modelo.

### Variables de estado candidatas

Como punto de partida, se consideran las siguientes variables para representar la población adulta del GBG:

* \(M_w(t)\): número de machos silvestres fértiles en el tiempo \(t\).
* \(F_v(t)\): número de hembras silvestres vírgenes en el tiempo \(t\).
* \(F_m(t)\): número de hembras silvestres apareadas en el tiempo \(t\).
* \(M_s(t)\): número de machos estériles disponibles en la población después de las liberaciones en el tiempo \(t\).

Estas variables constituyen una propuesta inicial para la representación de la dinámica reproductiva. Su inclusión definitiva y la forma en que interactúan serán determinadas durante la formulación de las ecuaciones del modelo matemático.

### Variables epidemiológicas candidatas

Para representar la relación entre la población de GBG y los hospedadores considerados en el proyecto, se contemplan inicialmente:

* \(I_b(t)\): número de bovinos infestados en el tiempo \(t\).
* \(I_p(t)\): número de porcinos infestados en el tiempo \(t\).

Estas variables no necesariamente formarán parte del mismo sistema de ecuaciones que describe la población de moscas. Su función podrá ser la de representar una capa epidemiológica u observacional que permita relacionar la presencia de GBG con los hospedadores y, cuando existan datos suficientes, apoyar la estimación o validación del modelo.

No se establecerá una conversión directa entre el número de animales infestados y el número de moscas silvestres sin contar con evidencia científica que permita justificar dicha relación.

### Variables de entrada y control

La principal variable de control considerada inicialmente es:

* \(R_t\): cantidad de moscas estériles liberadas durante el periodo \(t\).

Esta variable podrá modificarse entre escenarios para evaluar diferentes estrategias de liberación, considerando las restricciones de producción de la planta de Metapa de Domínguez, Chiapas.

La cantidad liberada deberá cumplir las restricciones de disponibilidad y producción establecidas previamente:

$$
R_t \leq A_t
$$

$$
A_t \leq C_t
$$

por lo que:

$$
R_t \leq A_t \leq C_t
$$

donde \(A_t\) representa la cantidad de moscas disponibles para una estrategia de liberación y \(C_t\) representa la producción disponible de la planta durante el periodo correspondiente.

### Variables de salida

A partir de las variables de estado y de control podrán obtenerse variables derivadas que permitan evaluar el comportamiento de cada escenario.

Entre ellas se consideran inicialmente:

* \(N_w(t)\): población silvestre total de GBG.
* \(\rho(t)\): proporción entre machos estériles y machos silvestres.
* \(T_E\): tiempo necesario para alcanzar el criterio de erradicación establecido.
* \(R_{total}\): cantidad total de moscas estériles liberadas durante una simulación.
* \(U_C\): utilización de la capacidad de producción disponible.

Estas variables serán calculadas a partir del comportamiento del modelo y no deberán confundirse con parámetros de entrada.

La clasificación anterior es provisional y podrá modificarse durante la formulación matemática si el análisis de las ecuaciones, la disponibilidad de datos o la validación del modelo indican que alguna variable debe incorporarse, eliminarse o cambiar de categoría.

## 4.2 Variables de la población silvestre

Las variables de la población silvestre representan los diferentes grupos de adultos del gusano barrenador del ganado que participan en la dinámica reproductiva de la población objetivo.

Para la formulación inicial del modelo se propone separar la población adulta de acuerdo con su sexo y estado reproductivo. Esta separación permite representar de manera explícita el proceso de apareamiento y posteriormente analizar el efecto de la liberación de machos estériles sobre la reproducción de la población silvestre.

### 4.2.1 Machos silvestres fértiles

La variable \(M_w(t)\) representa el número de machos silvestres fértiles presentes en el sistema en el tiempo \(t\).

Estos individuos forman parte de la población reproductiva natural y compiten con los machos estériles liberados mediante la TIE por el apareamiento con las hembras.

Su cantidad puede variar debido a factores como:

* nacimiento de nuevos machos adultos;
* mortalidad natural;
* condiciones ambientales;
* disponibilidad de hospedadores;
* dinámica reproductiva de la población.

La variable se expresa como:

$$
M_w(t) = \text{número de machos silvestres fértiles en el tiempo } t
$$

Unidad:

$$
\text{individuos}
$$

### 4.2.2 Hembras silvestres vírgenes

La variable \(F_v(t)\) representa el número de hembras silvestres adultas que todavía no han sido apareadas en el tiempo \(t\).

Esta variable es importante para representar el proceso de apareamiento, ya que las hembras vírgenes pueden aparearse tanto con machos silvestres fértiles como con machos estériles liberados.

Se expresa como:

$$
F_v(t) = \text{número de hembras silvestres vírgenes en el tiempo } t
$$

Unidad:

$$
\text{individuos}
$$

La transición de una hembra virgen hacia el grupo de hembras apareadas dependerá del tipo de macho con el que se produzca el apareamiento.

### 4.2.3 Hembras silvestres apareadas

La variable \(F_m(t)\) representa el número de hembras silvestres que ya han sido apareadas y que pueden participar en la producción de descendencia.

En el modelo inicial, esta variable permitirá distinguir a las hembras que ya tuvieron contacto reproductivo de aquellas que permanecen vírgenes.

Se expresa como:

$$
F_m(t) = \text{número de hembras silvestres apareadas en el tiempo } t
$$

Unidad:

$$
\text{individuos}
$$

La contribución de estas hembras a la generación de nuevos individuos dependerá de si el apareamiento ocurrió con un macho silvestre fértil o con un macho estéril.

### 4.2.4 Población silvestre adulta total

A partir de las variables anteriores puede definirse una variable derivada para representar la población adulta silvestre total:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

donde:

* \(N_w(t)\) = población adulta silvestre total;
* \(M_w(t)\) = machos silvestres fértiles;
* \(F_v(t)\) = hembras silvestres vírgenes;
* \(F_m(t)\) = hembras silvestres apareadas.

Esta variable permitirá observar de manera general la evolución de la población silvestre durante la simulación.

Sin embargo, \(N_w(t)\) se considera inicialmente una **variable derivada**, ya que su valor se obtiene a partir de las variables de estado principales y no necesariamente requiere una ecuación diferencial independiente.

### 4.2.5 Consideraciones para la formulación matemática

La separación de la población adulta en \(M_w(t)\), \(F_v(t)\) y \(F_m(t)\) permitirá representar de manera más detallada el efecto de la TIE.

En particular, el modelo deberá considerar que los machos estériles no tienen como objetivo eliminar directamente a los machos silvestres, sino reducir la probabilidad de que las hembras silvestres tengan apareamientos capaces de producir descendencia viable.

Por esta razón, la interacción entre:

$$
M_w(t),\quad F_v(t),\quad F_m(t),\quad M_s(t)
$$

será una parte fundamental de la formulación matemática.

La estructura definitiva de estas interacciones se establecerá en el documento correspondiente al modelo matemático, después de revisar los parámetros biológicos y de TIE disponibles.

Por el momento, estas variables se consideran **variables candidatas de estado** del modelo.

## 4.3 Variables de reproducción

Las variables de reproducción representan los procesos relacionados con el apareamiento de la población adulta del gusano barrenador del ganado (GBG) y la generación de nuevos individuos.

Estas variables son necesarias para representar el mecanismo mediante el cual la población silvestre puede mantenerse o disminuir a lo largo del tiempo. Asimismo, permiten incorporar el efecto de la Técnica del Insecto Estéril (TIE), debido a que los machos estériles liberados compiten con los machos silvestres por el apareamiento con las hembras.

### 4.3.1 Apareamientos con machos silvestres

La variable \(A_w(t)\) representa la cantidad o tasa de apareamientos entre hembras silvestres y machos silvestres fértiles durante el tiempo \(t\).

Estos apareamientos pueden producir descendencia viable y, por lo tanto, contribuir al mantenimiento de la población silvestre.

Se expresa conceptualmente como:

$$
A_w(t)=\text{apareamientos efectivos entre hembras y machos silvestres}
$$

La unidad definitiva dependerá de la formulación matemática utilizada, pudiendo expresarse como apareamientos por unidad de tiempo.

El valor de \(A_w(t)\) dependerá de factores como:

* cantidad de machos silvestres disponibles;
* cantidad de hembras vírgenes;
* capacidad de apareamiento;
* competencia entre machos;
* condiciones establecidas mediante los parámetros biológicos del modelo.

### 4.3.2 Apareamientos con machos estériles

La variable \(A_s(t)\) representa la cantidad o tasa de apareamientos entre hembras silvestres y machos estériles liberados durante el tiempo \(t\).

Estos apareamientos son fundamentales para representar el funcionamiento de la TIE, debido a que un apareamiento con un macho estéril debe reducir o impedir la producción de descendencia viable.

Se expresa como:

$$
A_s(t)=\text{apareamientos efectivos entre hembras silvestres y machos estériles}
$$

La unidad definitiva dependerá de la formulación matemática.

La cantidad de estos apareamientos estará relacionada con:

* número de hembras vírgenes;
* cantidad de machos estériles presentes;
* cantidad de machos silvestres;
* competitividad relativa de los machos estériles;
* supervivencia de los machos estériles.

### 4.3.3 Proporción de apareamientos con machos estériles

La variable \(p_s(t)\) representa la proporción de apareamientos de hembras silvestres que ocurren con machos estériles.

Como aproximación inicial, puede calcularse mediante:

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

donde:

* \(p_s(t)\) = proporción de apareamientos con machos estériles;
* \(M_s(t)\) = cantidad de machos estériles disponibles;
* \(M_w(t)\) = cantidad de machos silvestres fértiles;
* \(c\) = competitividad relativa de los machos estériles.

Esta expresión se considera inicialmente una función conceptual para representar la competencia entre machos. Su forma definitiva deberá validarse durante la formulación del modelo y de acuerdo con los parámetros biológicos disponibles.

### 4.3.4 Proporción de apareamientos con machos silvestres

La variable \(p_w(t)\) representa la proporción de apareamientos que ocurren con machos silvestres fértiles.

Cuando solamente se consideran dos posibilidades de apareamiento, macho silvestre o macho estéril, puede expresarse como:

$$
p_w(t)=1-p_s(t)
$$

donde:

* \(p_w(t)\) = proporción de apareamientos con machos silvestres;
* \(p_s(t)\) = proporción de apareamientos con machos estériles.

Esta variable permitirá determinar qué fracción de los apareamientos tiene potencial para producir descendencia viable.

### 4.3.5 Descendencia viable

La variable \(B_v(t)\) representa la cantidad de nuevos individuos viables generados a partir de los apareamientos reproductivamente efectivos durante el tiempo \(t\).

Conceptualmente:

$$
B_v(t)=\text{nuevos individuos viables generados durante }t
$$

La producción de descendencia dependerá principalmente de:

* número de hembras reproductivamente activas;
* proporción de apareamientos con machos fértiles;
* fecundidad;
* supervivencia de las etapas posteriores al nacimiento;
* parámetros biológicos utilizados por el modelo.

La ecuación definitiva para \(B_v(t)\) se establecerá posteriormente en el modelo matemático.

### 4.3.6 Descendencia no viable asociada a la TIE

De manera conceptual, también puede definirse una variable \(B_s(t)\) para representar la descendencia asociada a apareamientos con machos estériles que no produce una nueva población viable.

$$
B_s(t)=\text{descendencia no viable asociada a apareamientos con machos estériles}
$$

Esta variable no necesariamente tendrá que incorporarse como una variable de estado independiente. Puede ser utilizada únicamente como variable auxiliar para representar el efecto de la TIE en la reproducción.

Su necesidad será evaluada durante la construcción de las ecuaciones definitivas.

### 4.3.7 Proporción estéril:silvestre

Para evaluar la presión ejercida por los machos estériles sobre la población silvestre se utilizará la razón:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

donde:

* \(\rho(t)\) = proporción de machos estériles respecto a machos silvestres;
* \(M_s(t)\) = machos estériles disponibles;
* \(M_w(t)\) = machos silvestres fértiles.

Esta variable será especialmente importante para comparar diferentes estrategias de liberación.

La razón de referencia de \(10:1\) documentada para áreas de baja densidad se tratará como una referencia operativa y no como una constante biológica universal del modelo.

### 4.3.8 Consideraciones para la formulación matemática

Las variables de reproducción permitirán establecer el vínculo entre la población adulta y la generación de nuevos individuos.

La lógica general será:

$$
\text{Machos silvestres}
+
\text{Hembras vírgenes}
\rightarrow
\text{Apareamiento}
\rightarrow
\text{Descendencia}
$$

Mientras que la TIE introduce una segunda posibilidad:

$$
\text{Machos estériles}
+
\text{Hembras vírgenes}
\rightarrow
\text{Apareamiento}
\rightarrow
\text{Reducción de descendencia viable}
$$

Por lo tanto, el efecto de la liberación de moscas estériles se representará principalmente mediante una modificación de la probabilidad de apareamiento y de la producción de descendencia viable, en lugar de considerar que las moscas estériles eliminan directamente a los individuos silvestres.

Las variables \(A_w(t)\), \(A_s(t)\) y \(B_s(t)\) se consideran inicialmente variables auxiliares o derivadas. Su incorporación definitiva al sistema de ecuaciones dependerá de la estructura matemática seleccionada.

La formulación final deberá evitar duplicar procesos biológicos o introducir variables que no sean necesarias para resolver los objetivos del modelo.

## 4.4 Variables de la población estéril

Las variables de la población estéril representan la cantidad de machos estériles disponibles y presentes en el sistema como resultado de las estrategias de producción y liberación provenientes de la planta de Metapa de Domínguez, Chiapas.

La representación de esta población es necesaria para determinar el efecto de la Técnica del Insecto Estéril (TIE) sobre la población silvestre de GBG.

En el modelo se distinguirá entre las moscas producidas por la planta, las disponibles para una estrategia de liberación, las efectivamente liberadas y las que permanecen disponibles en el ambiente después de la liberación.

### 4.4.1 Machos estériles presentes

La variable \(M_s(t)\) representa el número de machos estériles que permanecen disponibles en el sistema durante el tiempo \(t\) después de considerar las liberaciones y las pérdidas de individuos.

Se expresa como:

$$
M_s(t)=\text{número de machos estériles presentes en el tiempo }t
$$

Unidad:

$$
\text{individuos}
$$

Esta variable es diferente de la cantidad total de moscas estériles liberadas, ya que los individuos liberados pueden disminuir con el tiempo debido a la mortalidad u otros factores considerados por el modelo.

### 4.4.2 Cantidad de moscas estériles liberadas

La variable \(R_t\) representa la cantidad de moscas estériles liberadas durante el periodo \(t\).

$$
R_t=\text{cantidad de moscas estériles liberadas durante el periodo }t
$$

Unidad:

$$
\text{individuos/periodo}
$$

Esta variable constituye una de las principales variables de control del modelo, debido a que podrá modificarse para evaluar diferentes estrategias de liberación.

El valor de \(R_t\) estará limitado por la cantidad de moscas disponibles y por la capacidad de producción de la planta de Metapa.

### 4.4.3 Moscas estériles disponibles para liberación

La variable \(A_t\) representa la cantidad de moscas estériles que se encuentran disponibles para ser asignadas a una estrategia de liberación durante el periodo \(t\).

$$
A_t=\text{cantidad de moscas estériles disponibles para liberación}
$$

Unidad:

$$
\text{individuos/periodo}
$$

Esta variable permite diferenciar la producción de la planta de la cantidad que realmente puede ser utilizada por una estrategia específica.

Se considera la restricción:

$$
R_t\leq A_t
$$

### 4.4.4 Producción disponible de la planta

La variable \(C_t\) representa la cantidad de moscas estériles que la planta de Metapa puede producir o poner a disposición durante el periodo \(t\), de acuerdo con el escenario considerado.

$$
C_t=\text{cantidad de moscas estériles producidas durante el periodo }t
$$

Unidad:

$$
\text{individuos/periodo}
$$

La cantidad disponible para las estrategias de liberación estará limitada por esta producción:

$$
A_t\leq C_t
$$

Por lo tanto, la relación general será:

$$
R_t\leq A_t\leq C_t
$$

Esta relación permitirá que el modelo respete las restricciones de producción establecidas para la planta considerada.

### 4.4.5 Supervivencia de los machos estériles

La permanencia de los machos estériles en el sistema dependerá de su supervivencia después de la liberación.

Para representar este comportamiento se utilizará el parámetro de supervivencia \(S_s\) o, alternativamente, una tasa de mortalidad \(\mu_s\), dependiendo de la formulación matemática definitiva.

La variable \(M_s(t)\) podrá disminuir entre periodos como consecuencia de la mortalidad de los machos estériles.

La forma específica de esta disminución será determinada en el modelo matemático a partir de la información disponible sobre supervivencia de los individuos liberados.

### 4.4.6 Proporción de machos estériles respecto a machos silvestres

La variable \(\rho(t)\) representa la proporción entre machos estériles y machos silvestres fértiles presentes en el sistema:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

donde:

* \(\rho(t)\) = proporción de machos estériles respecto a machos silvestres;
* \(M_s(t)\) = número de machos estériles presentes;
* \(M_w(t)\) = número de machos silvestres fértiles.

Esta variable será utilizada para evaluar la presión relativa de los machos estériles sobre la población silvestre.

La proporción de referencia \(10:1\), documentada para áreas de baja densidad, será utilizada únicamente como referencia operativa y como posible escenario de comparación. No se considerará una constante universal para todas las condiciones del modelo.

### 4.4.7 Diferencia entre producción, disponibilidad y liberación

Para evitar errores en la simulación, se establecen las siguientes diferencias conceptuales:

$$
C_t \neq A_t \neq R_t \neq M_s(t)
$$

donde:

* \(C_t\): cantidad producida o disponible por la planta durante el periodo;
* \(A_t\): cantidad disponible para una estrategia;
* \(R_t\): cantidad efectivamente liberada;
* \(M_s(t)\): cantidad de machos estériles que permanece presente en el sistema después de las liberaciones y pérdidas.

Esta distinción será fundamental para representar correctamente las restricciones de la planta de Metapa.

Por ejemplo, que la planta tenga una capacidad de producción de determinado número de moscas por semana no significa que toda esa cantidad tenga que ser liberada inmediatamente ni que todos esos individuos permanezcan en campo durante toda la semana.

### 4.4.8 Relación con la planta de Metapa

Las variables relacionadas con la producción y disponibilidad deberán utilizar exclusivamente la planta de producción de moscas estériles de GBG ubicada en Metapa de Domínguez, Chiapas, como fuente de producción para el modelo.

Los escenarios de producción podrán utilizar los valores previamente documentados:

* \(C_{ini}=28\,000\,000\) moscas por semana;
* \(C_{max}=100\,000\,000\) moscas por semana;
* \(C_{fut}=120\,000\,000\) moscas por semana como escenario de posible expansión.

Estos valores representan escenarios de disponibilidad de producción y no implican que toda la producción deba destinarse a una única estrategia de liberación.

### 4.4.9 Consideraciones para la formulación matemática

La variable principal de estado relacionada con la población estéril será inicialmente \(M_s(t)\).

La cantidad \(R_t\) funcionará principalmente como una variable de entrada o control definida por cada estrategia de simulación.

La cantidad \(C_t\) funcionará como una restricción de producción, mientras que \(A_t\) permitirá representar la disponibilidad de moscas para una estrategia determinada.

La relación conceptual será:

$$
\text{Producción}
\rightarrow
\text{Disponibilidad}
\rightarrow
\text{Liberación}
\rightarrow
\text{Machos estériles presentes}
\rightarrow
\text{Competencia por apareamiento}
$$

La formulación matemática definitiva determinará cómo se incorporan la supervivencia, mortalidad, frecuencia de liberación y demás factores que afectan a \(M_s(t)\).

## 4.5 Variables epidemiológicas

Las variables epidemiológicas representan la relación entre la población del gusano barrenador del ganado (GBG) y los hospedadores considerados dentro del proyecto: bovinos y porcinos.

Estas variables permiten representar la presencia de infestaciones y, cuando exista información suficiente, relacionar los resultados del modelo poblacional con los registros de animales afectados.

Los bovinos y porcinos no constituyen la población objetivo de la Técnica del Insecto Estéril. La población objetivo corresponde al GBG silvestre. Por esta razón, las variables epidemiológicas se utilizarán principalmente para representar la interacción entre el insecto y sus hospedadores, así como para apoyar la estimación, interpretación o validación del comportamiento de la población de GBG.

### 4.5.1 Población bovina

La variable \(B(t)\) representa la cantidad de bovinos considerados dentro del área o escenario de estudio durante el tiempo \(t\).

$$
B(t)=\text{número de bovinos considerados en el sistema en el tiempo }t
$$

Unidad:

$$
\text{animales}
$$

El valor de esta variable dependerá de la escala geográfica y de la disponibilidad de información para el escenario seleccionado.

### 4.5.2 Bovinos infestados

La variable \(I_b(t)\) representa el número de bovinos que presentan una infestación por GBG durante el tiempo \(t\).

$$
I_b(t)=\text{número de bovinos infestados por GBG en el tiempo }t
$$

Unidad:

$$
\text{animales}
$$

Esta variable puede utilizarse como indicador de la presencia del GBG en una población de hospedadores.

El número de bovinos infestados no se interpretará directamente como el número de moscas silvestres presentes, debido a que una infestación puede involucrar diferentes cantidades de individuos y etapas del ciclo biológico.

### 4.5.3 Población porcina

La variable \(P(t)\) representa la cantidad de porcinos considerados dentro del área o escenario de estudio durante el tiempo \(t\).

$$
P(t)=\text{número de porcinos considerados en el sistema en el tiempo }t
$$

Unidad:

$$
\text{animales}
$$

Al igual que en el caso de los bovinos, su valor dependerá de la escala geográfica seleccionada y de la información disponible.

### 4.5.4 Porcinos infestados

La variable \(I_p(t)\) representa el número de porcinos que presentan una infestación por GBG durante el tiempo \(t\).

$$
I_p(t)=\text{número de porcinos infestados por GBG en el tiempo }t
$$

Unidad:

$$
\text{animales}
$$

Esta variable permitirá representar la presencia de infestaciones de GBG en la población porcina considerada.

Al igual que \(I_b(t)\), no se utilizará una conversión directa entre animales infestados y cantidad de moscas sin evidencia científica que permita establecer dicha relación.

### 4.5.5 Tasa de infestación en bovinos

La variable \(\lambda_b(t)\) representa la tasa de aparición de nuevas infestaciones por GBG en la población bovina durante el tiempo \(t\).

Conceptualmente:

$$
\lambda_b(t)=f(M_w(t),F(t),B(t))
$$

donde la función dependerá de la estructura definitiva del modelo.

La tasa podrá estar relacionada con factores como:

* presencia de hembras reproductivas;
* disponibilidad de hospedadores;
* cantidad de bovinos susceptibles;
* comportamiento de búsqueda de hospedadores;
* condiciones ambientales;
* parámetros epidemiológicos disponibles.

La forma matemática definitiva de esta relación será determinada posteriormente.

### 4.5.6 Tasa de infestación en porcinos

La variable \(\lambda_p(t)\) representa la tasa de aparición de nuevas infestaciones por GBG en la población porcina durante el tiempo \(t\).

Conceptualmente:

$$
\lambda_p(t)=f(M_w(t),F(t),P(t))
$$

Su formulación definitiva dependerá de la información epidemiológica disponible y de la estructura del modelo.

### 4.5.7 Probabilidad de infestación

Las variables \(p_b(t)\) y \(p_p(t)\) representan, respectivamente, la probabilidad o proporción de infestación asociada con bovinos y porcinos.

$$
p_b(t)=\text{probabilidad o proporción de bovinos infestados}
$$

$$
p_p(t)=\text{probabilidad o proporción de porcinos infestados}
$$

Estas variables no deberán considerarse automáticamente como constantes. Su comportamiento dependerá de la información disponible y de la escala temporal y espacial utilizada.

### 4.5.8 Recuperación o salida de animales infestados

De manera preliminar se consideran las variables \(\gamma_b(t)\) y \(\gamma_p(t)\) para representar la tasa a la que los animales infestados dejan de formar parte del conjunto de animales infestados.

$$
\gamma_b(t)=\text{tasa de salida de bovinos infestados}
$$

$$
\gamma_p(t)=\text{tasa de salida de porcinos infestados}
$$

Estas variables no implican que el GBG se transmita entre animales como una enfermedad contagiosa.

La salida de un animal del conjunto de infestados puede deberse a factores como tratamiento, recuperación, muerte, traslado u otros mecanismos que deberán definirse únicamente si existe información suficiente para incorporarlos al modelo.

### 4.5.9 Función de las variables epidemiológicas dentro del modelo

Las variables epidemiológicas podrán cumplir una de las siguientes funciones:

1. **Variables de estado**, si existe suficiente información para modelar explícitamente la dinámica de las infestaciones.
2. **Variables observacionales**, si los registros de animales infestados se utilizan principalmente para representar la presencia del GBG.
3. **Variables de validación**, si los datos disponibles permiten comparar los resultados del modelo con observaciones reales.
4. **Variables auxiliares**, si son necesarias para establecer una relación entre la población de GBG y los hospedadores.

La función definitiva se determinará después de evaluar la disponibilidad y calidad de los datos epidemiológicos.

### 4.5.10 Relación con la población de GBG

La relación conceptual entre la población silvestre y los hospedadores puede representarse como:

$$
\text{Población de GBG}
\rightarrow
\text{hembras reproductivas}
\rightarrow
\text{búsqueda de hospedador}
\rightarrow
\text{infestación}
$$

Por lo tanto, los hospedadores representan una parte importante del sistema, pero no sustituyen a las variables que describen directamente la población del insecto.

El modelo deberá evitar asumir que existe una relación lineal simple entre el número de animales infestados y la población total de GBG.

### 4.5.11 Consideraciones para la formulación matemática

Las variables \(B(t)\), \(P(t)\), \(I_b(t)\) e \(I_p(t)\) podrán utilizarse para representar la capa epidemiológica del modelo.

Sin embargo, su incorporación al sistema principal de ecuaciones diferenciales dependerá de la disponibilidad de datos y de la necesidad de incluirlas para cumplir los objetivos del proyecto.

Si los datos epidemiológicos disponibles no permiten estimar de manera confiable las tasas de infestación, estas variables podrán utilizarse como variables observacionales o de validación, evitando introducir supuestos que no puedan ser respaldados científicamente.

La población objetivo del modelo continuará siendo la población silvestre de GBG, mientras que los bovinos y porcinos serán considerados como hospedadores y como posible fuente de información epidemiológica para el análisis del sistema.

## 4.6 Variables de producción y liberación

Las variables de producción y liberación representan la disponibilidad de moscas estériles provenientes de la planta de producción de Metapa de Domínguez, Chiapas, así como las decisiones relacionadas con la cantidad y frecuencia de liberación utilizadas en cada escenario de simulación.

Estas variables permiten establecer la conexión entre la capacidad productiva de la planta y la cantidad de machos estériles que pueden incorporarse al sistema de control del GBG.

### 4.6.1 Producción de moscas estériles

La variable \(C_t\) representa la cantidad de moscas estériles producidas o disponibles por la planta durante el periodo \(t\).

$$
C_t=\text{cantidad de moscas estériles producidas durante el periodo }t
$$

Unidad:

$$
\text{moscas/periodo}
$$

El valor de \(C_t\) podrá variar de acuerdo con el escenario de producción seleccionado.

Para el modelo se consideran inicialmente los escenarios de producción previamente documentados:

$$
C_{ini}=28\,000\,000\ \text{moscas/semana}
$$

$$
C_{max}=100\,000\,000\ \text{moscas/semana}
$$

y un escenario de posible expansión:

$$
C_{fut}=120\,000\,000\ \text{moscas/semana}
$$

Estos valores no representan necesariamente la cantidad que será liberada en cada periodo.

### 4.6.2 Moscas disponibles para una estrategia

La variable \(A_t\) representa la cantidad de moscas estériles que puede ser asignada a una estrategia de liberación durante el periodo \(t\).

$$
A_t=\text{moscas estériles disponibles para la estrategia durante }t
$$

Unidad:

$$
\text{moscas/periodo}
$$

Esta variable permite separar la producción de la planta de la cantidad que se decide utilizar en una estrategia determinada.

Se establece:

$$
A_t\leq C_t
$$

### 4.6.3 Cantidad liberada

La variable \(R_t\) representa la cantidad de moscas estériles que efectivamente se libera durante el periodo \(t\).

$$
R_t=\text{cantidad de moscas estériles liberadas durante }t
$$

Unidad:

$$
\text{moscas/periodo}
$$

La cantidad liberada estará limitada por la disponibilidad de moscas:

$$
R_t\leq A_t
$$

Por lo tanto:

$$
R_t\leq A_t\leq C_t
$$

Esta restricción será incorporada posteriormente al modelo computacional para evitar estrategias de liberación superiores a la capacidad de producción disponible.

### 4.6.4 Frecuencia de liberación

La variable \(f_R\) representa la frecuencia con la que se realizan las liberaciones de moscas estériles.

$$
f_R=\text{frecuencia de liberación}
$$

Unidad:

$$
\text{liberaciones/periodo}
$$

La frecuencia podrá variar entre escenarios. Por ejemplo, una estrategia puede considerar liberaciones semanales, mientras que otra podría utilizar periodos diferentes si los datos biológicos y operativos disponibles lo permiten.

La frecuencia definitiva deberá ser compatible con la supervivencia de los machos estériles y con la disponibilidad de producción.

### 4.6.5 Intervalo entre liberaciones

La variable \(\Delta t_R\) representa el tiempo transcurrido entre una liberación y la siguiente.

$$
\Delta t_R=\text{intervalo entre liberaciones}
$$

Unidad:

$$
\text{tiempo}
$$

Esta variable permitirá comparar estrategias con diferentes periodicidades de liberación.

Existe una relación conceptual entre la frecuencia y el intervalo:

$$
f_R\propto\frac{1}{\Delta t_R}
$$

La relación exacta dependerá de la unidad temporal utilizada en la simulación.

### 4.6.6 Duración de la estrategia

La variable \(T_R\) representa el periodo durante el cual se mantiene activa una estrategia de liberación.

$$
T_R=\text{duración de la estrategia de liberación}
$$

Unidad:

$$
\text{tiempo}
$$

Esta variable permitirá evaluar estrategias de distinta duración y determinar si una determinada cantidad y frecuencia de liberación permite alcanzar el criterio de control o erradicación.

### 4.6.7 Proporción de machos estériles respecto a silvestres

La variable \(\rho_t\) representa la proporción de machos estériles respecto a machos silvestres durante el periodo \(t\):

$$
\rho_t=\frac{M_s(t)}{M_w(t)}
$$

Esta variable será utilizada para evaluar la intensidad de la estrategia de liberación en relación con el tamaño de la población silvestre.

La proporción de referencia:

$$
\rho_{ref}=10:1
$$

será considerada como un escenario o referencia operativa para determinadas condiciones y no como una condición universal que deba cumplirse durante toda la simulación.

### 4.6.8 Acumulación de liberaciones

La variable \(R_{total}\) representa la cantidad acumulada de moscas estériles liberadas durante toda la simulación.

$$
R_{total}=\sum_t R_t
$$

Unidad:

$$
\text{moscas}
$$

Esta variable permitirá comparar el consumo total de moscas entre diferentes estrategias.

### 4.6.9 Utilización de la capacidad de producción

La variable \(U_C\) representa la proporción de la capacidad de producción disponible que fue utilizada por una estrategia durante el periodo de simulación.

Se define como:

$$
U_C=
\frac{\sum_t R_t}
{\sum_t C_t}
$$

donde:

* \(U_C\) = utilización de la capacidad disponible;
* \(R_t\) = cantidad liberada durante el periodo \(t\);
* \(C_t\) = producción disponible durante el periodo \(t\).

Esta variable permitirá determinar qué tan intensivamente utiliza una estrategia la capacidad de producción de la planta.

### 4.6.10 Variables de estrategia

Una estrategia de liberación podrá representarse mediante el conjunto:

$$
S_R=\{R_t,\Delta t_R,T_R\}
$$

donde:

* \(R_t\) = cantidad de moscas liberadas;
* \(\Delta t_R\) = intervalo entre liberaciones;
* \(T_R\) = duración de la estrategia.

Posteriormente, el simulador podrá modificar estos valores para comparar diferentes estrategias bajo las mismas condiciones iniciales.

### 4.6.11 Relación entre producción y liberación

La relación general entre las variables será:

$$
C_t\rightarrow A_t\rightarrow R_t\rightarrow M_s(t)
$$

donde:

* \(C_t\) representa la producción disponible;
* \(A_t\) representa la cantidad disponible para la estrategia;
* \(R_t\) representa la cantidad efectivamente liberada;
* \(M_s(t)\) representa los machos estériles presentes en el sistema después de considerar las liberaciones y pérdidas.

Esta estructura permitirá que el modelo evalúe estrategias de control que sean compatibles con la capacidad de producción de la planta de Metapa.

### 4.6.12 Consideraciones para la simulación

Las variables de producción y liberación podrán modificarse de acuerdo con los escenarios planteados en el proyecto.

Entre los escenarios iniciales se consideran:

* producción de 28 millones de moscas por semana;
* incremento progresivo de la producción;
* producción de 100 millones de moscas por semana;
* posible expansión a 120 millones de moscas por semana;
* diferentes cantidades de moscas liberadas;
* diferentes frecuencias de liberación;
* diferentes duraciones de las estrategias.

La selección de una estrategia no se realizará únicamente con base en la cantidad de moscas disponibles. También deberá considerarse el efecto obtenido sobre la población silvestre, el tiempo necesario para alcanzar el criterio establecido y la cantidad total de moscas utilizadas.

Por lo tanto, las variables de producción y liberación permitirán posteriormente comparar la **viabilidad productiva** de una estrategia con su **eficacia poblacional**.

## 4.7 Variables de salida

Las variables de salida representan los resultados obtenidos a partir de la ejecución del modelo matemático y permiten evaluar el comportamiento de la población de gusano barrenador del ganado (GBG) bajo diferentes estrategias de liberación de moscas estériles.

Estas variables serán utilizadas para comparar escenarios y determinar la eficacia y viabilidad de las estrategias de control consideradas.

Las variables de salida podrán ser calculadas a partir de las variables de estado, los parámetros biológicos, las restricciones de producción de la planta de Metapa y las condiciones definidas para cada escenario.

### 4.7.1 Población silvestre total

La variable \(N_w(t)\) representa la cantidad total de individuos adultos de GBG pertenecientes a la población silvestre durante el tiempo \(t\).

Para la estructura inicial propuesta:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

donde:

* \(N_w(t)\) = población adulta silvestre total;
* \(M_w(t)\) = machos silvestres fértiles;
* \(F_v(t)\) = hembras silvestres vírgenes;
* \(F_m(t)\) = hembras silvestres apareadas.

Unidad:

$$
\text{individuos}
$$

Esta será una de las principales variables para evaluar si la población silvestre está disminuyendo como consecuencia de la estrategia de liberación.

### 4.7.2 Población de machos estériles

La variable \(M_s(t)\) representa la cantidad de machos estériles presentes en el sistema durante el tiempo \(t\).

$$
M_s(t)=\text{machos estériles presentes en el sistema}
$$

Unidad:

$$
\text{individuos}
$$

Su comportamiento permitirá analizar si la cantidad de individuos estériles disponibles es suficiente para mantener una presión reproductiva sobre la población silvestre.

### 4.7.3 Proporción estéril:silvestre

La variable \(\rho(t)\) representa la proporción entre machos estériles y machos silvestres:

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

Esta variable permitirá observar cómo cambia la relación entre ambas poblaciones durante la simulación.

Será especialmente útil para comparar estrategias con diferentes cantidades y frecuencias de liberación.

### 4.7.4 Cantidad de moscas liberadas por periodo

La variable \(R_t\) permitirá conocer la cantidad de moscas estériles liberadas durante cada periodo de la simulación.

$$
R_t=\text{cantidad de moscas liberadas durante }t
$$

Unidad:

$$
\text{moscas/periodo}
$$

Esta variable permitirá visualizar la distribución temporal de las liberaciones y comprobar que la estrategia respete las restricciones de producción establecidas.

### 4.7.5 Cantidad total de moscas liberadas

La variable \(R_{total}\) representa la cantidad acumulada de moscas estériles utilizadas durante toda la simulación:

$$
R_{total}=\sum_tR_t
$$

Unidad:

$$
\text{moscas}
$$

Este resultado permitirá comparar el consumo total de moscas entre diferentes estrategias.

Una estrategia que requiera menos moscas para alcanzar el mismo criterio de control podrá considerarse más eficiente desde el punto de vista del uso del recurso, siempre que también cumpla con las demás condiciones del modelo.

### 4.7.6 Tiempo para alcanzar el criterio de control

La variable \(T_C\) representa el tiempo necesario para que la población silvestre alcance el criterio de control establecido.

$$
T_C=\text{tiempo necesario para alcanzar el criterio de control}
$$

Unidad:

$$
\text{tiempo}
$$

El valor concreto del criterio de control será definido posteriormente con base en la información científica disponible.

### 4.7.7 Tiempo para alcanzar el criterio de erradicación

La variable \(T_E\) representa el tiempo necesario para que la población silvestre alcance el criterio de erradicación establecido para el modelo.

$$
T_E=\text{tiempo necesario para alcanzar el criterio de erradicación}
$$

Unidad:

$$
\text{tiempo}
$$

Esta variable constituye uno de los resultados principales del proyecto, ya que permitirá estimar cuánto tiempo podría requerir una estrategia determinada para alcanzar el objetivo establecido.

El criterio matemático de erradicación todavía deberá definirse y justificarse científicamente. Por lo tanto, no se asumirá automáticamente que:

$$
N_w(t)=0
$$

sea la única condición válida.

### 4.7.8 Utilización de la capacidad de producción

La variable \(U_C\) representa la proporción de la capacidad de producción de la planta utilizada por una estrategia durante el periodo de simulación.

$$
U_C=
\frac{\sum_tR_t}
{\sum_tC_t}
$$

Unidad:

$$
\text{proporción}
$$

También podrá expresarse como porcentaje:

$$
U_C(\%)=
\frac{\sum_tR_t}
{\sum_tC_t}\times100
$$

Esta variable permitirá determinar qué tan intensivamente una estrategia utiliza la producción disponible de la planta de Metapa.

### 4.7.9 Población de hospedadores infestados

Las variables \(I_b(t)\) e \(I_p(t)\) podrán utilizarse como resultados epidemiológicos cuando el modelo incorpore una capa explícita de infestación.

$$
I_b(t)=\text{bovinos infestados}
$$

$$
I_p(t)=\text{porcinos infestados}
$$

Unidad:

$$
\text{animales}
$$

Estas variables permitirán analizar la posible relación entre la reducción de la población de GBG y la disminución de las infestaciones en los hospedadores.

Sin embargo, su inclusión como salida dependerá de la disponibilidad y calidad de los datos epidemiológicos.

### 4.7.10 Estado final de la población

La variable \(N_{w,f}\) representa la población silvestre al finalizar el periodo de simulación:

$$
N_{w,f}=N_w(T)
$$

donde \(T\) representa el tiempo final de la simulación.

Esta variable permitirá determinar si la estrategia consiguió alcanzar el criterio de control o erradicación dentro del periodo evaluado.

### 4.7.11 Indicadores de eficiencia de la estrategia

A partir de las variables anteriores podrán calcularse indicadores para comparar estrategias.

Entre ellos se consideran inicialmente:

* población silvestre final;
* tiempo para alcanzar el criterio de control;
* tiempo para alcanzar el criterio de erradicación;
* cantidad total de moscas liberadas;
* utilización de la capacidad de producción;
* proporción máxima y promedio de machos estériles respecto a silvestres;
* comportamiento temporal de la población silvestre.

Estos indicadores permitirán realizar comparaciones entre escenarios sin limitar la evaluación únicamente a la cantidad de moscas liberadas.

### 4.7.12 Conjunto mínimo de resultados

Como resultado mínimo de cada simulación, el modelo deberá generar:

$$
\{N_w(t),M_s(t),\rho(t),R_t,R_{total},T_E,U_C\}
$$

y, cuando los datos epidemiológicos permitan incorporarlos:

$$
\{I_b(t),I_p(t)\}
$$

Este conjunto de resultados constituirá la base para las tablas, gráficas y comparaciones que posteriormente utilizará el simulador y, en una etapa posterior, la plataforma web.

### 4.7.13 Consideraciones para la interpretación

Las variables de salida representan resultados del modelo y no observaciones directas de la realidad.

Por esta razón, los resultados deberán interpretarse de acuerdo con:

* los parámetros utilizados;
* las condiciones iniciales;
* los supuestos establecidos;
* la estrategia de liberación;
* la capacidad de producción considerada;
* la incertidumbre de los parámetros;
* la calidad de los datos utilizados para la parametrización.

Las estimaciones de tiempo para control o erradicación deberán presentarse como resultados condicionados al escenario simulado y no como predicciones absolutas del comportamiento del GBG en México.

## 4.8 Clasificación de variables

Las variables identificadas para el modelo se clasifican de acuerdo con la función que desempeñan dentro de la simulación. Esta clasificación permite diferenciar las cantidades que describen el estado del sistema, las acciones externas utilizadas para modificarlo y los resultados obtenidos después de ejecutar el modelo.

La clasificación podrá modificarse durante la formulación matemática si se determina que alguna variable cumple una función diferente o no es necesaria para el modelo definitivo.

### 4.8.1 Variables de estado

Las variables de estado representan cantidades que describen el estado del sistema en un momento determinado y cuyo valor cambia durante la simulación.

Inicialmente se consideran:

| Variable                   | Símbolo    | Descripción                                                       | Unidad     |
| -------------------------- | ---------- | ----------------------------------------------------------------- | ---------- |
| Machos silvestres fértiles | \(M_w(t)\) | Machos silvestres reproductivamente disponibles                   | individuos |
| Hembras vírgenes           | \(F_v(t)\) | Hembras silvestres adultas que aún no se han apareado             | individuos |
| Hembras apareadas          | \(F_m(t)\) | Hembras silvestres que ya han sido apareadas                      | individuos |
| Machos estériles           | \(M_s(t)\) | Machos estériles presentes después de las liberaciones y pérdidas | individuos |

Estas variables constituyen el conjunto inicial de candidatos para formar el vector de estado del modelo:

$$
X(t)=
\begin{bmatrix}
M_w(t)\\
F_v(t)\\
F_m(t)\\
M_s(t)
\end{bmatrix}
$$

La composición definitiva del vector de estado se establecerá en la formulación del modelo matemático.

### 4.8.2 Variables de entrada y control

Las variables de entrada y control representan condiciones externas o decisiones establecidas antes o durante una simulación.

Entre ellas se considera principalmente:

| Variable                       | Símbolo        | Descripción                                    | Unidad               |
| ------------------------------ | -------------- | ---------------------------------------------- | -------------------- |
| Liberación de moscas estériles | \(R_t\)        | Cantidad liberada durante el periodo \(t\)     | moscas/periodo       |
| Frecuencia de liberación       | \(f_R\)        | Número de liberaciones por periodo             | liberaciones/periodo |
| Intervalo de liberación        | \(\Delta t_R\) | Tiempo entre liberaciones                      | tiempo               |
| Duración de la estrategia      | \(T_R\)        | Tiempo durante el cual se aplica la estrategia | tiempo               |

Estas variables podrán modificarse para construir diferentes estrategias de control.

### 4.8.3 Variables de producción

Las variables de producción representan las restricciones relacionadas con la disponibilidad de moscas estériles provenientes de la planta de Metapa.

| Variable       | Símbolo | Descripción                                   | Unidad         |
| -------------- | ------- | --------------------------------------------- | -------------- |
| Producción     | \(C_t\) | Cantidad producida o disponible durante \(t\) | moscas/periodo |
| Disponibilidad | \(A_t\) | Cantidad disponible para una estrategia       | moscas/periodo |

Estas variables deberán respetar:

$$
A_t\leq C_t
$$

y:

$$
R_t\leq A_t
$$

por lo que:

$$
R_t\leq A_t\leq C_t
$$

La capacidad de producción considerada corresponde exclusivamente a la planta de Metapa de Domínguez, Chiapas.

### 4.8.4 Variables epidemiológicas

Las variables epidemiológicas representan la interacción del GBG con los hospedadores considerados en el proyecto.

| Variable            | Símbolo    | Descripción                           | Unidad   |
| ------------------- | ---------- | ------------------------------------- | -------- |
| Población bovina    | \(B(t)\)   | Bovinos considerados en el escenario  | animales |
| Bovinos infestados  | \(I_b(t)\) | Bovinos con infestación por GBG       | animales |
| Población porcina   | \(P(t)\)   | Porcinos considerados en el escenario | animales |
| Porcinos infestados | \(I_p(t)\) | Porcinos con infestación por GBG      | animales |

Estas variables podrán funcionar como variables de estado, observacionales, auxiliares o de validación, dependiendo de la disponibilidad de datos y de la estructura final del modelo.

### 4.8.5 Variables auxiliares o derivadas

Las variables auxiliares o derivadas son aquellas cuyo valor puede calcularse a partir de otras variables y parámetros del modelo.

Entre ellas se consideran:

| Variable                                   | Símbolo     | Definición                                |
| ------------------------------------------ | ----------- | ----------------------------------------- |
| Población silvestre adulta total           | \(N_w(t)\)  | \(M_w(t)+F_v(t)+F_m(t)\)                  |
| Proporción estéril:silvestre               | \(\rho(t)\) | \(M_s(t)/M_w(t)\)                         |
| Proporción de apareamientos con estériles  | \(p_s(t)\)  | Función de \(M_s(t)\), \(M_w(t)\) y \(c\) |
| Proporción de apareamientos con silvestres | \(p_w(t)\)  | \(1-p_s(t)\)                              |
| Apareamientos con machos silvestres        | \(A_w(t)\)  | Derivada de la dinámica de apareamiento   |
| Apareamientos con machos estériles         | \(A_s(t)\)  | Derivada de la dinámica de apareamiento   |

Estas variables no necesariamente requieren ecuaciones diferenciales independientes.

### 4.8.6 Variables de salida

Las variables de salida representan los resultados principales obtenidos al finalizar o durante una simulación.

| Variable                    | Símbolo       | Descripción                                      | Unidad     |
| --------------------------- | ------------- | ------------------------------------------------ | ---------- |
| Tiempo de control           | \(T_C\)       | Tiempo para alcanzar el criterio de control      | tiempo     |
| Tiempo de erradicación      | \(T_E\)       | Tiempo para alcanzar el criterio de erradicación | tiempo     |
| Moscas liberadas acumuladas | \(R_{total}\) | Total de moscas liberadas                        | moscas     |
| Utilización de capacidad    | \(U_C\)       | Proporción de capacidad productiva utilizada     | proporción |
| Población final             | \(N_{w,f}\)   | Población silvestre al final de la simulación    | individuos |

Estas variables permitirán comparar diferentes estrategias de liberación.

### 4.8.7 Clasificación general

De manera resumida, la estructura de variables del modelo queda inicialmente organizada de la siguiente manera:

```text
VARIABLES DEL MODELO
│
├── Variables de estado
│   ├── Mw(t)
│   ├── Fv(t)
│   ├── Fm(t)
│   └── Ms(t)
│
├── Variables de entrada/control
│   ├── Rt
│   ├── fR
│   ├── ΔtR
│   └── TR
│
├── Variables de producción
│   ├── Ct
│   └── At
│
├── Variables epidemiológicas
│   ├── B(t)
│   ├── Ib(t)
│   ├── P(t)
│   └── Ip(t)
│
├── Variables auxiliares/derivadas
│   ├── Nw(t)
│   ├── ρ(t)
│   ├── ps(t)
│   └── pw(t)
│
└── Variables de salida
    ├── TC
    ├── TE
    ├── Rtotal
    ├── UC
    └── Nw,f
```

### 4.8.8 Consideraciones para la clasificación definitiva

La clasificación presentada es una estructura inicial y no implica que todas las variables deban formar parte del sistema principal de ecuaciones diferenciales.

En particular, las variables epidemiológicas relacionadas con bovinos y porcinos podrán mantenerse como una capa independiente u observacional si los datos disponibles no permiten incorporarlas de manera confiable a la dinámica poblacional del GBG.

Asimismo, las variables auxiliares y de salida serán calculadas a partir de las variables de estado y de los parámetros correspondientes.

La estructura definitiva deberá priorizar un modelo suficientemente detallado para representar el efecto de la TIE, pero sin incorporar variables que no puedan ser respaldadas por datos o evidencia científica.

## 4.9 Variables confirmadas y pendientes

Las variables identificadas para el modelo no cuentan actualmente con el mismo nivel de información disponible. Algunas pueden definirse y parametrizarse a partir de información oficial o científica, mientras que otras requieren obtener datos adicionales antes de incorporarse al sistema matemático definitivo.

Por esta razón, las variables se clasifican inicialmente en **confirmadas**, **pendientes de parametrización** y **condicionadas a disponibilidad de datos**.

### 4.9.1 Variables confirmadas

Las variables confirmadas son aquellas cuya definición dentro del modelo puede establecerse con la información disponible actualmente y cuyos valores de referencia cuentan con respaldo documental.

| Variable                                   | Símbolo        | Situación actual                             |
| ------------------------------------------ | -------------- | -------------------------------------------- |
| Producción inicial reportada               | \(C_{ini}\)    | 28 millones de moscas/semana                 |
| Capacidad proyectada                       | \(C_{max}\)    | 100 millones de moscas/semana                |
| Posible capacidad futura                   | \(C_{fut}\)    | 120 millones de moscas/semana como escenario |
| Cantidad del primer lote mexicano liberado | \(R_{obs}\)    | 2.5 millones de moscas                       |
| Proporción operativa de referencia         | \(\rho_{ref}\) | 10:1 en determinadas áreas de baja densidad  |
| Machos silvestres                          | \(M_w(t)\)     | Variable de estado candidata                 |
| Hembras vírgenes                           | \(F_v(t)\)     | Variable de estado candidata                 |
| Hembras apareadas                          | \(F_m(t)\)     | Variable de estado candidata                 |
| Machos estériles                           | \(M_s(t)\)     | Variable de estado candidata                 |
| Moscas liberadas                           | \(R_t\)        | Variable de control                          |
| Población silvestre total                  | \(N_w(t)\)     | Variable derivada                            |

Los valores de producción corresponden exclusivamente a la planta de Metapa de Domínguez, Chiapas.

La existencia y definición de estas variables están respaldadas por la información recopilada durante las etapas anteriores del proyecto.

### 4.9.2 Variables pendientes de parametrización

Las variables pendientes de parametrización cuentan con una definición conceptual, pero todavía requieren determinar un valor, rango o función que pueda utilizarse de manera justificada en la simulación.

Entre ellas se encuentran:

#### Variables biológicas

* \(M_w(0)\): población inicial de machos silvestres.
* \(F_v(0)\): población inicial de hembras vírgenes.
* \(F_m(0)\): población inicial de hembras apareadas.
* \(d_L\): duración del desarrollo larvario.
* \(d_P\): duración de la etapa pupal.
* \(d_A\): duración de la etapa adulta.
* \(b\): fecundidad.
* \(r\): proporción sexual.
* \(\mu_M\): mortalidad de machos silvestres.
* \(\mu_F\): mortalidad de hembras.
* \(S_L\): supervivencia larvaria.
* \(S_P\): supervivencia pupal.
* \(S_A\): supervivencia adulta.

#### Variables relacionadas con la TIE

* \(S_s\): supervivencia de machos estériles.
* \(\mu_s\): mortalidad de machos estériles.
* \(c\): competitividad relativa de los machos estériles.
* \(E_s\): eficacia de la esterilización.
* \(p_s(t)\): proporción de apareamientos con machos estériles.
* \(p_w(t)\): proporción de apareamientos con machos silvestres.

Las variables \(p_s(t)\) y \(p_w(t)\) pueden calcularse a partir de otras variables y parámetros, pero la función utilizada para representarlas todavía deberá validarse.

#### Variables epidemiológicas

* \(B(t)\): población bovina.
* \(P(t)\): población porcina.
* \(I_b(t)\): bovinos infestados.
* \(I_p(t)\): porcinos infestados.
* \(\lambda_b(t)\): tasa de infestación bovina.
* \(\lambda_p(t)\): tasa de infestación porcina.
* \(p_b(t)\): probabilidad o proporción de infestación bovina.
* \(p_p(t)\): probabilidad o proporción de infestación porcina.
* \(\gamma_b(t)\): tasa de salida de bovinos infestados.
* \(\gamma_p(t)\): tasa de salida de porcinos infestados.

### 4.9.3 Variables dependientes de la estrategia

Algunas variables no tendrán un valor único para todo el proyecto, debido a que serán modificadas de acuerdo con el escenario de simulación.

Entre ellas:

$$
R_t
$$

$$
f_R
$$

$$
\Delta t_R
$$

$$
T_R
$$

$$
A_t
$$

$$
C_t
$$

$$
\rho(t)
$$

Estas variables permitirán construir diferentes estrategias de producción y liberación.

Por ejemplo, una simulación podrá utilizar una determinada cantidad de moscas liberadas semanalmente, mientras que otra podrá modificar tanto la cantidad como la frecuencia de liberación.

### 4.9.4 Variables que se obtendrán mediante cálculo

Algunas variables no requieren un valor inicial proporcionado directamente por una fuente, ya que serán calculadas durante la simulación.

Entre ellas:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

$$
p_w(t)=1-p_s(t)
$$

$$
R_{total}=\sum_tR_t
$$

$$
U_C=
\frac{\sum_tR_t}{\sum_tC_t}
$$

Además, el tiempo necesario para alcanzar los criterios establecidos se obtendrá mediante la simulación:

$$
T_C=\text{tiempo hasta alcanzar el criterio de control}
$$

$$
T_E=\text{tiempo hasta alcanzar el criterio de erradicación}
$$

### 4.9.5 Variables que requieren datos iniciales

Uno de los aspectos más importantes antes de ejecutar el modelo será determinar las condiciones iniciales de la población.

Se requiere establecer, cuando los datos disponibles lo permitan:

$$
M_w(0)
$$

$$
F_v(0)
$$

$$
F_m(0)
$$

$$
M_s(0)
$$

En el caso de \(M_s(0)\), podrá establecerse de acuerdo con el momento en que inicia la estrategia de liberación.

La población inicial de GBG silvestre no deberá obtenerse mediante una conversión arbitraria de animales infestados a número de moscas.

Cuando no exista una estimación directa, será necesario utilizar un método científicamente justificado, un rango de valores o escenarios de población inicial.

### 4.9.6 Variables sujetas a validación

Las variables y relaciones matemáticas que presenten mayor incertidumbre deberán someterse posteriormente a un proceso de validación.

Entre las más importantes se encuentran:

* población inicial de GBG;
* tasa de reproducción;
* mortalidad de adultos;
* competitividad de machos estériles;
* supervivencia de machos estériles;
* eficacia de la esterilización;
* relación entre infestación de hospedadores y población de GBG;
* frecuencia óptima de liberación;
* criterio de control;
* criterio de erradicación.

Estas variables tendrán prioridad durante la búsqueda de información científica y durante las pruebas del modelo.

### 4.9.7 Estado de preparación de las variables

Para facilitar el desarrollo posterior del modelo, se utilizarán tres estados:

**CONFIRMADA**

La variable cuenta con definición y respaldo suficiente para ser incorporada al modelo o utilizarse como referencia.

**PENDIENTE**

La variable está identificada, pero todavía requiere valor, rango, función o fuente suficiente.

**CONDICIONADA**

La variable podrá incorporarse dependiendo de la disponibilidad de datos y de la estructura matemática definitiva.

Esta clasificación permitirá evitar que una variable sea utilizada únicamente porque resulta conveniente para la simulación.

### 4.9.8 Regla para incorporar una variable al modelo

Una variable podrá considerarse lista para su incorporación al modelo matemático cuando se disponga, como mínimo, de:

1. Definición clara.
2. Símbolo.
3. Unidad de medida.
4. Valor, rango o función.
5. Fuente o método de estimación.
6. Justificación de su inclusión.
7. Relación con otras variables.
8. Tratamiento de su incertidumbre cuando corresponda.

Si alguno de estos elementos no está disponible, la variable deberá permanecer como pendiente o condicionada hasta obtener información suficiente.

### 4.9.9 Consideración sobre la incertidumbre

La ausencia de un valor único no significa que una variable deba ser eliminada automáticamente del modelo.

Cuando exista evidencia científica de un intervalo de valores, se podrá representar mediante:

$$
x\in[x_{min},x_{max}]
$$

y posteriormente evaluar diferentes escenarios.

De esta manera, el modelo podrá analizar cómo cambia el resultado cuando existe incertidumbre en determinados parámetros o variables.

Esta estrategia será especialmente importante para variables biológicas y de TIE que puedan presentar variabilidad entre condiciones experimentales o ambientales.

### 4.9.10 Estado actual

Al finalizar esta etapa, las variables del modelo se encuentran identificadas y clasificadas, pero no todas están listas para utilizarse en las ecuaciones definitivas.

El siguiente paso será construir una matriz maestra de variables que concentre su símbolo, unidad, clasificación, estado, fuente y función dentro del modelo.

La formulación matemática deberá utilizar únicamente las variables que resulten necesarias y que puedan ser justificadas mediante evidencia científica, datos oficiales o supuestos explícitamente documentados.

## 4.10 Matriz maestra de variables

La matriz maestra de variables concentra las variables identificadas para la formulación del modelo matemático, indicando su símbolo, unidad, clasificación, estado actual y función dentro de la simulación.

Esta matriz constituye un instrumento de trazabilidad para evitar inconsistencias entre la documentación, las ecuaciones matemáticas y la implementación computacional.

### 4.10.1 Matriz general

| Variable                               | Símbolo        | Unidad               | Clasificación  | Estado              | Función                                            |
| -------------------------------------- | -------------- | -------------------- | -------------- | ------------------- | -------------------------------------------------- |
| Machos silvestres fértiles             | \(M_w(t)\)     | individuos           | Estado         | Pendiente           | Representar la población masculina silvestre       |
| Hembras vírgenes                       | \(F_v(t)\)     | individuos           | Estado         | Pendiente           | Representar hembras disponibles para apareamiento  |
| Hembras apareadas                      | \(F_m(t)\)     | individuos           | Estado         | Pendiente           | Representar hembras que ya tuvieron apareamiento   |
| Machos estériles                       | \(M_s(t)\)     | individuos           | Estado         | Pendiente           | Representar la población estéril presente          |
| Población bovina                       | \(B(t)\)       | animales             | Epidemiológica | Condicionada        | Representar hospedadores bovinos                   |
| Bovinos infestados                     | \(I_b(t)\)     | animales             | Epidemiológica | Condicionada        | Representar infestaciones en bovinos               |
| Población porcina                      | \(P(t)\)       | animales             | Epidemiológica | Condicionada        | Representar hospedadores porcinos                  |
| Porcinos infestados                    | \(I_p(t)\)     | animales             | Epidemiológica | Condicionada        | Representar infestaciones en porcinos              |
| Producción disponible                  | \(C_t\)        | moscas/periodo       | Producción     | Confirmada/variable | Representar la producción disponible de Metapa     |
| Disponibilidad                         | \(A_t\)        | moscas/periodo       | Producción     | Variable            | Representar moscas disponibles para una estrategia |
| Liberación                             | \(R_t\)        | moscas/periodo       | Control        | Variable            | Representar las moscas liberadas                   |
| Frecuencia de liberación               | \(f_R\)        | liberaciones/periodo | Control        | Variable            | Definir periodicidad de liberación                 |
| Intervalo de liberación                | \(\Delta t_R\) | tiempo               | Control        | Variable            | Definir tiempo entre liberaciones                  |
| Duración de estrategia                 | \(T_R\)        | tiempo               | Control        | Variable            | Definir duración de la estrategia                  |
| Población silvestre total              | \(N_w(t)\)     | individuos           | Derivada       | Calculada           | Representar población adulta silvestre total       |
| Proporción estéril:silvestre           | \(\rho(t)\)    | razón                | Derivada       | Calculada           | Evaluar presión relativa de machos estériles       |
| Apareamientos silvestres               | \(A_w(t)\)     | apareamientos/tiempo | Auxiliar       | Calculada           | Representar apareamientos con machos fértiles      |
| Apareamientos estériles                | \(A_s(t)\)     | apareamientos/tiempo | Auxiliar       | Calculada           | Representar apareamientos con machos estériles     |
| Proporción de apareamientos estériles  | \(p_s(t)\)     | proporción           | Derivada       | Calculada           | Determinar participación de machos estériles       |
| Proporción de apareamientos silvestres | \(p_w(t)\)     | proporción           | Derivada       | Calculada           | Determinar participación de machos fértiles        |
| Población final                        | \(N_{w,f}\)    | individuos           | Salida         | Calculada           | Evaluar población al final de la simulación        |
| Tiempo de control                      | \(T_C\)        | tiempo               | Salida         | Calculada           | Determinar tiempo para alcanzar control            |
| Tiempo de erradicación                 | \(T_E\)        | tiempo               | Salida         | Calculada           | Determinar tiempo para alcanzar erradicación       |
| Moscas liberadas acumuladas            | \(R_{total}\)  | moscas               | Salida         | Calculada           | Determinar consumo total                           |
| Utilización de capacidad               | \(U_C\)        | proporción           | Salida         | Calculada           | Evaluar uso de la capacidad productiva             |

### 4.10.2 Variables de estado principales

Para la formulación inicial se propone utilizar como conjunto principal de variables de estado:

$$
X(t)=
\begin{bmatrix}
M_w(t)\\
F_v(t)\\
F_m(t)\\
M_s(t)
\end{bmatrix}
$$

Estas variables representan la población adulta silvestre y estéril que participa directamente en la dinámica reproductiva del modelo.

La inclusión definitiva de cada variable será validada durante la formulación de las ecuaciones.

### 4.10.3 Variables de entrada

Las principales variables que podrán modificarse entre escenarios serán:

$$
R_t,\quad f_R,\quad \Delta t_R,\quad T_R
$$

Estas variables permitirán representar diferentes estrategias de liberación.

La producción de la planta funcionará como una restricción:

$$
R_t\leq A_t\leq C_t
$$

### 4.10.4 Variables derivadas principales

Las principales variables calculadas a partir del modelo serán:

$$
N_w(t)=M_w(t)+F_v(t)+F_m(t)
$$

$$
\rho(t)=\frac{M_s(t)}{M_w(t)}
$$

$$
p_s(t)=
\frac{cM_s(t)}
{M_w(t)+cM_s(t)}
$$

$$
p_w(t)=1-p_s(t)
$$

Estas variables permitirán analizar la interacción entre la población silvestre y los machos estériles.

### 4.10.5 Variables de producción

La estructura de producción y liberación queda representada mediante:

$$
C_t\rightarrow A_t\rightarrow R_t\rightarrow M_s(t)
$$

donde:

* \(C_t\) representa la producción disponible;
* \(A_t\) representa la cantidad disponible para una estrategia;
* \(R_t\) representa la cantidad liberada;
* \(M_s(t)\) representa los machos estériles presentes después de considerar las liberaciones y pérdidas.

Esta separación será utilizada posteriormente en la implementación computacional.

### 4.10.6 Variables de salida principales

Cada simulación deberá generar como mínimo información relacionada con:

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
T_E
$$

$$
U_C
$$

Además, cuando la estructura epidemiológica y los datos disponibles lo permitan, podrán incorporarse:

$$
I_b(t)
$$

$$
I_p(t)
$$

### 4.10.7 Relación entre variables

La estructura general del modelo puede representarse conceptualmente como:

```text
                 PARÁMETROS
                     │
                     ▼
              ┌─────────────┐
              │    MODELO   │
              │ MATEMÁTICO  │
              └─────────────┘
                 ▲       ▲
                 │       │
        POBLACIÓN│       │LIBERACIÓN
                 │       │
        ┌────────┘       └────────┐
        │                         │
        ▼                         ▼
   Población                 Producción
   silvestre                 de Metapa
        │                         │
        │                         ▼
        │                    Disponibilidad
        │                         │
        │                         ▼
        │                     Liberación
        │                         │
        ▼                         ▼
     ┌──────────────────────────────┐
     │       Dinámica de la TIE      │
     └──────────────────────────────┘
                    │
                    ▼
               RESULTADOS
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        Nw(t)      TE       Rtotal
```

### 4.10.8 Criterio para la actualización de la matriz

La matriz deberá actualizarse cuando se obtenga nueva información científica, epidemiológica u operativa que modifique:

* el valor de una variable;
* su rango;
* su unidad;
* su clasificación;
* su función dentro del modelo;
* su fuente;
* su nivel de incertidumbre.

Los cambios deberán mantenerse consistentes con la matriz maestra de parámetros establecida en `03_parametros.md`.

### 4.10.9 Relación con la implementación en Python

La matriz maestra servirá como referencia para organizar posteriormente las variables dentro del código.

De manera conceptual, la estructura podrá representarse como:

```text
variables/
├── estado
│   ├── Mw
│   ├── Fv
│   ├── Fm
│   └── Ms
│
├── control
│   ├── Rt
│   ├── fR
│   ├── ΔtR
│   └── TR
│
├── epidemiologicas
│   ├── B
│   ├── Ib
│   ├── P
│   └── Ip
│
├── derivadas
│   ├── Nw
│   ├── rho
│   ├── ps
│   └── pw
│
└── salidas
    ├── TC
    ├── TE
    ├── Rtotal
    ├── UC
    └── Nwf
```

Esta estructura es conceptual y no representa todavía la organización definitiva de los módulos de Python.

### 4.10.10 Estado final del documento de variables

Con esta matriz se concluye la identificación y clasificación inicial de las variables necesarias para el proyecto.

El documento `04_variables.md` establece:

* qué cantidades representan el estado de la población;
* qué variables controlan las estrategias de liberación;
* qué variables representan la producción de la planta de Metapa;
* qué variables representan la relación con bovinos y porcinos;
* qué variables son calculadas;
* qué resultados deberá producir la simulación.

La estructura definitiva de las variables dependerá de la formulación matemática desarrollada en el siguiente documento.

El siguiente paso del proyecto será establecer las relaciones matemáticas entre estas variables y construir el sistema de ecuaciones que describirá la dinámica poblacional del GBG y el efecto de la TIE.

