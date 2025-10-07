# Movies Database

## Descripción
Aplicación web en Python con Flask para buscar películas, ver detalles y dejar comentarios. La información de películas se obtiene vía API y los comentarios se almacenan en una base de datos SQLite.

## Instalación
1. Crear un entorno en Python y ejecutar:
```
pip install -r requirements.txt
```

2. Crear la base de datos y la tabla de comentarios según se indica en  `data > create.sql`

3. Obtener una API key:
Acceder a [omdbapi](https://www.omdbapi.com/apikey.aspx) y rellenar el formulario para obtener una API key por e-mail.

4. Configurar la aplicación:
- Crear un archivo `config.py` siguiendo el modelo de `config_template.py`.
- Rellenar tu `API_KEY` y la ruta de la base de datos (`ORIGIN_DATA`).

## Ejecución

Ejecutar el comando 

```
flask run
```

y abrir el servidor local.

Por defecto se abre en el puerto local 5002 por mejor compatibilidad con MacOS, pero puedes modificarlo en el archivo `.env`.


## Uso básico

- Buscar películas desde la página de inicio por título (en inglés )o año.
- Hacer clic en una película para ver su detalle.
- En la página de detalle, dejar un comentario rellenando el formulario.
- Los comentarios se muestran en la misma página, con fecha y autor.