#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "Sorry, you are not root."
	exit 1
fi

systemctl disable --now sensor_to_feed.service
systemctl disable --now track_feed.service

rm -f /etc/systemd/system/sensor_to_feed.service
rm -f /etc/systemd/system/track_feed.service

systemctl daemon-reload