# LED NODE
import rclpy
from rclpy.node import Node 
from interfaces_package.srv import SetLed
from interfaces_package.msg import LedState

class SetLedServer(Node):
    def __init__(self):
        super().__init__("set_led_server")
        self.server_ = self.create_service(SetLed, "set_led", self.set_the_leds)
        self.publisher_ = self.create_publisher(LedState, "led_states", 10)
        self.get_logger().info("SERVER has been created..")

    def set_the_leds(self, request, response):
        if request.is_battery_empty:
            # The battery is empty so the light must be powered
            self.get_logger().warn("Empty battery request has been received")
            response.led_lights = [0,0,1]
        
        else:
            # The battery is not empty
            self.get_logger().info("FULL BATTERY")
            response.led_lights = [0,0,0]
        self.publish_message_to_topic(response.led_lights)
        return response
    
    def publish_message_to_topic(self, led_lights):
        msg = LedState()
        msg.led_state = led_lights
        self.publisher_.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    the_node = SetLedServer()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
