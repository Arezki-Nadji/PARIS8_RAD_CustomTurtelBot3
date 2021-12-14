


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

disToObstacle =3

def callback(msg):
	#print to the terminal
	rospy.loginfo(rospy.get_caller_id() +"The distance to obstacle is - %s", msg.ranges[300])
#if the distance to an obstacle in front ot the robot is bigger then 1 meter, the robot will move forward
	if msg.ranges[300]> disToObstacle:
		print("in")
		move.linear.x=0.2
		move.angular.z = 0.0

#if the distance to an obstacle in front of the robot is smaller than 1 metter , the robot will turn left
	if msg.ranges[300] <= disToObstacle:
		print("out")
		move.linear.x =0.
		move.angular.z = 0.3
	pub.publish(move)

rospy.init_node('sub_node')
#we subscribe the laser to the topic
sub =rospy.Subscriber('/scan',LaserScan,callback)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=2)
rate=rospy.Rate(10)
move=Twist()

rospy.spin()
