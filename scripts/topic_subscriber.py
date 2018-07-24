#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    print data.data

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('counter',Int32, callback)
rospy.spin()
