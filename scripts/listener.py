#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

datob=''
datoc=''
datod=''

def callback(data):
    global datob
    rospy.loginfo(rospy.get_caller_id() + 'I heard E %s', data.data)
    datob=data.data

def callback2(data):
    global datoc
    rospy.loginfo(rospy.get_caller_id() + 'I heard F %s', data.data)
    datoc=data.data

def callback3(data):
    global datod
    rospy.loginfo(rospy.get_caller_id() + 'I heard G %s', data.data)
    datod=data.data

def listener():
    global datob
    global datoc
    global datod
    rospy.init_node('H', anonymous=True)

    rospy.Subscriber('chatterE', String, callback)#definimos que el nodo se suscribe al topic del tipo string

    rospy.Subscriber('chatterF', String, callback2)#definimos que el nodo se suscribe al topic del tipo string

    rospy.Subscriber('chatterG', String, callback3)#definimos que el nodo se suscribe al topic del tipo string
    
    pub=rospy.Publisher('chatterH', Int8, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
	#arbol de decisiones
	if datob=='A':
	    bool1=1*18
	else:
	    bool1=0*18

	if datoc=='A':
	    int1=1*18
	elif datoc=='M':
	    int1=0.6*18
	else:	
	    int1=0.2*18

	if datod=='A':
	    float1=1*18
	elif datod=='M':
	    float1=0.5*18
	else:	
	    float1=0*18
	
	R=0.5*(bool1)+0.4*(int1)+0.1*(float1)  
	Arduino=int(R)   
	rospy.loginfo(Arduino)
	pub.publish(Arduino)
        rate.sleep()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

#main
if __name__ == '__main__':
    try:
        listener() #ejecuta la funcion
    except rospy.ROSInterruptException:
        pass
