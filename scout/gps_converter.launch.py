from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions
import os
import launch.actions


def generate_launch_description():
    return LaunchDescription(
        [
            launch_ros.actions.Node(
                package="is_gps_publisher_ros2",
                executable="gps_output_publisher",
                name="gps_out_ros2",
                output="screen",
            ),
            launch_ros.actions.Node(
                package="py_get_init_pos",
                executable="gps_convert",
                name="gps_to_xy",
                output="screen",
            ),
        ]
    )
