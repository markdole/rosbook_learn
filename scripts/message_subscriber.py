#!/usr/bin/env python

import rospy
from mark1.msg import Complex

def callback(msg):
	print 'Real', msg.real
	print 'Img', msg.imaginary,'\n'
	
rospy.init_node('message_subscriber')
sub = rospy.Subscriber('Complex' , Complex , callback)
rospy.spin()

