import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
from numpy.random import randint

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_the_server(a=randint(100), b=randint(100))


    def call_the_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(5.0):
            self.get_logger().warn("It has been 5 seconds for God's sake...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request=request)
########################################################################################################
######   Actually it is enough until that part. However, we also want to see the reponse from the server
        future.add_done_callback(partial(self.callback_add_two_ints, a=a, b=b))

    def callback_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(f"Reponse from the server: {str(a)} + {str(b)} = {str(response.sum)}") 

        except Exception as e:
            self.get_logger().info(f"An exception occured in callback_add_two_ints function: {e}")
########################################################################################################
########################################################################################################
def main(args=None):
    rclpy.init(args=args)
    the_node = AddTwoIntsClientNode()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()