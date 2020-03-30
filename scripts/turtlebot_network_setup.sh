IP=$(ifconfig | grep -o -E '192.[^ ]+' | head -n 1)
# First argument ($1) is the remote PC  
echo "export ROS_MASTER_URI=http://$1:11311" >> ~/.bashrc
echo "export ROS_HOSTNAME=$IP" >> ~/.bashrc
source ~/.bashrc
