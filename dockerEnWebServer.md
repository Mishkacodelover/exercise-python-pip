# Usar docker con web server

Si queremos utilizar contenedores para nuestro servidor, que es lo más comúm, hay leves cambios en comparación con hacerlo para ejecutar scripts.

Tenemos que añadir a nuetro archivo docker-compose:
ports: - '80:80'

Y añadir a nuetro archivo dockerfile:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

- Para comprobar que funciona podemos ir al navegador y poner directamente
  http://localhost/contact

No hace falta poner 8000, porque el contenedor está en el 80 y sale automáticamente.
