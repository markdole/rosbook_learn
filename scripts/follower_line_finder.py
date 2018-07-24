#!/usr/bin/env python
import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import CompressedImage

class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		self.image_sub = rospy.Subscriber('/camera/rgb/image_raw/compressed',CompressedImage,self.image_callback)
	
	def image_callback(self,msg):
		image = self.bridge.compressed_imgmsg_to_cv2(msg,desired_encoding='bgr8')
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		lower_yellow = numpy.array([20,50,150])
		upper_yellow = numpy.array([50,255,190])
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#		masked = cv2.bitwise_and(image,image,mask=mask)
#		print image.size, image.shape
		h,w,d= image.shape
		top = 3*h/4
		bot = top + 20
		mask[0:top,:] = 0
		mask[bot:h,:] = 0
		#cut the image to a blade
		M = cv2.moments(mask)
		print M
		#class MOMENTS
		if M['m00']>0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.circle(image,(cx,cy),20,(0,0,255),-1)
		cv2.namedWindow("window2",cv2.WINDOW_NORMAL)
		cv2.imshow("window2",image)
		cv2.namedWindow("window",cv2.WINDOW_NORMAL)
		cv2.imshow("window",mask)
		cv2.waitKey(3)
		
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()
