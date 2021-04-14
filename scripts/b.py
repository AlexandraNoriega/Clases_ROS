#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random
from std_msgs.msg import Bool
from std_msgs.msg import String
##se importa la estructuras de std_msgs
ab="False"

def callback(data):
    global ab #se usarala variable global
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    ab=data.data
    #rospy.loginfo(ab)

def b():
    global ab #se usarala variable global
    pub = rospy.Publisher('chatterB', String, queue_size=10) #crea el topic con evio de String
    rospy.Subscriber('chatterAB', Bool, callback) #suscribe el nodo al topic y especifica la estructura que se usa
    rospy.init_node('B', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
	rospy.loginfo(ab)
	#se toma establece la pertenencia del dato
	if ab == 1:
	    datoB = "100/0/0"
	else:
	    datoB = "0/0/100"

	rospy.loginfo('Alto%/Medio%/Bajo%')	
	rospy.loginfo('%s',datoB)
        pub.publish(datoB)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        b()
    except rospy.ROSInterruptException:
        pass
