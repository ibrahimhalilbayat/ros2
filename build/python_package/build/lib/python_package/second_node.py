#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_second")
        self.create_timer(1, self.ErrorFunction)

    def ErrorFunction(self):
        self.get_logger().error("This is an ERROR log from  ErrorFunction from the Second Node...")

    
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

