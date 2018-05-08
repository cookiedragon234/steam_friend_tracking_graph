sudo apt-get install screen -y
sudo apt-get install python -y
echo
echo "How often should the python script run? (In seconds)"
read time
echo
screen -S steamgraph -dm watch -n $time python get.py
echo "Running script with a delay of $time seconds"
echo
echo "If you need to cancel the script running, just run this:"
echo "screen -X -S steamgraph quit"
