# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from nav2_common.launch import RewrittenYaml


def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_params = os.path.join(os.getcwd(), "params", "nav2_params.yaml") # "nav2_no_map_params.yaml")

    navigation2_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(os.getcwd(), "turtlebot_navigation_launch.py")
        ),
        launch_arguments={
            "use_sim_time": "True", # True
            "params_file": nav2_params, # configured_params,
            "autostart": "False", # True
        }.items(),
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # simulator launch
    # ld.add_action(gazebo_cmd)

    # navigation2 launch
    ld.add_action(navigation2_cmd)


    return ld
