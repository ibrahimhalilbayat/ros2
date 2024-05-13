# BATTERY NODE
import rclpy
from rclpy.node import Node
from interfaces_package.srv import SetLed
from time import sleep
from functools import partial

class SetLedClient(Node):
    def __init__(self):
        super().__init__("set_led_client")
        self.get_logger().info("Client has been created...")
        self.call_server()
    
    def call_server(self):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(5.0):
            self.get_logger().warn("Waiting for the server for Tutatis' sake")
        
        while True:
            try:
                request = SetLed.Request()
                sleep(4)
                request.is_battery_empty = True
                future = client.call_async(request=request)
                future.add_done_callback(partial(self.respose_from_server, is_battery_empty=request.is_battery_empty))
                sleep(6)
                request.is_battery_empty = False
                future = client.call_async(request=request)
                future.add_done_callback(partial(self.respose_from_server, is_battery_empty=request.is_battery_empty))
            except KeyboardInterrupt:
                break 
            
            except Exception as e:
                self.get_logger().error(f"An error has been occured in call_server function: {e}")

    def respose_from_server(self, future, is_battery_empty):
        try:
            response = future.result()
            self.get_logger().info(f"RESPONSE FROM SERVER:  {str(response.led_lights)} --  The request: {is_battery_empty}")
        except Exception as e:
            self.get_logger().error(f"An exception occured in response_from_server: {e}")


def main(args=None):
    rclpy.init(args=args)
    the_node = SetLedClient()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()