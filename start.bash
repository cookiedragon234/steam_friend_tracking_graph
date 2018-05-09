sudo apt-get install screen -y
sudo apt-get install python -y
echo
if [ ! -f apikey.txt ]; then
  echo "Please enter your steam API key:"
  read $apikey
  echo $apikey >> apikey.txt
fi
echo
if [ ! -f steamids.txt ]; then
  echo "Please enter the comma seperated list of steamids to track:"
  read $steamids
  echo $steamids >> steamids.txt
fi
echo
echo "How often should the python script run? (In seconds)"
echo "(Common times to multiply: 5 minutes: 300, 10 minutes: 600, 1 hour: 3600, 1 day: 86400)"
read time
echo
echo "Would you like to name the screen session? (Default is 'steamgraph')"
read scrn
if ! screen -list | grep -q "$scrn"; then
  screen -S $scrn -dm watch -n $time python get.py
else
  echo "Screen with same name already running!"
  exit 1
fi
echo
echo "Running script with a delay of $time seconds"
echo
echo "If you need to cancel the script running, just run this:"
echo "screen -X -S $scrn quit"
