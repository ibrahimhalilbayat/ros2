import rclpy
from rclpy.node import Node 
from example_interfaces.srv import AddTwoInts

class AddTwoIntsNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("AddTwoInts class is created")

    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"{str(request.a)} + {str(request.b)} = {str(response.sum)}")
        return response
    

def main(args=None):
    rclpy.init(args=args)
    the_node = AddTwoIntsNode()
    rclpy.spin(the_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

"""
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts {"a: 10, b: 20}"
"""
