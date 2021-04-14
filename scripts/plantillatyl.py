#!/usr/bin/env python
#Es obligatorio escribir en la primera línea esta instrucción, le da formato de python y ejecutable al script

#importamos las librerías necesarias
import rospy
from std_msgs.msg import Bool ##se importa la estructuras de std_msgs

#se inicializan variables que se vayan a usar el programa
ab="False"

#definimos el callback que se encargara de escuchar el dato que se esta enviando en el topic
def callback(name_data):
    global ab #se usara la variable global
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    ab=data.data

#definimos la funcion del programa
def talkerandlistener():
    global ab #se usara la variable global

    #se crean los topics que lanzara el nodo, dandoles nombre, tipo de variable a enviar y el largo de la misma
    pub = rospy.Publisher('chatterB', String, queue_size=10) 

    #definimos que el nodo se suscribe al topic del tipo string y obtiene el dato con la funcion callback
    rospy.Subscriber('chatterAB', Bool, callback) 

    #iniciamos el nodo, le damos nombre y si deseamos que coloque un serial para que no se replique el nombre activamos anonymous
    rospy.init_node('B', anonymous=True)

    #establecemos el periodo de muestreo
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
	#--------------------------------------------------
	#Coloca las instrucciones que se dessen ejecutar (algoritmo)
	#--------------------------------------------------
	rospy.loginfo('Alto%/Medio%/Bajo%') #  rospy.loginfo imprime en terminal 	
	rospy.loginfo('%s',datoB)
        pub.publish(datoB)		    #  publica en el topic la variable
	#duerme el programa hasta que se cumpla el periodo de muestreo
        rate.sleep()

    # spin() mantiene la ejecución del script hasta que el nodo sea cerrado
    rospy.spin()

# main, una vez se llama al programa ejecuta la funcion definida
if __name__ == '__main__':
    try:
        talkerandlistener()
    except rospy.ROSInterruptException:
        pass

#Recuerda, si vas a crear otro nodo copias y pegas la plantilla y luego haces las modificaciones necesarias
#no olvides si tienes anonymous activado y creas nodos bajo el mismo nombre, se eliminara el primero y solo quedara el ultimo que hayas ejecutado.
#Apenas termines las modificaciones modifica el CMakeList del paquete y agrega el archivo dentro del catkin_install_python, de lo contrario no encontrara el ejecutable en el paquete
