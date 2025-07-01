import sys
from tutorial_interfaces.srv import AddThreeInts

import rclpy
from rclpy.node import Node

class AddThreeIntsClient(Node):

    def __init__(self):
        super().__init__('add_three_ints_client')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, a, b, c):
        req = AddThreeInts.Request()
        req.a = a
        req.b = b
        req.c = c
        self.future = self.cli.call_async(req)
        
        return self.future
    
def main():
    rclpy.init()

    add_three_ints_client = AddThreeIntsClient()
    future = add_three_ints_client.send_request(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    rclpy.spin_until_future_complete(add_three_ints_client, future)

    if future.result() is not None:
        add_three_ints_client.get_logger().info(f'Result of add_three_ints: {future.result().sum}')
    else:
        add_three_ints_client.get_logger().error('Exception while calling service: %r' % future.exception())

    add_three_ints_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ros2 run py_srvcli add_three_ints_client <a> <b> <c>")
        sys.exit(1)
    main()
