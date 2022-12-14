#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    
    def __init__(self):
        super().__init__("number_publisher")    
        self.number_=5    
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(0.5, self.publish_number)
        self.get_logger().info("Number Publisher Node has been started")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    
    node = NumberPublisherNode() #Node("py_test")
    
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ =="__main__":
    main()