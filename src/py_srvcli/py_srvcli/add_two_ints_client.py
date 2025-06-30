import sys
from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node

class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__('add_two_ints_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        self.future = self.cli.call_async(req)
        
        return self.future
    
def main():
    rclpy.init()

    add_two_ints_client = AddTwoIntsClient()    
    future = add_two_ints_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(add_two_ints_client, future)

    if future.result() is not None:
        add_two_ints_client.get_logger().info(f'Result of add_two_ints: {future.result().sum}')
    else:
        add_two_ints_client.get_logger().error('Exception while calling service: %r' % future.exception())

    add_two_ints_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ros2 run py_srvcli add_two_ints_client <a> <b>")
        sys.exit(1)
    main()
