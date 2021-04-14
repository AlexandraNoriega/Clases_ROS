#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random
from std_msgs.msg import Float32
from std_msgs.msg import String
from decimal import *
##se importa la estructuras de std_msgs
ad=0
maxin=10
mn=(Decimal(-4)/Decimal(maxin)) #decimal para que la division arroje decimales
mp=Decimal(4)/Decimal(maxin)

def callback(data):
    global ad
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    ad=data.data

def d():
    global ad
    pub = rospy.Publisher('chatterD', String, queue_size=10)
    rospy.Subscriber('chatterAD', Float32, callback)
    rospy.init_node('D', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
	if ad <= (maxin/4):
	    dato = "0/0/100"
	elif ad >= (3*maxin/4):
	    dato = "100/0/0"
	elif ad == (maxin/2):
	    dato = "0/100/0"
	elif ad < (maxin/2) and ad > (maxin/4):
	    Bajo = (2+(float(mn)*ad))
	    Medio = (float(mp)*ad)-1
	    dato = '0/'+str(int(Medio*100))+'/'+str(int(Bajo*100)) #str para concatenar y int para obtener el porcentaje entero
	elif ad < (3*maxin/4) and ad > (maxin/2):
	    Medio = ((float(mn)*ad)+3)
	    Alto = ((float(mp)*ad)-2)
	    dato = str(int(Alto*100))+'/'+str(int(Medio*100))+'/0'

	rospy.loginfo('I send %s',dato)
        pub.publish(dato)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        d()
    except rospy.ROSInterruptException:
        pass
