#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MiddleEarthNews(Node):
    def __init__(self):
        super().__init__("middle_Earth_news")
        self.declare_parameter("location_name")
        self.declare_parameter("publish_freq", 1.0)
        self.location_ = self.get_parameter("location_name").value
        self.publish_freq_ = self.get_parameter("publish_freq").value
        self.publisher_ = self.create_publisher(String, "news_of_middle_earth", 10)
        self.timer_ = self.create_timer(self.publish_freq_, self.publishing_callback)

    def publishing_callback(self):
        msg = String()
        msg.data = f"News from {self.location_}"
        self.publisher_.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    le_node = MiddleEarthNews()
    rclpy.spin(le_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()