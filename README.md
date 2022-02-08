# Postal_app
Aplicación de consumo de API de códigos postales

![Diagrama arq](https://user-images.githubusercontent.com/90158740/153053250-7efce91d-88ea-4235-a918-58ab0934965d.png)

La aplicación conecta 2 microservicios:
El primero es una aplicación web desarrollada en Django en la cual se almacenan los datos extraidos del archivo csv que se encuentra en la carpeta.
Tiene un modelo, en el cual contiene los campos de la tabla del archivo csv.
Tiene 2 vistas, la primera es `/import` en la cual se cargan los datos del archivo csv a la tabla del modelo, retornando un mensaje de éxito al finalizar.
la otra es `/postal/id/` en donde se ingresa un número entre el 1 al 999 y retorna la latitud y la longitud ligadas a ese id.

La aplicación se puede subir tanto a un contenedor de docker como a una aplicación de heroku, como es el caso.
link: 

Pasos para usarla localmente:
1. Abir una terminal en la carpeta donde se tiene almacenado (Tener python previamente instalado)
2. ejecutar `python3 -m venv env` si es en linux/mac o `python -m venv env`  si es en windows
3. ingresar `source env/bin/activate` si es en linux/mac o `env/Scripts/activate`
4. ejecutar el comando `python3/py pip install django` y `python3/py pip install djangorestframework`  (python3 o py dependiendo del sistema operativo)
5. ejecutar en este orden los siguientes comandos: `python3/py manage.py makemigrations` , `python3/py manage.py migrate` y `python3/py manage.py runserver`
6. abrir la dirección que retorna la terminal y añadir a la url el endpoint `/import` para ingresar a la base de datos los datos del archivo csv


La segunda aplicación trae los datos del anterior microservicio para ingresarlos en la petición que se realiza a la api de los códigos postales, la aplicación está desarrollada en el framework flask y también se puede ubpir a un contenedor de docker así como a una app de heroku, link:
Pasos para el uso local: 
1. Abir una terminal en la carpeta donde se tiene almacenado (Tener python previamente instalado)
2. ejecutar `python3 -m venv env` si es en linux/mac o `python -m venv env` si es en windows
3. ingresar `source env/bin/activate` si es en linux/mac o `env/Scripts/activate`
4. ejecutar el comando `python3/py pip install -r requirements.txt` (python3 o py dependiendo del sistema operativo)
5. ejecutar el comando `python3/py main.py`
6.  abrir la dirección que retorna la terminal y añadir a la url el endpoint `/postal-code/id` en donde id es el id de un objeto de la aplicación anterior.

