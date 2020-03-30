cd ~/catkin_ws/src/
sudo apt-get install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers sshpass
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/detroit-sdp/tadashi
cd ~/catkin_ws && catkin_make
IP=$(ifconfig | grep -o -E '192.[^ ]+' | head -n 1)
echo "export ROS_MASTER_URI=http://$IP:11311" >> ~/.bashrc
echo "export ROS_HOSTNAME=$IP" >> ~/.bashrc
source ~/.bashrc
sshpass -p 'turtlebot' ssh -XC pi@numel turtlebot_network_setup.sh $IP
