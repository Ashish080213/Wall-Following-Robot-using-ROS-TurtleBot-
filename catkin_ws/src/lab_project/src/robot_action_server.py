#! /usr/bin/env python
import rospy
import actionlib
from lab_project.msg import OdomRecordFeedback, OdomRecordResult, OdomRecordAction
from geometry_msgs.msg import Point32
from nav_msgs.msg import Odometry
import math

class OdomClass(object):
    def __init__(self):
        self.increment_distance = 0
        self.total_distance = 0
        self._as = actionlib.SimpleActionServer("record_odom", OdomRecordAction, self.goal_callback, False)
        self._as.start()
        rospy.loginfo('action server is ready')
        self._feedback = OdomRecordFeedback()
        self._result = OdomRecordResult()
        self.sub = rospy.Subscriber('/odom', Odometry, self.odom_list_callback)
        rospy.loginfo("subscriber is ready")
        self.odom = Odometry()
    
    def odom_list_callback(self, readings):
        self.odom = readings
    
    def goal_callback(self, goal):
        self._result.list_of_odoms = []
        r = rospy.Rate(1)
        self._feedback.current_total = 0
        rospy.loginfo('Executing....')
        i = 0
        while True:
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                self._as.set_preempted()
                success = False
                break
            pos_x = self.odom.pose.pose.position.x
            pos_y = self.odom.pose.pose.position.y
            ori_z = self.odom.pose.pose.orientation.z
            self._result.list_of_odoms.append(Point32(x=pos_x, y=pos_y, z=ori_z))

            if i != 0:
                self.increment_distance = math.pow(
                    (math.pow(self._result.list_of_odoms[i].x - self._result.list_of_odoms[i - 1].x, 2) +
                     math.pow(self._result.list_of_odoms[i].y - self._result.list_of_odoms[i - 1].y, 2)), 0.5)
                self.total_distance += self.increment_distance
                self._feedback.current_total = self.total_distance
                self._as.publish_feedback(self._feedback)
            
            i += 1
            if self.total_distance > 5.5:
                rospy.loginfo('ONE LAP DONE')
                success = True
                break
            r.sleep()
    
        if success:
            rospy.loginfo('Succeeded')
            rospy.loginfo("One lap done successfully")
            self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
    rospy.init_node('Odom_node')
    OdomClass()
    rospy.spin()


# ----------------------------------------------------------------------------------------------------------

# import rospy
# import actionlib
# from lab_project.msg import OdomRecordFeedback, OdomRecordResult, OdomRecordAction
# from geometry_msgs.msg import Point32
# from nav_msgs.msg import Odometry
# import math

# class OdomClass(object):
    

#   def __init__(self):

#     self.increment_distance = 0
#     self.total_distance = 0
#     self._as = actionlib.SimpleActionServer("record_odom", OdomRecordAction, self.goal_callback, False)
#     self._as.start()
#     rospy.loginfo('action server is ready')
#     self._feedback = OdomRecordFeedback()
#     self._result   = OdomRecordResult()
#     self.sub = rospy.Subscriber('/odom',Odometry,self.odom_list_callback)
#     rospy.loginfo("subscriber is ready")
#     self.odom = Odometry() 


#   def odom_list_callback(self, readings):
#     self.odom_list = readings

    
#   def goal_callback(self, goal):

#     list_of_odoms = [[0.0,0.0,0.0]]
#     self._result.list_of_odoms = []

#     r = rospy.Rate(1)
    
#     self._feedback.current_total = 0
#     rospy.loginfo('Executing....')
    
#     i = 0
#     while(True):
    
#       if self._as.is_preempt_requested():
#         rospy.loginfo('The goal has been cancelled/preempted')
#         self._as.set_preempted()
#         success = False
#         break
#       pos_x = self.odom.pose.pose.position.x
#       pos_y = self.odom.pose.pose.position.y
#       ori_z = self.odom.pose.pose.orientation.z
#       list_of_odoms.append([pos_x,pos_y,ori_z])

#       if i != 0:
#         self.increment_distance = math.pow((math.pow(self.list_of_odoms[i][0]-self.list_of_odoms[i-1][0],2)+math.pow(self.list_of_odoms[i][1]-self.list_of_odoms[i-1][1],2)),0.5)
#       self.total_distance = self.total_distance + self.increment_distance
#       self._feedback.current_total = self.total_distance
#       self._as.publish_feedback(self._feedback)
#       i+=1

#       if self.total_distance > 1.5:
#         rospy.loginfo('ONE LAP DONE')
#         success = True
#         break
#       r.sleep()
    
#     if success:
#       self._result.list_of_odoms = self.odom_list
#       rospy.loginfo('Succeeded')
#       rospy.loginfo("One lap done successfully")
#       print(list_of_odoms)
#       self._as.set_succeeded(self._result)
      
# if __name__ == '__main__':
#   rospy.init_node('Odom_node')
#   OdomClass()
#   rospy.spin()



#   #! /usr/bin/env python
# import rospy

# import actionlib

# from actionlib_tutorials.msg import FibonacciFeedback, FibonacciResult, FibonacciAction

# class FibonacciClass(object):
    
#   # create messages that are used to publish feedback/result
#   _feedback = FibonacciFeedback()
#   _result   = FibonacciResult()

#   def __init__(self):
#     # creates the action server
#     self._as = actionlib.SimpleActionServer("fibonacci_as", FibonacciAction, self.goal_callback, False)
#     self._as.start()
    
#   def goal_callback(self, goal):
#     # this callback is called when the action server is called.
#     # this is the function that computes the Fibonacci sequence
#     # and returns the sequence to the node that called the action server
    
#     # helper variables
#     r = rospy.Rate(1)
#     success = True
    
#     # append the seeds for the fibonacci sequence
#     self._feedback.sequence = []
#     self._feedback.sequence.append(0)
#     self._feedback.sequence.append(1)
    
#     # publish info to the console for the user
#     rospy.loginfo('"fibonacci_as": Executing, creating fibonacci sequence of order %i with seeds %i, %i' % ( goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))
    
#     # starts calculating the Fibonacci sequence
#     fibonacciOrder = goal.order
#     for i in range(1, fibonacciOrder):
    
#       # check that preempt (cancelation) has not been requested by the action client
#       if self._as.is_preempt_requested():
#         rospy.loginfo('The goal has been cancelled/preempted')
#         # the following line, sets the client in preempted state (goal cancelled)
#         self._as.set_preempted()
#         success = False
#         # we end the calculation of the Fibonacci sequence
#         break
      
#       # builds the next feedback msg to be sent
#       self._feedback.sequence.append(self._feedback.sequence[i] + self._feedback.sequence[i-1])
#       # publish the feedback
#       self._as.publish_feedback(self._feedback)
#       # the sequence is computed at 1 Hz frequency
#       r.sleep()
    
#     # at this point, either the goal has been achieved (success==true)
#     # or the client preempted the goal (success==false)
#     # If success, then we publish the final result
#     # If not success, we do not publish anything in the result
#     if success:
#       self._result.sequence = self._feedback.sequence
#       rospy.loginfo('Succeeded calculating the Fibonacci of order %i' % fibonacciOrder )
#       self._as.set_succeeded(self._result)
      
# if __name__ == '__main__':
#   rospy.init_node('fibonacci')
#   FibonacciClass()
#   rospy.spin()