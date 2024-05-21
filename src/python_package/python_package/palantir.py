import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class Palantir(Node):
    def __init__(self):
        super().__init__("palantir_node")
        self.subscriber_ = self.create_subscription(String, "news_of_middle_earth", self.callback_first_python_topic, 10)

    def callback_first_python_topic(self, the_message):
        self.get_logger().info(the_message.data)

def main(args=None):
    rclpy.init(args=args)
    node = Palantir()
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()