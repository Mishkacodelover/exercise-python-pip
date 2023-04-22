# Como guardar instrucciones de módulos instalados en entornos virtuales

Cuando trabajamos en entornos virtuales , tenemos instalados una serie de módulos.
Si queremos que otro compañero pueda trabajar en el proyecto, para pasarle todos los módulos , podemos
guardalos en un archivo de texto , al estilo del package de node.js.

Las instrucciones son:

1. Entramos en el entorno virtual
2. pip3 freeze > nombre.txt  (esto es para crear el archivo y guardar los módulos dentro)
3. car nombre.tex (esto es para abrir el archivo creado y ver las dependencias instaladas)
4. Para instalar las dependencias todas de golpe: 
    pip3 install -r nombre.txt
