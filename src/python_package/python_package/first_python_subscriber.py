import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class FirstPythonSubscriber(Node):
    def __init__(self):
        super().__init__("first_python_subscriber")
        self.subscriber_ = self.create_subscription(String, "first_python_topic", self.callback_first_python_topic, 10)

    def callback_first_python_topic(self, the_message):
        self.get_logger().info(the_message.data)

def main(args=None):
    rclpy.init(args=args)
    node = FirstPythonSubscriber()
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()