from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp_parameters',
            executable='cpp_parameters_node',
            name='custom_minimal_param_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'my_parameter': 'earth'}
            ]
        )
    ])
# This launch file starts the cpp_parameters_node with a custom parameter 'my_parameter' set to 'earth'.