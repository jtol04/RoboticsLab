#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Modified by: Amir Hossain and Jary Tolentino
# Fordham Robotics Lab
# This code was modified to be used for the Logitech ATK3 Joystick
# by adding code to the callback function

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

rospy.init_node('joy_teleop')

def joyCallback(data):
    if data.buttons[0] == 1:
        twist = Twist()
        twist.linear.x = 1*data.axes[1]
       	twist.angular.z = 1.5*data.axes[0]
       	pub.publish(twist)
    else:
        twist = Twist()
       	twist.linear.x = 0
       	twist.angular.z = 0
       	pub.publish(twist)
def callback_shutdown():
    print("Shutting down")
    pub = rospy.Publisher(robot + '/RosAria/cmd_vel', Twist, queue_size=1)
    msg = Twist()
    msg.angular.z=0.0
    msg.linear.x=0.0
    pub.publish(msg)
    rospy.sleep(1)
    return





# Intializes everything
def start():
    # publishing to "Px/cmd_vel" to Px
    global pub
    pub = rospy.Publisher(robot + '/RosAria/cmd_vel', Twist, queue_size=100,latch=True)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, joyCallback)
    # starts the node
    rospy.spin()

#-------------------------------MAIN  program----------------------
if __name__ == '__main__':
    try:
        rospy.on_shutdown(callback_shutdown)
        robot = input("Which robot would you like to pair with?: ")
        print("Publishing to '" + robot + "/RosAria/cmd_vel'")
        start()
    except rospy.ROSInterruptException:
        pass

