# Master_Prueba_Final_B.
Prueba_FInal_B_Tratamiento de Datos

### Detalle del proyecto
EL proyecto pretende hacer web scraping de una página web de venta de funko pops en el que se buscan
los funkos de la línea Marvel, reolectamos información sobre su nombre y su precio y lo almacenamos en MongoDB.
Posteriormente se realiza una pequeña página con programación en html en el que con uso de Python y flask se despliega
la información almacenada en MongoDB.

El proyecto repositorio contiene tres archivos .py, un .html y un txt en los cuales realizan las siguientes acciones:

__- Main.py:__ Contiene el código para la extracción de los datos (Nombre y precio) de una página de venta de figuras de acción.

__- db.py:__ Contiene el código para la comunicación entre Python y MongoDB, adicionalmente guarda la información extraida por el
            código Main.py en la base de datos MongoDB.
            
__- app.py:__ Contiene el código que extrae los datos de MongoDB y los muestra en un servidor web.

__- templates/web.html:__ En la carpeta templates se encuentra el archivo web.html que es la programación de la página donde se
                          mostrarán los datos almacenados en MongoDB.
                          
__- requirements.txt:__ El archivo contiene las libreriás necesarias para que el código funcione.

__- .env:__ Contiene el usuario y contraseña para el acceso a la base de datos.



### Información de ayuda.
Para la elaboración del proyecto se consultó varios tutoriales y paginas con información sobre la extracción de datos,
el almacenamiento en MongoDB y la extracción de los mismo por medio de un web server usando Python y Flask.

- https://www.youtube.com/watch?v=t9YQbFSsmns
- https://www.youtube.com/watch?v=oyU4SpeGztw
- https://flask-pymongo.readthedocs.io/en/latest/

