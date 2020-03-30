gnome-terminal -e "roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=~/saved_maps/map.yaml"
gnome-terminal -e "rosrun tadashi sendgoal_node"
gnome-terminal -e "sshpass -p 'turtlebot' ssh -XC pi@numel python server.py"
gnome-terminal -e "sshpass -p 'turtlebot' ssh -XC pi@numel python serial_test_node.py"
