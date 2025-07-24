#!/bin/bash

ros2 topic pub /local_xy_origin geometry_msgs/msg/PoseStamped "header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: 'map'
pose:
  position:
    x: -75.00
    y: 44.663
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
