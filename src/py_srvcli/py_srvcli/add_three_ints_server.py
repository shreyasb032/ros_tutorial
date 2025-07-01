from tutorial_interfaces.srv import AddThreeInts
import rclpy
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('add_three_ints_server')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info(f'Incoming request: a={request.a}, b={request.b}, c={request.c}')
        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    # Destroy the node explicitly
    minimal_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
