#!/usr/bin/env python3
import rclpy

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import math

import time

import os

class InverseKinematicsNode(Node):
    def __init__(self):
        super().__init__("InverseKinematics")
        self.pub = self.create_publisher(String, "InverseKinematics", 10)
        #self.timer = self.create_timer(1.0, self.timer_callback)
        self.subscription = self.create_subscription(
            String,
            'CameraToUV',
            self.listener_callback,
            10)
        self.subscription

        self.l1 = 9
        self.l2 = 12

    def listener_callback(self, msg):
        uv = msg.data.split(" ")

        u = int(uv[0])
        v = int(uv[1])

        #with open("~/robot_ws/src/robot_arm_controller/robot_arm_controller/uv.txt", "r") as f:
        #    u = f.readline()
        #    v = f.readline()

        self.get_logger().info("u, v : {} {}".format(u, v))

        h = 0.01
        u *= h
        v *= h

        #x = u
        #y = v
        #z = 0

        x = 0
        y = 15
        z = 2

        x1 = x + 5
        y1 = y
        z1 = z

        x2 = x - 5
        y2 = y
        z2 = z

        self.get_logger().info("===============================================")
        self.get_logger().info("X,Y,Z: {} {} {}".format(x1, y1, z1))

        if( (pow(x1,2) + pow(y1,2) + pow(z1,2)) < (pow( self.l1 + self.l2, 2 )) and
        (pow(x2,2) + pow(y2,2) + pow(z2,2) < pow(self.l1 + self.l2 , 2))):

            e11,e12,e13 = XYZtoE123(self.l1, self.l2, x1, y1, z1)
            e1 = str(e11) + " "  + str(e12) + " " + str(e13)+ " "
            msg.data = e1
            self.pub.publish(msg)
            time.sleep(0.1)
            self.get_logger().info("e1, e2, e3 publishing#1: %s " % msg.data)

            self.get_logger().info("X,Y,Z: {} {} {}".format(x2, y2, z2))

            e21,e22,e23 = XYZtoE123(self.l1, self.l2, x2, y2, z2)
            e2 = str(e21) + " "  + str(e22) + " " + str(e23)+ " "
            msg.data = e2
            self.pub.publish(msg)
            time.sleep(0.1)
            self.get_logger().info("e1, e2, e3 publishing#1: %s " % msg.data)

            e31, e32, e33 = 2, 2, 2
            e3 = str(e31) + " "  + str(e32) + " " + str(e33)+ " "
            msg.data = e3
            self.pub.publish(msg)
            time.sleep(0.1)
            self.get_logger().info("e1, e2, e3 publishing#1: %s " % msg.data)
        else:
            msg.data = "Action is out of robot's span."
            self.get_logger().info(" %s " % msg.data)

def XYZtoE123(l1,l2,x,y,z):
    e1 = math.atan2(y,x)
    e1 = e1 / math.pi * 180

    d = math.sqrt(pow(x,2)+pow(y,2)+pow(z,2))

    e3 = math.atan(  math.sqrt( (pow(2*l1*l2,2)-(pow((pow(l1,2)+pow(l2,2)-pow(d,2)),2)))  /  (pow((pow(l1,2)+pow(l2,2)-pow(d,2)),2))  )  )
    e3 = 180 - e3 / math.pi * 180

    k = math.atan(  math.sqrt(  (  pow(2 * l1 * d , 2) - pow( pow(l1,2) + pow (d, 2) - pow(l2, 2) , 2 ) ) / pow( pow(l1,2) + pow(d,2) - pow(l2, 2) , 2  )  )  )
    j = math.atan2(z, math.sqrt( pow(x,2) + pow(y,2) ) )
    k = k / math.pi * 180
    j = j / math.pi * 180
    e2  = 90 - k - j

    return e1,e2,e3

def main(args = None):
    rclpy.init(args=args)
    node = InverseKinematicsNode()
    rclpy.spin(node)
    rclpy.shutdown()


#        h = 0.01
#        u *= h
#        v *= h
#
#    #[X]      [   a1, a2, a3, xe  ]   [x]
#    #[Y]  =   [   b1, b2. b3, ye  ] * [y]
#    #[0]      [   c1, c2, c3, ze  ]   [Q]
#    #[1]      [   0,  0,  0,  1   ]   [1]
#
#        a1 = 1
#        b1 = 0
#        c1 = 0
#
#        a2 = 0
#        b2 = 1
#        c2 = 0
#
#        a3 = 0
#        b3 = 0
#        c3 = -1
#
#        xe = 0
#        ye = 12
#        ze = 0
#
#        Q = -(c1*u +c2*v + ze)/c3
#        X = a1*u + a2*v + a3+Q + xe
#        Y = b1*u + b2*v + b3*Q + ye
#
#        x = X
#        y = Y
#        z = 0
#
#        #action1
#        x1 = x
#        y1 = y - 3
#        z1 = 1
#        #action2
#        x2 = x
#        y2 = y + 3
#        z2 = 1
#        #action3
#        e31 = 0
#        e32 = 0
#        e33 = 0
#

