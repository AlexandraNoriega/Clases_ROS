#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random #importamos libreria random para la funcion random
from std_msgs.msg import Bool
from std_msgs.msg import Int8
from std_msgs.msg import Float32
##se importa la estructura string de std_msgs
datobool=False
datoint=0

def callback(data):
    global datobool
    rospy.loginfo(rospy.get_caller_id() + 'I heard E %s', data.data)
    datobool=data.data

def callback2(data):
    global datoint
    rospy.loginfo(rospy.get_caller_id() + 'I heard E %s', data.data)
    datoint=data.data

def talker():
    global datobool
    global datoint
    rospy.Subscriber('Arduinob', Bool, callback)
    rospy.Subscriber('Arduinoi', Int8, callback2)
    pubab = rospy.Publisher('chatterAB', Bool, queue_size=10) #crea un topic donde el nodo publique un bool
    pubac = rospy.Publisher('chatterAC', Int8, queue_size=10) #crea un topic donde el nodo publique un int8
    pubad = rospy.Publisher('chatterAD', Float32, queue_size=10) #crea un topic donde el nodo publique un int8
    rospy.init_node('A', anonymous=True) #inicializa el node
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ab = datobool
	ac = datoint
	ad= round(random.uniform(0.00, 10.00), 2)
	rospy.loginfo(ab) #imprime en pantalla el dato
	rospy.loginfo('ac:')       
	rospy.loginfo(ac)
	rospy.loginfo('ad:')       
	rospy.loginfo(ad)
        pubab.publish(ab) #publica en el topic AB la variable
	pubac.publish(ac)
	pubad.publish(ad)
        rate.sleep()

# main
if __name__ == '__main__':
    try:
        talker() #ejecuta la funcion
    except rospy.ROSInterruptException:
        pass
