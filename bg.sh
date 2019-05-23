#!/bin/bash

#Set variables
USER=target_victim
FILE=bg.jpg
FILE_PATH=/home/$USER/$FILE
URL=http://url.to/image.png

#Download picture to user's home directory
wget $URL -O $FILE

#We need some variables to be exported so cron can change the wallpaper
PID=$(pgrep -u $USER gnome-session)

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

sleep 5

#Now change the wallpaper image
gsettings set org.gnome.desktop.background picture-uri file://$FILE_PATH
