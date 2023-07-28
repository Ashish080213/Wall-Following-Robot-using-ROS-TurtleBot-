#! /usr/bin/env python

# import rospy
# from lab_project.srv import FindWall, FindWallResponse # you import the service message python classes 
#                                                        # generated from FindWall.srv.
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist
# import math

# def value(ranges):
#     global min_value    
#     min_value = (min(ranges))
#     return min_value


# def laser_callback(beam):
#     global count
#     global count2
#     global min_value
#     global turn_check
#     global move_front_check

#     ranges = beam.ranges
#     print("Total values in range array: ",len(ranges))
#     print("Front Laser value: ", ((ranges[360]))) #We print the distance to an obstacle in front of the robot
#     print("Right Laser value: ", (ranges[180])) #We print the distance to an obstacle in right of the robot
#     if count == 0:
#         min_value = value(ranges)
#         count = 1
#         turn_check = 1
#     min_value = round((min_value),1)

#     # min_index = ranges.index(min_value)
#     # print(min(ranges))

#     front_range = math.floor((ranges[360]) * 10) / 10
#     print("Front Laser value: ",front_range) #We print the distance to an obstacle in front of the robot

#     if front_range > min_value and turn_check == 1:
#         print(min_value)
#         move.angular.z = 0.2
#         move.linear.x = 0.0
#         print("turning")
#         pub.publish(move)

#     elif turn_check == 1:
#         move.angular.z = 0.0
#         move.linear.x = 0.0
#         print("stopping")
#         move_front_check = 1
#         pub.publish(move)

#     if move_front_check == 1:
#         if front_range > 0.2:
#             print("moving front")
#             move.angular.z = 0.0
#             move.linear.x = 0.1
#             pub.publish(move)
#         else:
#             move.angular.z = 0.0
#             move.linear.x = 0.0
#             pub.publish(move)
#             move_front_check = 0
#         turn_check = 0
        
#     if front_range <= 0.2 or count2 == 1:
#         if abs(round(ranges[180],2) - round(min(ranges),2)) > 0.02:
#             # print(math.floor((ranges[180]) * 10) / 10)
#             print(round(min(ranges),2))
#             print(round(ranges[180],2))
#             move.angular.z = 0.2
#             move.linear.x = 0.0
#             pub.publish(move)
#             count2 = 1
#         else:
#             move.angular.z = 0.0
#             move.linear.x = 0.
#             print("DONE")
#             pub.publish(move)

# def my_callback(request):
    
#     my_response = FindWallResponse()
#     my_response.wallfound = True
#     return  my_response # the service Response class, in this case FindWallResponse

# count = 0
# count2 = 0
# min_value = 0
# turn_check = 0
# move_front_check = 0

# rospy.init_node('service_node') 
# my_service = rospy.Service('/find_wall', FindWall , my_callback) # create the Service called find_wall with the defined callback
# sub = rospy.Subscriber('/scan', LaserScan, laser_callback, queue_size=1) #We subscribe to the laser's topic
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #We publish to the cmd_vel topic
# move = Twist()
# rate = rospy.Rate(2)
# rospy.spin() # maintain the service open.


# -------------------------------------------------------------------------------------

import rospy
from lab_project.srv import FindWall, FindWallResponse
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class WallFinder:
    def __init__(self):

        self.count1 = 0
        self.count2 = 0
        self.min_value = 0
        self.move_front_check = 0
        self.ranges = None
        # self.service_called = False
        self.result_response = False
        self.ranges_available = False  

        rospy.init_node('service_node')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.move = Twist()
        self.sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback, queue_size=1)
        self.my_service = rospy.Service('/find_wall', FindWall, self.my_callback)
        self.rate = rospy.Rate(10)
        rospy.spin()

    def value(self, ranges):
        self.min_value = min(ranges)
        return self.min_value

    def laser_callback(self, beam):
        # if not self.service_called:
        #     return
        self.ranges = beam.ranges
        self.ranges_available = True 
        if self.count1 == 0:
            print("Total values in range array: ", len(self.ranges))
            print("Front Laser value: ", self.ranges[360])
            print("Right Laser value: ", self.ranges[180])
            self.count1 = 1


    def my_callback(self, request):
        # self.service_called = True

        # print("ok: ", ranges[360])
        # if ranges is not None: 
        # if self.ranges_available: 
        while self.ranges is None:
            rospy.loginfo("Waiting for laser scan data...")
            rospy.sleep(0.1)

        ranges = self.ranges
        print("Front Laser value: ", ranges[360])
        print("Right Laser value: ", ranges[180])

        self.min_value = self.value(ranges)
        self.min_value = round(self.min_value, 1)
        print("Min Laser Value: ", self.min_value)
        front_range = math.floor(ranges[360] * 10) / 10
        
        # while (front_range > self.min_value):
        while (abs(front_range - self.min_value) > 0.1):
            print("CURRENT Front Laser value: ", front_range)
            print("DESIRED Front Laser Value: ", self.min_value)
            self.move.angular.z = 0.2
            self.move.linear.x = 0.0
            self.pub.publish(self.move)
            print("TURNING")
            ranges = self.ranges
            front_range = math.floor(ranges[360] * 10) / 10
            rospy.sleep(0.5)

        self.move.angular.z = 0.0
        self.move.linear.x = 0.0
        self.move_front_check = 1
        self.pub.publish(self.move)
        print("STOPPED")
        print("ROBOT FACING TO THE WALL")
        rospy.sleep(2)

        while (self.move_front_check == 1):
            if front_range > 0.3:
                self.move.angular.z = 0.0
                self.move.linear.x = 0.1
                self.pub.publish(self.move)
                print("MOVING TOWARDS WALL")
            else:
                self.move.angular.z = 0.0
                self.move.linear.x = 0.0
                self.pub.publish(self.move)
                print("STOPPED")
                self.move_front_check = 0
                rospy.sleep(1)
            ranges = self.ranges
            front_range = math.floor(ranges[360] * 10) / 10
            rospy.sleep(0.1)

        while (front_range <= 0.3 or self.count2 == 1):
            if abs(round(ranges[180], 2) - round(min(ranges), 2)) > 0.02:
                print("CURRENT Right Laser Value: ", round(ranges[180], 2))
                print("DESIRED Right Laser Value: ", round(min(ranges), 2))
                print("TURNING LEFT")
                self.move.angular.z = 0.2
                self.move.linear.x = 0.0
                self.pub.publish(self.move)
                self.count2 = 1
            else:
                self.move.angular.z = 0.0
                self.move.linear.x = 0.0
                print("DONE, whole proccess completed!")
                self.count2 = 0
                self.pub.publish(self.move)
            ranges = self.ranges
            front_range = math.floor(ranges[360] * 10) / 10
            rospy.sleep(0.5)

        # rospy.loginfo("Wall following behavior initiated.")
        my_response = FindWallResponse()
        my_response.wallfound = True
        if  my_response.wallfound == True:
            rospy.loginfo("WALL FOUND.")
            rospy.loginfo("Ready for the Service again!!!.")

            self.result_response = True
            self.count1 = 0
            self.count2 = 0
            self.min_value = 0
            self.move_front_check = 0
            self.ranges = None
            # self.service_called = False

        return self.result_response

        # else:
        #     rospy.logwarn("Laser scan data is not available.")

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    wall_finder = WallFinder()
    wall_finder.run()




