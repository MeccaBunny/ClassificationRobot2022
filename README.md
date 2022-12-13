## ClassificationRobot2022

Uploaded files are located at /home/meccabunny/robot_ws/src/robot_arm_controller/robot_arm_controller/

Also yolov3.weights should be added to that directory too.

link to download yolov3.weights: https://pjreddie.com/darknet/yolo/

The environment I used to develop this robot is ubuntu 22.04. and the Open-source-software I used is ROS-humble, yolov3, opencv 4.6.0.

"robotParts" contains the stl file I used to 3d print this robot arm.

"robotArm" contains the arduino file for robot arm. <br/> <br/>



To Activate a robot,

First, Turn on 6 terminals in ubuntu. <br/> <br/>



Second, turn on arduino ise and upload the file given in robotArm.

$ arduino

Uploading the code directly will cause an error.

The reason for this error is because usb port connected to arduino cable is not authorized.

Copy and paste this command in 2nd terminal.

$ sudo chmod a+rw /dev/ttyACM0 <br/> <br/>



Third, for each terminal, turn on the ROS nodes to activate the robot arm.

To do this, copy and paste this commands to 3rd, 4th, 5th terminal.

$ ros2 run robot_arm_controller actionBuf

$ ros2 run robot_arm_controller inverse_kinematics

$ ros2 run robot_arm_controller CameraToUV  <br/> <br/>



Finally, copy and paste this command to 6th terminal.

$ cs

$ code .

Meaning of this code is that you are turning on vscode in directory "~/robot_ws/src/".

Then, run the python code, "ObjectDetectionCamera.py"

<br/>

