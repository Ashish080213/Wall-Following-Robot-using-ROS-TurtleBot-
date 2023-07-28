#! /usr/bin/env python3

# import rospy
# from sensor_msgs.msg import LaserScan

# def callback(msg):
#     print(len(msg.ranges))
# rospy.init_node('scan_values')
# sub = rospy.Subscriber('/scan', LaserScan, callback)
# rospy.spin()


# -------------------------------------------------------------------------------------------------


# import rospy
# from sensor_msgs.msg import LaserScan 
# from geometry_msgs.msg import Twist
# # Import the service message used by the service /find_wall
# from lab_project.srv import FindWallRequest, FindWall

# def callback(msg): 
#   print("Total values in range array: ",len(msg.ranges))
#   print("Front Laser value: ",msg.ranges[360]) #We print the distance to an obstacle in front of the robot
#   print("Right Laser value: ",(msg.ranges[180])) #We print the distance to an obstacle in right of the robot


# #If the distance to an obstacle in front of the robot is smaller than 0.5 meter, the robot will turn left
#   if msg.ranges[360] < 0.5:
#       move.linear.x = 0.0
#       move.angular.z = 1  

#   else:
#     if msg.ranges[180] > 0.2 and msg.ranges[180] < 0.3:
#        move.linear.x = 0.2
#        move.angular.z = 0.0

# #If the distance to an obstacle at the right side of the robot is greater than 0.3 meters, the robot will right left
#     if msg.ranges[180] > 0.3:
#         move.linear.x = 0.2
#         move.angular.z = -0.2

# #If the distance to an obstacle at the right side of the robot is smaller than 0.2 meters, the robot will turn left
#     if msg.ranges[180] < 0.2: 
#         move.linear.x = 0.2
#         move.angular.z = 0.2


#   print("linear speed: ",move.linear.x)
#   print("angular speed: ",move.angular.z)
#   pub.publish(move)


# rospy.init_node('project_node')
# # Wait for the service client /find_wall to be running
# rospy.wait_for_service('/find_wall')
# # Create the connection to the service
# find_wall_service = rospy.ServiceProxy('/find_wall', FindWall)
# # Create an object of type FindWallRequest
# find_wall_object = FindWallRequest()
# # Send through the connection the name of the trajectory to be executed by the robot
# result = find_wall_service(find_wall_object)
# # Print the result given by the service called
# print(result)

# sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
# print("Subscribed")
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #We publish to the cmd_vel topic
# print("Published")
# move = Twist()

# rospy.spin()


# --------------------------------------------------------------------------------------------------

# # If the distance to an obstacle in front of the robot is smaller than 0.5 meter, the robot will turn left
#   if msg.ranges[360] < 0.5:
#     move.linear.x = 0.0
#     move.angular.z = 0.49

#   else:
#     if msg.ranges[180] > 0.2 and msg.ranges[180] < 0.3:
#       move.linear.x = 0.15
#       move.angular.z = 0.0

# #If the distance to an obstacle at the right side of the robot is greater than 0.3 meters, the robot will right left
#     if msg.ranges[180] > 0.3:
#       move.linear.x = 0.05
#       move.angular.z = -0.15

# #If the distance to an obstacle at the right side of the robot is smaller than 0.2 meters, the robot will turn left
#     if msg.ranges[180] < 0.2: 
#       move.linear.x = 0.05
#       move.angular.z = 0.15



# ------------------------------------------------------------------------------------

# import rospy
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist
# from lab_project.srv import FindWall, FindWallRequest

# class WallFollower:
#     def __init__(self):
#         self.result = False
#         self.ranges = None
#         self.count1 = 0

#         rospy.init_node('project_node')
#         rospy.wait_for_service('/find_wall')        
#         self.find_wall_service = rospy.ServiceProxy('/find_wall', FindWall)
#         find_wall_object = FindWallRequest()
#         self.result = self.find_wall_service(find_wall_object)
#         print("WALL FOUND: ",self.result)
#         self.sub = rospy.Subscriber('/scan', LaserScan, self.callback, queue_size=1)
#         self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#         self.move = Twist()
#         rospy.spin()

#     def callback(self, msg):
#         self.ranges = msg.ranges

#         if self.count1 == 0:
#             print("Total values in range array: ", len(self.ranges))
#             print("Front Laser value: ", self.ranges[360])
#             print("Right Laser value: ", self.ranges[180])
#             print("Total values in range array: ", len(self.ranges))
#             self.count1 = 1
#             rospy.sleep(1)
#         self.perform_robot_movement()

#     def perform_robot_movement(self):
#         # if self.result == True:
#         rate = rospy.Rate(10) 
#         ranges = self.ranges
#         print("Front Laser Value: ", ranges[360])
#         print("Right Laser Value: ", ranges[180])
#         if ranges[360] < 0.5:
#             self.move.linear.x = 0.0
#             self.move.angular.z = 1
#             print("MOVING LEFT")

