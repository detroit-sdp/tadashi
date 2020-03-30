IP=$(ifconfig | grep -o -E '192.[^ ]+' | head -n 1)
echo "export ROS_MASTER_URI=http://$IP:11311" >> ~/.bashrc
echo "export ROS_HOSTNAME=$1" >> ~/.bashrc
