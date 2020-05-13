#!/bin/sh

#checking for an internet connection
wget -q --spider https://google.com

echo "CONNECTION TEST EXIT STATUS - $?"

if [ $? -eq 0]; then

  echo "INSTALLING..."
  sleep 3

  sudo apt-get update
  sudo apt-get install python3-pip
  sudo apt-get -y install build-essential libssl-dev python3-dev libffi-dev
  sudo pip3 install -r modules.txt
  sudo apt-get install portaudio19-dev python-pyaudio
  sudo apt-get install python3-pyaudio
  sudo apt install mpg321
  pip3 install PyAudio
  pip3 install sounddevice
  pip3 install soundfile

else
  echo "Device is OFFLINE"
  echo "Connect to Internet and try again later"
fi



