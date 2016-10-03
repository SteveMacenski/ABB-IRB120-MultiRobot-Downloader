# ABB_MultiBot_Feedback_Project

This repository will be a workground for a number of things to support a multi-robot ABB IRB120 experiment. 
A TBD force/torque sensor and visual rod segmentation work will be completed for feedback on the robots motion planner. 

This repository will also act as a staging ground for my updated ABB_Drivers package which will enable 2 or more robots to interact in ROS with a single IRC5 controller. Setup instructions for how to setup multiple robots and changes to the ROS-I abb_driver will be included. Demos of code running on the ROS-I trajectory action controller are included for those wishing to not use moveit. 

ABB_MultiBot pkg is for multiple robots in ROS through a IRC5 with additional drive modules. See instructions below for setup.

FT_sensor_feedback pkg is for the setup and launching of the force torque sensor with gravity compensation and feedback loops for motion planning

visual_feedback pkg is for the setup and launching fo the depth and RGB cameras for feedback of motion planning

elastic_rod_experiment pkg uses all of the above packages in combination and does the motion planning and feedback for control over the robot manipulators with the rod. 

## Lab Start-Up Instructions For Twin ABB IRB120 robots without F/T or Visual Feedback
1. Ensure that the ethernet connection is made between the ROSmaster computer and the IRC5 controller.

2. Power on the IRC5 and accompanying additional drive module, wait for start up on the flexpendant.

3. Turn on the motors by pressing the Motor On button on the IRC5 controller. This is the round white button that may be flashing.

4. Start the controller connection to the ROSmaster computer, 

`roslaunch ABB_MultiBot abb_multi_robot_single_controller.launch`

You should see on the flexpendant 4 connections (a stateServer and motionServer for each robot).

5. Move the program pointer to the main entry function on the flexpendant.

6. Release the breaks and enable the robot motors by pressing the play button on the flexpendant. Note: you may stop the robot motion at anytime by pressing the stop button below the play button.
 
7. In a separate terminal, execute the ROS node, python, or C++ program. Alternatively, making a new launch file to open the node and open the robot connection would be advantageous for complex launches and additional drivers. An example: 

`python demo_ROS_multi_robot.py`

in the demo_multibot_multi_point_motion directory. 

## Data Structure
TBA

## Instructions for modification of abb_driver for multiple robots through ethernet connection to an IRC5 with additional drive modules. 
TBA, general notes: make new copies of each of the global variables stored in the ros_common.sys file for each additional robot and replace them in the copies of the motionServer.mod, stateServer.mod, and motion.mod files, also for each robot. 

## ABB_MultiBot / multi_robot_single_controller.launch
This launch file will launch the two robots on the workstation computer. Each robot will be in its own namespace and have its own separate topics for publishing and substribing telemetry. Assumes setup of RAPID on IRC5. 

## ABB_MultiBot / Demo / [single, Multi] MultiBot Motion
This includes a python ROS node meant as a quick test of your multirobot abb_driver was currently installed on the IRC5 controller and the launch file is communicating with the controller. This will make the two robots complete a simple trajectory as outlined in the traj.txt file. The single will execute 1 point at a time at a fixed rate. The multi will execute multiple points in one download motion. This acts as a good first tutorial in ROS-I motion planning.

## ABB_MultiBot / Demo / Multi Straight Line
This just moves the robot in a very roughly (not really) straight line diagonal path to test that the robot will interpolate velocities between waypoints and not simply 'stop' at the end of one point before continuing. 

