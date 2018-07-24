# rosbook_learn
ROS Packages for TurtleBot3 Simulations with the ROS book: " Programming Robots with ROS: A Practical Introduction to the Robot Operating System "
# The Code version 1.0
Including the  Chapter1-10,12 of the book .(Python)
- Computer Environment:
- Ubuntu 16.04: Xenail
- ROS :  Kinetic
# Usage :
git clone to the ROS workspace and change the package name to mark1 && catkin_make 
# Code change infomation:
- Chapter7 Wanderbot :exp 7-1 change the if sentence
- Chapter12 Follower : exp 12-2 change the usage of cv2.namedWINDOW()
- Chapter12 Follower : course.launch . The old version of turtlebot package didn't include the course.launch file ,I creat the launch file and change the map
- Chapter12 Follwer : 12-3 change the cv2.inRange of color filter.
- Chapter12 Follwer : 12-4 follow the change of 12-3 and delete an useless sentence , change the mask range.
- Chapter12 Follwer : 12-3 change the publish topic to fit the gazebo subscriber topic (/cmd_vel) and adjust the coefficient of  <self.twist.angular.z>
