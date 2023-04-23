# Docker para aislar entornos

Si queremos mantener los proyectos aislados en la nube, cuando los subamos
a un servidor real, no nos sirven los entornos virtuales de local.

Para tener varias versiones, docker aisla con contenedores las versiones y los entornos web.
Se puede desplegar para amazon, etc..

## Instalar docker con WSL

1. Página oficial[https://docs.docker.com/desktop/install/windows-install/]
2. Instalamos el instalador
3. Instalamos según instrucciones en windows y en ubuntu
4. Ahora podemos dockenizar nuestros archivos:

En una carpeta de archivos de scripts como nuetra app, creamos un archivo docker

Y en el ponemos:
(Le ponemos qué versión de python queremos que tenga nuestro contenedor)

FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt
//(esto lo ponemos dos veces, porque el izq es nuestro archivo local y el derecho el de docker)

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

COPY . /app/
//(el punto es para decirle que copie todo lo que hay dentro de la carpeta app)
CMD bash -c "while true; do sleep 1; done"
// (este comando es en bash, y es para que esté encendido siempre el contenedor)

## Para ejecutar el contenedor

Hay que crear otro archivo más llamado docker-compose.yml
A este le decimos literalmente que El servicio se llama app csv, le decimos que haga un build y le indicamos que el contexto del build es el archivo dockerfile.
En otras palabras: Vas a construir este servicio, desde el contexto de la carpeta donde etoy ubicada y esta carpeta busca el archivo dockerfile para construir el contenedor.

services:
app-csv:
build:
context: .
dockerfile: Dockerfile

### Ejecutamos en la terminal para encenderlo

1. Primero abrimos la aplicación de docker en el escritorio
2. Comando:

docker compose build

!!!OJO¡¡¡ en powershell los comandos docker funcionan tal cual, pero en la consola de ubuntu, tenemos que ejecutar siempre con .exe
Y si lo hacemos con ubuntu hay tener instalada la version 2 de wsl para ubuntu.

Es decir docker.exe compose build

3.  docker compose up -d
4.  Para ver el estado del contenedor ponemos
    docker compose ps
5.  Para conectarnos dentro de ese servidor virtual
    docker compose exec nombreDeCarpetaCreada bash

    Para listar los archivos de dentro ejecutamos ls -l

6.  Así podemos ejecutar nuestros scripts dentro del ambiente de docker.
7.  Para salir ejecutamos comando exit

### Enlazar sistema de archivos para automatizarlos con docker

Esto sirve para que cada vex que hagamos un cambio en un archico por ejemplo en v code , se nos actualice también en el entorno de docker.
Esto se consigue añadiendo esta pequeña línea de código a nuestro archivo
docker-compose.yml

volumes: - .:/app

Así no tenemos que entrar y salir del contenedor cada vez, solo le damos otra vez al comando 'cat nombreDelArchivoActualizado' y ya está.
