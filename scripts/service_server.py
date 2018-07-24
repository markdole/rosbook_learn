#!/usr/bin/env python
import rospy
from mark1.srv import WordCount, WordCountResponse

s= set('',)

def count_words(request):
    s.update(set( request.words.split() ))
    print s
    return WordCountResponse( len( request.words.split()))

rospy.init_node('mark_service_server')

service = rospy.Service('Word_count', WordCount, count_words)

rospy.spin()

