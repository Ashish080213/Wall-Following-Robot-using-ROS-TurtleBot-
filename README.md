# Wall-Following-Robot-using-ROS-TurtleBot-

This project on wall finding and following behavior for a TurtleBot involved creating a ROS-based simulation where a robot could autonomously follow a wall. The goal was to implement a robot behavior that would make it move forward while maintaining a constant distance from the wall on its right-hand side. Here's a brief overview of the key steps and functionalities implemented in the project:

1. Wall Following Behavior:

The robot's task was to follow the wall on its right side while maintaining a 30cm distance from the wall.

2. Subscribing to Laser Scan Topic:

The robot subscribed to the /scan topic, which provided laser scan data from the robot's sensors. The data helped to detect obstacles and measure distances.

3. Calculating Wall Distance:

The robot analyzed the laser scan data and selected the right-most ray to measure the distance from the robot to the wall on its right side.

4. Controlling Robot Movement:

Based on the distance measured, the robot made decisions on how to adjust its movement.
If the distance was greater than 0.3m, the robot approached the wall slightly by adding rotational speed.
If the distance was between 0.2m and 0.3m, the robot moved forward without any rotation.
If the distance was less than 0.2m, the robot moved away from the wall by adding rotational speed in the opposite direction.

5. Handling Wall Transitions:

The robot was programmed to handle wall transitions. When the robot reached the end of one wall and found another wall in front of it, it would smoothly transition from following the current wall to following the new wall.
This was done by using the front laser ray and turning fast to the left while moving forward.

6. Creating a Service Server:

A service server named find_wall was created to initiate the process of wall finding.
When the server was called, the robot would look for the nearest wall and position itself parallel to it.

7. Creating an Action Server:

An action server named record_odom was implemented to record the robot's odometry over time.
The server would start recording (x, y, theta) odometry at one-second intervals.
As feedback, the server provided the total distance the robot had moved so far.

8. Creating a Launch File:

A launch file named main.launch was created to launch both the wall following node and the service server node.
This launch file enabled testing both functionalities together.

9. Testing and Simulation:

The wall following and odometry recording functionalities were tested in a simulation environment.
The simulation allowed debugging and verifying the correctness of the robot's behavior.
The project aimed to demonstrate how to control a robot using ROS topics, services, and action servers to achieve a wall following behavior and record odometry data. The simulated robot was able to autonomously follow walls, handle transitions between walls, and record its movements. The concepts learned in this project could be applied to real-world robotic systems for various applications, such as exploration and navigation.
