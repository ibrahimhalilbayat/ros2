import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NewsFromIsengard(Node):
    def __init__(self):
        super().__init__("news_from_isengard_node")
        self.declare_parameter("publishing_frequency", 1.0)
        self.publish_freq_ = self.get_parameter("publishing_frequency").value
        self.publisher_ = self.create_publisher(String, "news_of_middle_earth", 10)
        self.timer_ = self.create_timer(self.publish_freq_, self.callback_for_publishing)

    def callback_for_publishing(self):
        msg = String()
        msg.data = "ISENGARD: Gandalf the fool..."
        self.publisher_.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    the_node = NewsFromIsengard()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()