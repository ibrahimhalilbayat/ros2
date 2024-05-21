import rclpy
from rclpy.node import Node
from numpy.random import randint 
from interfaces_package.msg import Health

class PsychologicalHealthPublisherNode(Node):
    def __init__(self):
        super().__init__("psychological_health_node")
        self.publisher_ = self.create_publisher(Health, "psychological_health", 10)
        self.timer_ = self.create_timer(1.0, self.callback_for_psy_health)
        self.get_logger().info("PsychologicalHealth Node has been created...")
    
    def callback_for_psy_health(self):
        msg = Health()
        msg.level = randint(100)
        msg.is_weather_sunny = True 
        if msg.level > 50:
            msg.the_message = "Mood is good"
        else:
            msg.the_message = "Leave me alone..."

        self.publisher_.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    the_node = PsychologicalHealthPublisherNode()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()