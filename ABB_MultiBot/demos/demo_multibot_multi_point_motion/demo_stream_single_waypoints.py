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
    time.sleep(3)

    rate = rospy.Rate(0.25)

    commanded_trajectory = [[.31, -.051, .33, -.55, .28, .60], #P1
        [.14726, -.014151, .166507, -.33571, .395997, .38657], #P2
        [-.09309, .003150, .003559, .16149, .524427, -.1867],  #P3
        [-.27752, .077886, -.1828, .38563, .682589, -.44665],  #P4
        [-.09309, .003150, .003559, .16149, .524427, -.1867],  #P3
        [.14726, -.014151, .166507, -.33571, .395997, .38657]] #P2
        #this will repeat

    while not rospy.is_shutdown():
       i=0
       for command in commanded_trajectory:

           #  first way to define a point
           traj_waypoint_1_gary = JointTrajectoryPoint()
           traj_waypoint_1_rosey = JointTrajectoryPoint
           
           #  second way to define a point
           traj_waypoint_gary = JointTrajectoryPoint(positions=command,
            time_from_start = Duration(1))
           traj_waypoint_rosey = JointTrajectoryPoint(positions=command,
            time_from_start = Duration(1))  
           
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
           if (i > 0):
               message_gary.goal.trajectory.points.append(old_waypoint)
           message_gary.goal.trajectory.points.append(traj_waypoint_gary)
           if (i > 0):
               message_rosey.goal.trajectory.points.append(old_waypoint) #current location
           message_rosey.goal.trajectory.points.append(traj_waypoint_rosey) #now "second" for timing

           #  publishing to ROS node
           #if (i % 3 == 0):  # every 3 cycles
           pub_gary.publish(message_gary)
           pub_rosey.publish(message_rosey)
           print 'published: ' + str(commanded_trajectory[i])
         
           rate.sleep()
           i += 1
           old_waypoint = traj_waypoint_rosey
           old_waypoint.time_from_start.secs = 0
           #if i ==1:
           #    rate.sleep()
           #    rate.sleep()
           #    rate.sleep()
           if i == 5:
               return
           if rospy.is_shutdown():
               break
               

if __name__ == '__main__':
    try:
        functional()
    except rospy.ROSInterruptException:
        pass
