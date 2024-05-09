# This is the first node
# This file has 1 publisher
# Name: number_publisher
# This will publish under a topic named 'number'

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from numpy.random import randint

class HW1(Node):
    def __init__(self):
        super().__init__("number_publisher")

        self.the_publisher_ = self.create_publisher(Int64, "number", 10)
        

        self.get_logger().info("number_publisher is created and published under number")

        self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        random_number = randint(100)
        the_message = Int64()
        the_message.data = random_number
        self.get_logger().info(f"The random number is: {random_number}")
        self.the_publisher_.publish(the_message)



def main(args=None):
    rclpy.init(args=args)
    the_node = HW1()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()