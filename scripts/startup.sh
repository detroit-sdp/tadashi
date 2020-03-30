gnome-terminal -e "roscore"
gnome-terminal -e "sshpass -p 'turtlebot' ssh -XC pi@numel roslaunch turtlebot3_bringup turtlebot3_robot.launch"