#         else:
#             if (0.2 < ranges[180]) and (ranges[180] < 0.3):
#                 self.move.linear.x = 0.1
#                 self.move.angular.z = 0.0
#             if ranges[180] > 0.3:
#                 self.move.linear.x = 0.1
#                 self.move.angular.z = -0.2
#             if ranges[180] < 0.2:
#                 self.move.linear.x = 0.1
#                 self.move.angular.z = 0.2

#             print("MOVING STRAIGHT")

#         print("Linear Speed: ", self.move.linear.x)
#         print("Angular Speed: ", self.move.angular.z)
#         self.pub.publish(self.move)
#         rate.sleep()

# if __name__ == '__main__':
#     wall_follower = WallFollower()


# -----------------------------------------------------------------------------------------------


# import rospy
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist
# from lab_project.srv import FindWall, FindWallRequest
# from lab_project.msg import OdomRecordFeedback, OdomRecordResult, OdomRecordGoal, OdomRecordAction
# import actionlib

# class WallFollower:
#     def __init__(self):
#         self.result = False
#         self.ranges = None
#         self.count1 = 0

#         rospy.init_node('project_node')

#         self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#         self.move = Twist()

#         rospy.wait_for_service('/find_wall') 
#         self.find_wall_service = rospy.ServiceProxy('/find_wall', FindWall)
        
#         find_wall_object = FindWallRequest()
#         self.result = self.find_wall_service(find_wall_object)

#         self.client = actionlib.SimpleActionClient('/record_odom', OdomRecordAction)

#         print("WALL FOUND: ", self.result)
#         self.sub = rospy.Subscriber('/scan', LaserScan, self.callback, queue_size=1)

#         self.client.wait_for_server()
#         goal = OdomRecordGoal()
#         self.client.send_goal(goal, feedback_cb = self.feedback_callback)
#         while (self.client.get_state() < 2):
#             pass
#         self.result = self.client.wait_for_result()
#         print('[Result]: ',(self.result.list_of_odoms))



#     def feedback_callback(self, feedback):
#         self.feedback = feedback.total_distance
#         print("TOTAL DISTANCE: ", self.feedback)


#     def callback(self, msg):
#         self.ranges = msg.ranges

#         if self.count1 == 0:
#             print("Total values in range array: ", len(self.ranges))
#             print("Front Laser value: ", self.ranges[360])
#             print("Right Laser value: ", self.ranges[180])
#             print("Total values in range array: ", len(self.ranges))
#             self.count1 = 1
#             rospy.sleep(1)

#     def perform_robot_movement(self):
#         # if self.result == True:
#         ranges = self.ranges
#         if ranges is not None:
#             print("Front Laser Value: ", ranges[360])
#             print("Right Laser Value: ", ranges[180])
#             if ranges[360] < 0.5:
#                 self.move.linear.x = 0.0
#                 self.move.angular.z = 1
#                 print("MOVING LEFT")

#             else:
#                 if (0.2 < ranges[180]) and (ranges[180] < 0.3):
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = 0.0
#                 if ranges[180] > 0.3:
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = -0.2
#                 if ranges[180] < 0.2:
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = 0.2

#                 print("MOVING STRAIGHT")

#             print("Linear Speed: ", self.move.linear.x)
#             print("Angular Speed: ", self.move.angular.z)
#             self.pub.publish(self.move)

#     def run(self):
#         rate = rospy.Rate(10) 
#         while not rospy.is_shutdown():
#             self.perform_robot_movement()
#             rate.sleep()

# if __name__ == '__main__':
#     wall_follower = WallFollower()
#     wall_follower.run()


# ------------------------------------------------------------------------------------------------------


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from lab_project.srv import FindWall, FindWallRequest
from lab_project.msg import OdomRecordFeedback, OdomRecordResult, OdomRecordGoal, OdomRecordAction
import actionlib

