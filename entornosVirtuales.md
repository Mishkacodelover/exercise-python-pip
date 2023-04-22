# Entornos virtuales en python

Las librerías que se instalan en python pueden generar conflictos por las 
versiones, ya que a veces ciertos programas necesitan una versión distinta de un mismo módulo.
Para evitar esto, se crean entornos virtuales.

Podemos comprobar qué entorno virtual tenemos instalado de forma global con los comandos:

which python3
which pip3
 
Si nos sale usr/bin/python3 y usr/bin/pip3 nos indica que están de forma global las versiones 3.

Si no tenemos mac, no hace falta hacer nada. Si no es el caso, tenemos que
instalar entorno virtual:

sudo apt install -y python3-

le ponemos nombre:
python3 -m venv env

Si listamos la carpeta vemos que se ha creado una carpeta llamada  /env
El siguiente paso es activar esa carpeta:

source env/bin/activate

Así entramos dentro de ese ambiente.
Para salirnos se desactiva:

deactivate

Si miramos dentro veremos que dentro del ambiente no hay instalado nada, ningún módulo.
Por eso por ejemplo tenemos que instalar matplotlib si la queremos usar.


