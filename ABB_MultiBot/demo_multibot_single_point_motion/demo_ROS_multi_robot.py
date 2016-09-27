#!/usr/bin/env python

import ast
import rospy
import std_msgs.msg
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryActionGoal
import time

def functional(commanded_trajectory):
    pub_gary = rospy.Publisher('/gary/joint_trajectory_action/goal', FollowJointTrajectoryActionGoal, queue_size=10)
    pub_rosey = rospy.Publisher('/rosey/joint_trajectory_action/goal', FollowJointTrajectoryActionGoal, queue_size=10)
    rospy.init_node('traj_maker', anonymous=True)
    time.sleep(4)

    rate = rospy.Rate(0.10)
    i = 0
    while not rospy.is_shutdown():
       for command in commanded_trajectory:
           i += 1
           msg_gary = JointTrajectory()
           msg_rosey = JointTrajectory()
           
           traj_waypoints_gary = JointTrajectoryPoint()
           traj_waypoints_rosey = JointTrajectoryPoint()

           # JointTrajectory part of message
           header_gary = std_msgs.msg.Header()
           header_rosey = std_msgs.msg.Header()
           
           header_gary.stamp = rospy.Time.now()
           header_rosey.stamp = rospy.Time.now()
           
           msg_gary.header = header_gary
           msg_rosey.header = header_rosey
           
           msg_gary.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', \
                              'joint_5', 'joint_6']
           msg_rosey.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', \
                              'joint_5', 'joint_6']

           traj_waypoints_gary.positions = command
           
           traj_waypoints_rosey.positions = [-1*elem for elem in command]

           traj_waypoints_rosey.time_from_start.secs = 0 + 2*i #first move slow
           traj_waypoints_gary.time_from_start.secs = 0 + 2*i
           
           msg_gary.points = [traj_waypoints_gary]
           msg_rosey.points = [traj_waypoints_rosey]
           
           print traj_waypoints_gary.positions
           print traj_waypoints_rosey.positions
           
           #Follow... together
           message_gary = FollowJointTrajectoryActionGoal()
           message_rosey = FollowJointTrajectoryActionGoal()
           
           message_gary.goal.trajectory = msg_gary
           message_rosey.goal.trajectory = msg_rosey
           
           message_gary.header = header_gary
           message_rosey.header = header_rosey
           
           pub_gary.publish(message_gary)
           pub_rosey.publish(message_rosey)
           
           rate.sleep()
           
           if rospy.is_shutdown():
               break



if __name__ == '__main__':
    commandL = []
    f = open('traj.txt','r')
    for line in f:
        parse_line = line.replace('\n','')
        parse_line = parse_line.replace(
        "{joint_names: {'joint_1', 'joint_2', 'joint_3' 'joint_4' 'joint_5', 'joint_6'}, points: ",'')
        positions_position = parse_line.find('positions')
        velocities_position = parse_line.find('velocities')
        
        position_command = parse_line[positions_position+10:velocities_position-2]

        commandL.append(ast.literal_eval(position_command))


   


    try:
        functional(commandL)
    except rospy.ROSInterruptException:
        pass
