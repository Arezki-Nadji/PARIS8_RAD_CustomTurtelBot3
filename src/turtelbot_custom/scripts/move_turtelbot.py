#! /usr/bin/env python3

import rospy 
from geometry_msgs.msg import Twist

def move_circle():

	rospy.init_node('topic_publisher')
	pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
	rate = rospy.Rate(1)
	now = rospy.Time.now()
	move = Twist()
	move.linear.x= 0.2
	move.angular.z = 0.2
	while not rospy.is_shutdown():
		pub.publish(move)
		rate.sleep

if __name__=='__main__':
	try:
		move_circle()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass