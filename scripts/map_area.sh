gnome-terminal -e "roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping"
gnome-terminal -e "sshpass -p 'turtlebot' ssh -XC pi@numel rosrun tadashi manualcontrol_node"
