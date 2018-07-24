#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage
import cv2, cv_bridge

class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		#self.CvBridgeError= cv_bridge.CvBridgeError()
		#cv2.namedWindow("window",cv2.WINDOW_AUTOSIZE) unknown Error occured 
		self.image_sub = rospy.Subscriber('/camera/rgb/image_raw/compressed',CompressedImage,self.image_callback)
		
	def image_callback(self,msg):
		image = self.bridge.compressed_imgmsg_to_cv2(msg,desired_encoding="bgr8")
		print image.size, image.shape
		#cv2.namedWindow("window",cv2.WINDOW_NORMAL)
		#cv2.imshow("window",image)
		cv2.namedWindow("window2",cv2.WINDOW_NORMAL)
		cv2.imshow("window2",image[:,:,0])
		cv2.waitKey(3)		

rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()
