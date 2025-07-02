import rclpy
from rclpy.node import Node

class MinimalParam(Node):
    def __init__(self):
        super().__init__('minimal_param_node')
        self.declare_parameter('my_parameter', 'world')
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value
        self.get_logger().info(f'Hello {my_param}!')
        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

# This script defines a ROS 2 node that declares a parameter and updates it periodically.
# It logs a message using the parameter value and updates the parameter to a new value.
# The node is designed to run in a ROS 2 environment, and it uses the rclpy library for Python-based ROS 2 development.
# The node will print "Hello world!" every second and then update the parameter to "world".
