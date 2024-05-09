import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class FirstPythonPublisher(Node):
    def __init__(self):
        super().__init__("first_python_publisher")
        
        self.the_publisher_ = self.create_publisher(String, "first_python_topic", 10)
        # 10 here is the queue size. It will keep up to 10 messages if some messages are late

        self.timer_ = self.create_timer(0.5, self.publish_to_topic)
        self.get_logger().info("Message is publishing under the topic 'first_python_topic'...")

    
    def publish_to_topic(self):
        the_message = String()
        the_message.data = "One ring to rule them all"
        self.the_publisher_.publish(the_message)

def main(args=None):
    rclpy.init(args=args)
    node = FirstPythonPublisher()
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()