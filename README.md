# project_ros_nodes

Proyecto Nodos ROS
=============

El nodo A (Talker.py) se encargará de escuchar los datos que envíe el Arduino que toma datos del circuito implementado con Fotoresistencia para el valor entero, button para el booleano y como salida un led al que se le envía PWM.

Los nodos B, C y D reciben estos datos enviados y a partir de los valores se buca mediante lógica fuzzy dar la pertenecia a los conjuntos ALTO/MEDIO/BAJO.

[img1]: //home/amy/Imágenes/pertenencia.png "Pertenencia"

Los nodos E, F y G recibiran estas pertenencias y seleccionará el porcentaje más alto de pertenencia como el conjunto al que pertenencen las variables enviadas por el nodo A, se envía un string de un caracter con la inicial del conjunto ( A, M O B). 

Finalmente en el nodo H, le llega esta clasificación de las variables y se realiza un árbol de decisión basado en porcentajes para decidir el valor PWM para el led en el circuito, este árbol le da un porcentaje de 50% al bool, 40% al int y 10% al float.Internamente el bool de A a B maneja pocentajes: para bool [0 1], int [1 0.6 0.2] y float [1 0.5 0]. En el nodo del arduino recibirá este valor que va de 1-18 y lo multiplocará por (255/18) con el fin de que quede escalado hasta 255.

Para ejecutar los nodos creados

``` 
$ roscore
$ rosrun project_ros_nodes _.py
```

**Arduino como Nodo ROS**

<https://youtu.be/MOBSb6cA7kY> Hasta el 6:11 donde el dentro del IDE del arduino encuentra el ejemplo de Hello World de la librería ros_lib

<https://youtu.be/lkyUqMVJBQ0> Este tutorial se encargará de subir el programa al arduino y correrlo como nodo de ROS

**Nota**

Cada que se corre el nodo de Arduino es necesario darle los permisos al puerto 

``` 
sudo chmod 777 /dev/ttyUSB
```
Para correr el archivo de Arduino como nodo ros ejecutamos la siguiente línea

``` 
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

TEMPLATE PARA GENERAR EL README.md GIT
==============

*This will be Italic*

**This will be Bold**

- This will be a list item
- This will be a list item

1. This will be a numerated list 
2. This will be a numerated list 

``` 
this will be a code segment
```

> this will be a definition

<http://url> this will be a web link

<!--this will a comment-->

This will a title
--------------
