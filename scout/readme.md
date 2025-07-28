Checklist to begin GPS-based navigation with Scout 2.0 and Inertial Sense:
- launch scout_base and scout_description
- launch LiDAR SDK and pointcloud_to_laserscan
- Launch Inertial Sense ROS 2 software (ISRoverNetworkNMEA & is_gps_publisher_ros2)
- set local xy origin (map_frame_CU_hill.bash)
- launch py_get_init_pos to automatically set the initial pose for robot_localization (see note below)
- launch robot_localization (‘ros2 launch dual_ekf_navsat_scout.launch.py’)
- launch Nav2 (‘ros2 launch scout_gps_launch.py’)
- launch Rviz2 (‘ros2 launch nav2_bringup rviz_launch.py’)
- (optional) launch mapviz (‘ros2 launch mapviz mapviz.launch.py’)

## Note

Due to limitations with the Inertial Sense IMU NMEA message, the orientation info is not available in the sensor message. Therefore the Scout 2.0 must be facing due east when starting robot_localization.