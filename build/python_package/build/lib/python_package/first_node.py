#!/usr/bin/env python3 
# We use the line above to specify the interpreter

# To use ROS2 functionalities
import rclpy
from rclpy.node import Node

class LeNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.create_timer(0.5, self.WarningFunction)

    def WarningFunction(self):
        self.get_logger().warning("This is a WARNING from WarningFunction function from the first_node...")


def main(args=None):
    # initialize the communication 
    rclpy.init(args=args)
    #### code ####
    # Let's create a Node and give it a name 'py_test'
    # Name of the node is not the name of the file
    node = LeNode()
    rclpy.spin(node=node)
    #### code ####
    # Now shutdown the communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()