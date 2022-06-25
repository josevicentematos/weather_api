# Weather API

Pequeña API hecha en Django con Rest Django Framework para consultar la API de [OpenWeatherMap](https://openweathermap.org/api).

## Prerequisitos

Es necesario tener el módulo de virtual environment instalado para poder usar con facilidad el proyecto, ya que esté trae su propio virtual environment.
```sh
python -m pip install virtualenv
```

Una vez instalado navegaremos hasta la carpeta del repositorio en una CLI e iniciaremos el ambiente virtual con la siguiente linea:
```sh
env\Scripts\activate
```

Ya con el ambiente virtual activado iniciamos el servidor con:
```sh
python manage.py runserver
```

## Cómo usar

Para consultar la API se debe hacer una petición GET desde el explorador o alguna herramienta como Postman de las siguientes formas:
```sh
127.0.0.1:8000/weather/bogota/co

127.0.0.1:8000/weather?city=bogota&country=co
```
Los parametros *bogota* y *co* pueden ser reemplazados con el nombre y codigo (o nombre) de otra ciudad como por ejemplo: *montevideo* y *uruguay*.

Para ejecutar los test se ejecuta lo siguiente:
```sh
python manage.py test
```
