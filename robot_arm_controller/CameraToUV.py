import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import os

#~/robot_ws/src/robot_arm_controller/robot_arm_controller/uv.txt

def uv():
    u,v = 0,0
    #if os.path.isdir("~/robot_ws/src/robot_arm_controller/robot_arm_controller/uv.txt"):
    if(1):
        with open("/home/meccabunny/.ros/uv.txt", "r") as f:
            u = f.readline()
            v = f.readline()
    return u, v

class CameraToUV_Node(Node):
    def __init__(self):
        super().__init__("CameraToUV")
        self.pub = self.create_publisher(String, "CameraToUV", 10)
        self.timer = self.create_timer(8.0, self.timer_callback)
        self.u_prev = 0
        self.v_prev = 0

    def __del__(self):
        pass

    def timer_callback(self):
        msg = String()

        u,v = uv()

        if( not(u == self.u_prev and v == self.v_prev) ):
            if( not(u == 0 and v == 0)):
                msg.data = str(u) + " " + str(v)
                self.pub.publish(msg)
                self.get_logger().info("u,v publishing: %s " % msg.data)
            else:
                self.get_logger().info("u,v is zero")
        else:
            self.get_logger().info("not publishing")

        self.u_prev = u
        self.v_prev = v

        #msg.data = os.getcwd()
        #self.get_logger().info("u,v publishing: %s " % msg.data)

def main(args = None):
    rclpy.init(args = args)
    cameraToUV_Node = CameraToUV_Node()

    rclpy.spin(cameraToUV_Node)

    cameraToUV_Node.destroy_node()
    rclpy.shutdown()

if __name__ == "__name__":
    main()

