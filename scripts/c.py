#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random
from std_msgs.msg import Int8
from std_msgs.msg import String
from decimal import *
##se importa la estructuras de std_msgs
ac=0
maxin=40
mn=(Decimal(-4)/Decimal(maxin)) #decimal para que la division arroje decimales
mp=Decimal(4)/Decimal(maxin)

def callback(data):
    global ac
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    ac=data.data

def c():
    global ac
    pub = rospy.Publisher('chatterC', String, queue_size=10)
    rospy.Subscriber('chatterAC', Int8, callback)
    rospy.init_node('C', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
	if ac <= (maxin/4):
	    dato = "0/0/100"
	elif ac >= (3*maxin/4):
	    dato = "100/0/0"
	elif ac == (maxin/2):
	    dato = "0/100/0"
	elif ac < (maxin/2) and ac > (maxin/4):
	    Bajo = (2+(mn*ac))
	    Medio = (mp*ac)-1
	    dato = '0/'+str(int(Medio*100))+'/'+str(int(Bajo*100)) #str para concatenar y int para obtener el porcentaje entero
	elif ac < (3*maxin/4) and ac > (maxin/2):
	    Medio = ((mn*ac)+3)
	    Alto = ((mp*ac)-2)
	    dato = str(int(Alto*100))+'/'+str(int(Medio*100))+'/0'

	rospy.loginfo('I send %s',dato)
        pub.publish(dato)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        c()
    except rospy.ROSInterruptException:
        pass
