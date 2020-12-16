# BikeLightDetector
BikeLightDetector - a project for the Smart City school assignment

## Files

- `app/feed_test.py`: Testing for the Adafruit IO feeds.
- `app/settings.py`: Settings for the GPIO pins
- `app/private_settings.py`: Private settings, in this case the Adafruit IO authentication data. Not included for security reasons.
- `app/sensor_to_feed.py`: Script for constantly sending data from sensors to Adafruit IO feeds.
- `app/track_feed.py`: Script for tracking Adafruit IO feeds and warning the user, based on the situation.

- `systemd-scripts`: Contains two systemd services so you can run the scripts on startup.

## How to set up this script on a Raspberry Pi?

1. Install Python 3.7 and Pip.
    - On Raspiberry Pi OS Buster, this is done with: ```sudo apt update && sudo apt install python3-pip```
2. Install the dependencies for the scripts.
    - This can be done with ```pip3 install -r requirements.txt```
3. You can now run the scripts like usual from the command line.


## How to run the scripts on bootup?

*Warning: some experience with systemd and Linux is recommended for using this function.*

1. Ensure that the directory names in the two services are correct.
2. Run either the `create_script_services.sh` or the `remove_script_services.sh` service