class WallFollower:
    def __init__(self):
        self.result = False
        self.ranges = None
        self.count1 = 0
        self.feedback = None
        self.action_result = None

        rospy.init_node('project_node')

        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.move = Twist()

        rospy.wait_for_service('/find_wall')
        self.find_wall_service = rospy.ServiceProxy('/find_wall', FindWall)

        find_wall_object = FindWallRequest()
        self.result = self.find_wall_service(find_wall_object)

        self.client = actionlib.SimpleActionClient('/record_odom', OdomRecordAction)

        print("WALL FOUND: ", self.result)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback, queue_size=1)

        self.client.wait_for_server()
        goal = OdomRecordGoal()
        self.client.send_goal(goal, feedback_cb=self.feedback_callback)

    def feedback_callback(self, feedback):
        if feedback is not None:
            self.feedback = feedback
            print("CURRENT TOTAL DISTANCE: ", self.feedback.current_total)
            rospy.sleep(1)

    def callback(self, msg):
        self.ranges = msg.ranges

        if self.count1 == 0:
            print("Total values in range array: ", len(self.ranges))
            print("Front Laser value: ", self.ranges[360])
            print("Right Laser value: ", self.ranges[180])
            print("Total values in range array: ", len(self.ranges))
            self.count1 = 1
            rospy.sleep(1)

    def perform_robot_movement(self):
        ranges = self.ranges
        if ranges is not None:
            print("Front Laser Value: ", ranges[360])
            print("Right Laser Value: ", ranges[180])
            if ranges[360] < 0.5:
                self.move.linear.x = 0.0
                self.move.angular.z = 0.49
                # self.move.angular.z = 1
                print("MOVING LEFT")

            else:
                if 0.2 < ranges[180] < 0.3:
                    self.move.linear.x = 0.15
                    # self.move.linear.x = 0.1
                    self.move.angular.z = 0.0
                elif ranges[180] > 0.3:
                    self.move.linear.x = 0.05
                    self.move.angular.z = -0.15
                    # self.move.linear.x = 0.1
                    # self.move.angular.z = -0.2
                elif ranges[180] < 0.2:
                    self.move.linear.x = 0.05
                    self.move.angular.z = 0.15
                    # self.move.linear.x = 0.1
                    # self.move.angular.z = 0.2

                print("MOVING STRAIGHT")

            print("Linear Speed: ", self.move.linear.x)
            print("Angular Speed: ", self.move.angular.z)
            self.pub.publish(self.move)
            rospy.sleep(0.2)

    def run(self):
        rate = rospy.Rate(10)
        temp = 0
        while not rospy.is_shutdown():
            if not temp:
                if self.feedback is not None:
                    print("FINAL TOTAL DISTANCE:", self.feedback.current_total)
                if self.client.get_state() == actionlib.GoalStatus.SUCCEEDED:
                    if self.action_result is None:
                        self.action_result = self.client.get_result()
                        if self.action_result is not None:
                            print("Action Result:", self.action_result.list_of_odoms)
                    self.move.linear.x = 0.0
                    self.move.angular.z = 0.0
                    self.pub.publish(self.move)
                    print("Robot stopped.")
                    temp = 1
                else:
                    self.perform_robot_movement()
            rate.sleep()

if __name__ == '__main__':
    wall_follower = WallFollower()
    wall_follower.run()

# ---------------------------------------------------------------------------------------------------------

# import rospy
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist
# from lab_project.srv import FindWall, FindWallRequest
# from lab_project.msg import OdomRecordFeedback, OdomRecordResult, OdomRecordGoal, OdomRecordAction
# import actionlib

# class WallFollower:
#     def __init__(self):
#         self.result = False
#         self.ranges = None
#         self.count1 = 0
#         self.feedback = None
#         self.action_result = None

#         rospy.init_node('project_node')

#         self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#         self.move = Twist()

#         rospy.wait_for_service('/find_wall')
#         self.find_wall_service = rospy.ServiceProxy('/find_wall', FindWall)

#         find_wall_object = FindWallRequest()
#         self.result = self.find_wall_service(find_wall_object)

#         self.client = actionlib.SimpleActionClient('/record_odom', OdomRecordAction)

#         print("WALL FOUND: ", self.result)
#         self.sub = rospy.Subscriber('/scan', LaserScan, self.callback, queue_size=1)

#         self.client.wait_for_server()
#         goal = OdomRecordGoal()
#         self.client.send_goal(goal, feedback_cb=self.feedback_callback)

#     def feedback_callback(self, feedback):
#         if feedback is not None:
#             self.feedback = feedback
#             print("CURRENT TOTAL DISTANCE: ", self.feedback.current_total)

#     def callback(self, msg):
#         self.ranges = msg.ranges

#         if self.count1 == 0:
#             print("Total values in range array: ", len(self.ranges))
#             print("Front Laser value: ", self.ranges[360])
#             print("Right Laser value: ", self.ranges[180])
#             print("Total values in range array: ", len(self.ranges))
#             self.count1 = 1
#             rospy.sleep(1)

#     def perform_robot_movement(self):
#         ranges = self.ranges
#         if ranges is not None:
#             print("Front Laser Value: ", ranges[360])
#             print("Right Laser Value: ", ranges[180])
#             if ranges[360] < 0.5:
#                 self.move.linear.x = 0.0
#                 self.move.angular.z = 1
#                 print("MOVING LEFT")

#             else:
#                 if 0.2 < ranges[180] < 0.3:
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = 0.0
#                 elif ranges[180] > 0.3:
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = -0.2
#                 elif ranges[180] < 0.2:
#                     self.move.linear.x = 0.1
#                     self.move.angular.z = 0.2

#                 print("MOVING STRAIGHT")

#             print("Linear Speed: ", self.move.linear.x)
#             print("Angular Speed: ", self.move.angular.z)
#             self.pub.publish(self.move)

#     def run(self):
#         rate = rospy.Rate(10)
#         while not rospy.is_shutdown():
#             if self.feedback is not None and self.feedback.current_total > 1.5 and self.action_result is None:
#                 self.action_result = self.client.get_result()
#                 if self.action_result is not None:
#                     print("Total Distance:", self.feedback.current_total)
#                     print("Action Result:", self.action_result.list_of_odoms)
#             self.perform_robot_movement()
#             rate.sleep()

# if __name__ == '__main__':
#     wall_follower = WallFollower()
#     wall_follower.run()


# --------------------------------------------------------------------------------------------------------