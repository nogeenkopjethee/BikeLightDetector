#!/bin/bash

# mkdir -p /home/pi/.config/systemd/user

if [ "$(id -u)" != "0" ]; then
	echo "Sorry, you are not root."
	exit 1
fi

cp systemd_scripts/* /etc/systemd/system/

systemctl daemon-reload

systemctl enable sensor_to_feed.service
systemctl enable track_feed.service
