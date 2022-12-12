import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

Buffer = []

class ActionBufferNode(Node):
    def __init__(self):
        super().__init__("ActionBuffer")
        self.create_timer(5.0, self.timer_callback)
        self.pub = self.create_publisher(String, "ActionBuffer", 10)
        self.subscription = self.create_subscription(
            String,
            'InverseKinematics',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        Buffer.append(msg.data)
        #self.get_logger().info("Buffer: " + str(Buffer))

    def timer_callback(self):
        if(len(Buffer) != 0):
            msg = String()
            msg.data = Buffer.pop(0)
            self.pub.publish(msg)
            self.get_logger().info("send: " + msg.data)
            send = bytes(msg.data, "utf8")
            ser.write(send)

def main(args = None):
    rclpy.init(args = args)
    actionBuffer = ActionBufferNode()
    rclpy.spin(actionBuffer)
    actionBuffer.destroy_node()
    rclpy.shutdown()

if __name__ == "__name__":
    main()

