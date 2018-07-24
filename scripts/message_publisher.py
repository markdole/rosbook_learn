#!/usr/bin/env python
import rospy
from mark1.msg import Complex
from random import random

rospy.init_node('message_pub')
pub = rospy.Publisher('Complex',Complex,queue_size=20)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	msg= Complex()
	msg.real = random()
	msg.imaginary = random()
	
	pub.publish(msg)
	rate.sleep

