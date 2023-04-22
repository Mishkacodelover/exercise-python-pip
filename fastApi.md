# Mi servidor web con Fast Api

Tenemos que instalar dos librerias:
1. pip install fastapi
2. pip install "uvicorn[standard]"
 (este sirve para publicar como un servidor web la fastapi. Es un servidor web, lanza en línea el servidor hecho en pip3)

3. Para activar nuestro servidro(para que escuche por un puerto), hay que poner en la consola los siguiente comandos:

  uvicorn main:app --reload

4. Ahora nos sale información del puerto que nos ha asignado, en mi cas
   http://127.0.0.1:8000

5. Así que pongo en el navegador locahost:8000
