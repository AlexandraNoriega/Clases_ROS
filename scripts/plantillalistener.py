#!/usr/bin/env python
#Es obligatorio escribir en la primera línea esta instrucción, le da formato de python y ejecutable al script

#importamos las librerías necesarias
import rospy
from std_msgs.msg import String # importa la librería y especificamente la estructura

#definimos el callback que se encargara de escuchar el dato que se esta enviando en el topic
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard E %s', data.data)

#definimos la funcion del programa
def listener():

    #iniciamos el nodo, le damos nombre y si deseamos que coloque un serial para que no se replique el nombre activamos anonymous
    rospy.init_node('H', anonymous=True)

    #definimos que el nodo se suscribe al topic del tipo string y obtiene el dato con la funcion callback
    rospy.Subscriber('chatterE', String, callback)

    # spin() mantiene la ejecución del script hasta que el nodo sea cerrado
    rospy.spin()

#main, una vez se llama al programa ejecuta la funcion definida
if __name__ == '__main__':
    listener()


#Recuerda, si vas a crear otro nodo copias y pegas la plantilla y luego haces las modificaciones necesarias
#no olvides si tienes anonymous activado y creas nodos bajo el mismo nombre, se eliminara el primero y solo quedara el ultimo que hayas ejecutado.
#Apenas termines las modificaciones edita el CMakeList del paquete y agrega el archivo dentro del catkin_install_python, de lo contrario no encontrara el ejecutable en el paquete
