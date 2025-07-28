# Nav2_GPS_CU_Summer25

This is the main github repository documenting the implementation of GPS-based Navigation using Nav2. Summer 2025 at Clarkson University.

![RVIZ2 & Mapviz screenshot and Scout 2.0 picture](/scoutandscreenshots.jpg)

This repository contains:
- Nav2 and robot_localization launch scripts and parameter files for use with an AgileX Scout 2.0 and a simulated Turtlebot3
- keepout_filter of some of the sidewalks on Clarkson University’s Potsdam campus
- a python script to help create keepout filters that lineup with orthoimagery
- mapviz config
- some helpful bash scripts


Related repositories to assist with running/testing GPS-based navigation with Nav2:
- [turtlebot_gps](https://github.com/arcater/turtlebot_gps)
- [ISRoverNetworkNMEA] (https://github.com/arcater/ISRoverNetworkNMEA)
- [is_gps_publisher_ros2](https://github.com/ChesterMK7/is_gps_publisher_ros2)
- [py_get_init_pos](https://github.com/ChesterMK7/py_get_init_pos)


# Usage

All scripts from this repository and the previously listed related repositories are for use with ROS 2 Humble. Tested using Ubuntu 22.04 LTS. 

The files in the scout directory are designed for use with the AgileX Scout 2.0 combined with an Inertial Sense uINS sensor. Only intended for those with access to the hardware setup present at Clarkson University.

The scripts in the turtlebot directory combined with [turtlebot_gps](https://github.com/arcater/turtlebot_gps) can be used by anyone to simulate GPS-based navigation with Nav2. A Turtlebot in an empty gazebo world will output GPS coordinates as if it were on-campus at Clarkson University.

Consult the readmes of the turtlebot and scout directories for more info on using the scripts.

# More Info

More information about Nav2, LiDAR-based navigation, and some of the hardware used at Clarkson University can be found in the following github: [AgileX_Autonomous_Driving_CU_Summer_2024](https://github.com/RowanW09/AgileX_Autonomous_Driving_CU_Summer_2024).

Additional information on how to reproduce the steps taken to implement GPS-based navigation with Nav2 can be found in [readme.pdf](/readme.pdf). This guide assumes the reader is already familiar with ROS 2 and setting up Nav2 for LiDAR-based navigation. 
