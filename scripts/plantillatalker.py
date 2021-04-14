#!/usr/bin/env python
#Es obligatorio escribir en la primera línea esta instrucción, le da formato de python y ejecutable al script

#importamos las librerías necesarias
import rospy
from std_msgs.msg import Bool #se importa la estructura string de std_msgs

#definimos la funcion del programa
def talker():
    #se crean los topics que lanzara el nodo, dandoles nombre, tipo de variable a enviar y el largo de la misma
    pubab = rospy.Publisher('chatterAB', Bool, queue_size=10) 

    #iniciamos el nodo, le damos nombre y si deseamos que coloque un serial para que no se replique el nombre activamos anonymous
    rospy.init_node('A', anonymous=True)

    #establecemos el periodo de muestreo
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        #--------------------------------------------------
	#Coloca las instrucciones que se dessen ejecutar (algoritmo)
	#--------------------------------------------------	
	rospy.loginfo('ac:')     #  rospy.loginfo imprime en terminal 
	rospy.loginfo(ac)
        pubab.publish(ab) 	 #  publica en el topic AB la variable
	#duerme el programa hasta que se cumpla el periodo de muestreo
        rate.sleep()

# main, una vez se llama al programa ejecuta la funcion definida
if __name__ == '__main__':
    try:
        talker() 
    except rospy.ROSInterruptException:
        pass


#Recuerda, si vas a crear otro nodo copias y pegas la plantilla y luego haces las modificaciones necesarias
#no olvides si tienes anonymous activado y creas nodos bajo el mismo nombre, se eliminara el primero y solo quedara el ultimo que hayas ejecutado.
#Apenas termines las modificaciones modifica el CMakeList del paquete y agrega el archivo dentro del catkin_install_python, de lo contrario no encontrara el ejecutable en el paquete
