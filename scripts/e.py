#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
##se importa la estructuras de std_msgs
be='0/0/0'

def callback(data):
    global be
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    be=data.data

def e():
    global be
    pub = rospy.Publisher('chatterE', String, queue_size=10)
    rospy.Subscriber('chatterB', String, callback)
    rospy.init_node('E', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5hz

    while not rospy.is_shutdown():
	v = be.split("/",3) #separa el String teniendo en cuenta el caracter /
	Alto = int(v[0]) 
	Medio = int(v[1]) 
	Bajo = int(v[2]) 
	if Alto == 50 or Bajo == 50:
	    if Alto ==50:
		dato = 'A'
	    else :
		dato = 'M'
	else:
	    Per = {Alto,Medio,Bajo}
	    Maxi = max(Per)
	    if Alto == Maxi:
		dato = 'A'
	    elif Medio == Maxi:
		dato = 'M'
	    else: 
		dato = 'B'
	rospy.loginfo(dato)
        pub.publish(dato)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        e()
    except rospy.ROSInterruptException:
        pass
