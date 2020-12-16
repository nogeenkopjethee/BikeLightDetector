from Adafruit_IO import Client, Feed, Data
import settings
import private_settings
import RPi.GPIO as GPIO

# Goal of this script: read the two feeds of Adafruit IO. If the motion sensor detects motion, but the light sensor does not detect light, send a warning to the dashboard and the lights.

aio = Client(private_settings.ADAFRUIT_IO_USERNAME, private_settings.ADAFRUIT_IO_KEY)

# GPIO Setup
GPIO.setmode(GPIO.BCM) # Use BCM board layout. Hint: use https://pinout.xyz
GPIO.setmode(settings.GREEN_LIGHT_PIN, GPIO.out) 
GPIO.setmode(settings.RED_LIGHT_PIN, GPIO.out) 

