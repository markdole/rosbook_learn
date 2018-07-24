#!/usr/bin/env python
import rospy
from mark1.srv import WordCount
import sys

rospy.init_node('service_client')
rospy.wait_for_service('Word_count')

word_counter = rospy.ServiceProxy('Word_count', WordCount)
words = ' '.join(sys.argv[1:])
word_count = word_counter(words)

print words, '->', word_count.count
