import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import cv2
import numpy as np

import random


class ObjectDetectionNode(Node):
    def __init__(self):
        super().__init__("CameraToUV")
        self.pub = self.create_publisher(String, "CameraToUV", 10)
        self.timer = self.create_timer(3.0, self.timer_callback)

    def __del__(self):
        pass

    def timer_callback(self):
        if(random.random() < 0.3):
            msg = String()

            u = random.randint(200,400)
            v = random.randint(200,400)
            msg.data = str(u) + " " + str(v)

            self.pub.publish(msg)
            self.get_logger().info("u,v publishing: %s " % msg.data)

def main(args = None):
    rclpy.init(args = args)
    objectDetectionNode = ObjectDetectionNode()
    rclpy.spin(objectDetectionNode)
    objectDetectionNode.destroy_node()
    rclpy.shutdown()

if __name__ == "__name__":
    main()

