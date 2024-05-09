# This is the second node
# This file has 1 publisher and 1 subscriber
# Name: number_counter
# This will subscribe to a topic named 'number'
# And will publish under a topic named 'number_count'
# The class will also have a server named 'reset_counter'
# If the client requests True, then the counter will be 0

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
from numpy.random import randint

class HW2(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.get_logger().info("number_counter is created... It published and subscribes")
        self.counter_ = 0
        self.the_publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.the_subscriber_ = self.create_subscription(Int64, "number", self.callback_subscription, 10)

        self.create_timer(1.0 , self.publish_number)


        self.server_ = self.create_service(SetBool, "reset_counter", self.callback_counter_reset)
    
    def callback_counter_reset(self, request, response):
        if request.data:
            self.counter_ = 0
            self.get_logger().info("Counter has been reset.")
            response.success = True
            response.message = "The success has been set to True bro... The counter has been reset"
        else:
            response.success = False
            response.message = "TNO RESET"

        return response

    def publish_number(self):
        the_message = Int64()
        the_message.data = self.counter_
        self.get_logger().info(f"Publish the number {self.counter_} from HW2")
        self.the_publisher_.publish(the_message)
          
    def callback_subscription(self, received_message):
        self.get_logger().info(f"Received number is: {received_message.data}")
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    theNode = HW2()
    rclpy.spin(theNode)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
