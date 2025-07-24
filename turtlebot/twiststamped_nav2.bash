#!/bin/bash

ros2 run twist_stamper twist_stamper --ros-args -r cmd_vel_in:=cmd_vel_smoothed -r cmd_vel_out:=cmd_vel
