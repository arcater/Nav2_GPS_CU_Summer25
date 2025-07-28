Checklist to begin GPS-based navigation with a simulated Turtlebot when all needed software is installed:
- launch turtlebot_gps (see note below)
- set local xy origin (map_frame_CU_hill.bash)
- launch robot_localization (‘ros2 launch dual_ekf_navsat_turtlebot.launch.py’)
- launch Nav2 (‘ros2 launch bringup_launch.py’)
- launch twist_stamper (twiststamped_nav2.bash)
- launch Rviz2 (‘ros2 launch nav2_bringup rviz_launch.py’)
- (optional) launch mapviz (‘ros2 launch mapviz mapviz.launch.py’)

## Note

Launch turtlebot_gps with x_pose:=11 so it begins on the sidewalk. robot_localization is currently configured for the turtlebot to start at this position. Do not move the turtlebot before launching robot_localization.

‘ros2 launch turtlebot_gps headless_gps_world.launch.py x_pose:=11’
or
‘ros2 launch turtlebot_gps gps_world.launch.py x_pose:=11’

Use ‘gazebo-teleop.bash’ to manually control the turtlebot. Useful if the turtlebot is stuck in the keepout filter.