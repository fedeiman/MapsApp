# Demo

## Tareas Realizadas:

  

#### Backend:

  

+ Implementación mapa de la argentina dividido por distintos tipos de regiones con distintas granularidades como por ejemplo por Provincia, departamento, según regiones (cuyo , etc)

+ Realizar búsquedas mediante coordenadas (A partir de una latitud y longitud mostramos en el mapa donde físicamente esta ubicado mas el nombre especifico del lugar prov,ciudad,departamento.etc). Esto se logro gracias a usar una API publica georef del gobierno de la nación

+ A partir de distintas fuentes recolectamos todo tipo de datos influyentes en el indice de calidad de vida (ICV) ordenados según provincias,obtenidos por censos nacionales y otros estudios poblacionales realizados en los últimos años.

+ Manejamos estas tablas (CSV) mediante un script de python recolectando los datos mas influyentes de cada tabla y con ayuda de geojsons y la API georef enlazamos cada uno de estos datos relevantes con su ubicación, mostrando de esta forma el nombre de la provincia, departamento y otros datos geográficos conjuntamente con datos relacionados al ICV.

  

#### Frontend:

+ Utilizamos la librería leaflet de JavaScript para poder mostrar un mapa de Argentina dividido mediante distintos grupos de coordenadas, lo que muestran distintas regiones según se desee, cada región queda delimitada por un color especifico

+ Cada vez que se realiza la acción "mouseover" sobre una región especifica se le hace una request manejada por el backend la cual responde los datos disponibles de cada región.

+ Enlazamos entre si los distintos tipos de mapas con la finalidad de poder cambiar entre ellos y ver los datos disponibles segun distintos tipos de clasificaciones geográficas.

  
  

#### Predicción de datos:

+ Aprendimos el uso de la interfaz watson de IBM la cual entrena modelos de inteligencia artificial mediante datasets brindados por el usuario.

+ Con nuestros CSVs de distintos tipos de datos relacionados al ICV entrenamos modelos específicos para predecir datos que podrían ser relevantes utilizando parte de los conocimientos obtenidos en kaggle para saber que columnas necesitamos y cual de los modelos obtenidos por Watson es conveniente usar.

+ Planteamos otra posible solución al problema usando formulas matemáticas de interpolación y extrapolación. Estas formulas se pueden hacer para calcular por si sola las variables a usar en el modelo, para predecir un valor "target" (Caso en que el usuario no sepa exactamente que dato poner, esto mostraría el mas parecido al "deseado") o simplemente mostrar como se espera que el valor "target" avance en el tiempo y así determinar el crecimiento de distintas variables interesantes. ademas mediante el uso de distintas librerías de python podemos realizar gráficos de dichas funciones, mostrando como fueron en el pasados y como se espera que se comporten en el futuro datos relevantes para el usuario dándole un valor agregado a nuestra plataforma.

  

#### Por realizar:

+ IBM brinda una API a la cual hacer request para obtener datos del modelo entrenado, estamos teniendo problemas para realizar estas requests

+ Integrar los datos obtenidos por la API en el backend y mostrarlos en el frontend para ser visualizados por el usuario

+ Realizar una interfaz para que el usuario elija entre:

1. Usar un modelo de machine learning

2. Usar una función de interpolador

3. Completar con datos

4. Que el sistema genere datos

  

y así devolver una predición.


