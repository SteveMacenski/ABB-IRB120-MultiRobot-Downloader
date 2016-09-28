#!/usr/bin/env python

import ast
import rospy
from rospy import Duration
import std_msgs.msg
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryActionGoal
import time

def functional():
    pub_gary = rospy.Publisher('/gary/joint_trajectory_action/goal',
     FollowJointTrajectoryActionGoal, queue_size=10)
    pub_rosey = rospy.Publisher('/rosey/joint_trajectory_action/goal',
     FollowJointTrajectoryActionGoal, queue_size=10)
    rospy.init_node('traj_maker', anonymous=True)
    time.sleep(4)

    rate = rospy.Rate(0.01)

    while not rospy.is_shutdown():

           traj_waypoint_1_gary = JointTrajectoryPoint()
           traj_waypoint_1_rosey = JointTrajectoryPoint()

           traj_waypoint_1_gary.positions = [0,0,0,0,0,0]       
           traj_waypoint_1_rosey.positions = [0,0,0,0,0,0]

           traj_waypoint_1_rosey.time_from_start.secs = 10
           traj_waypoint_1_gary.time_from_start.secs = 10
           
           #  making message
           message_gary = FollowJointTrajectoryActionGoal()
           message_rosey = FollowJointTrajectoryActionGoal()
           
           #  required headers
           header_gary = std_msgs.msg.Header(stamp=rospy.Time.now())
           header_rosey = std_msgs.msg.Header(stamp=rospy.Time.now())
           message_gary.goal.trajectory.header = header_gary
           message_rosey.goal.trajectory.header = header_rosey
           message_gary.header = header_gary
           message_rosey.header = header_rosey
           
           #  adding in joints
           joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', \
                          'joint_5', 'joint_6']
           message_gary.goal.trajectory.joint_names = joint_names
           message_rosey.goal.trajectory.joint_names = joint_names
           
           #  appending up to 100 points
           # ex. for i in enumerate(len(waypoints)): append(waypoints[i])
           message_gary.goal.trajectory.points.append(traj_waypoint_1_gary)
           message_rosey.goal.trajectory.points.append(traj_waypoint_1_rosey)

          
           #  publishing to ROS node
           pub_gary.publish(message_gary)
           pub_rosey.publish(message_rosey)
         
           rate.sleep()
           
           if rospy.is_shutdown():
               break
           break
               

if __name__ == '__main__':
    try:
        functional()
    except rospy.ROSInterruptException:
        pass
