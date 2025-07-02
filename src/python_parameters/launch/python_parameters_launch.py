from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_parameters',
            executable='python_parameters_node',
            name='custom_minimal_param_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'my_parameter': 'earth'}
            ]
        )
    ])

# This launch file starts the python_parameters_node with a custom parameter 'my_parameter' set to 'earth'.
# It is designed to run in a ROS 2 environment, and it uses the launch and launch_ros libraries for launching ROS 2 nodes.