from Adafruit_IO import Client, Feed, Data
import settings
import private_settings
import RPi.GPIO as GPIO
# import asyncio
import time


# Goal of this script: read the two feeds of Adafruit IO. If the motion sensor detects motion, but the light sensor does not detect light, send a warning to the dashboard and the lights.

aio = Client(private_settings.ADAFRUIT_IO_USERNAME, private_settings.ADAFRUIT_IO_KEY)

# GPIO Setup
GPIO.setmode(GPIO.BCM) # Use BCM board layout. Hint: use https://pinout.xyz
GPIO.setup(settings.GREEN_LIGHT_PIN, GPIO.OUT) 
GPIO.setup(settings.RED_LIGHT_PIN, GPIO.OUT) 

light_sensor_feed = aio.feeds("bike-light-detector.light-sensor")
motion_sensor_feed = aio.feeds("bike-light-detector.motion-sensor")
warning_feed = aio.feeds("bike-light-detector.warning-feed")
sensor_state_feed = aio.feeds("bike-light-detector.sensor-states")


# Using a while-loop, this function reads the status of the motion sensor every second.
# If the motion sensor detects anything (1), the script will read out the light sensor.
# If the light sensor detects a light, everything is fine (green)
# If the light sensor does not detect a light: WARNING (red)
# If the motion sensor does not detect any motion: No bike detected (no lights)
def readFeed():
    aio.send_data(warning_feed.key, "Mogelijk druk kruispunt.")
    while True:
        motion_sensor_data = aio.receive(motion_sensor_feed.key)
        motion_sensor_value = int(motion_sensor_data.value)

        if motion_sensor_value == 1:
            light_sensor_data = aio.receive(light_sensor_feed.key)
            light_sensor_value = int(light_sensor_data.value)
            if light_sensor_value == 0:
                print("WARNING: Bike without light")
                print ("This warning will be shown for 20 seconds!")
                aio.send_data(sensor_state_feed.key, 2)
                aio.send_data(warning_feed.key, "WAARSCHUWING: Fiets zonder licht!")
                GPIO.output(settings.GREEN_LIGHT_PIN, GPIO.LOW)
                GPIO.output(settings.RED_LIGHT_PIN, GPIO.HIGH)
                time.sleep(20)
                aio.send_data(warning_feed.key, "Mogelijk druk kruispunt.")
            elif light_sensor_value == 1:
                aio.send_data(sensor_state_feed.key, 3)
                print("Bike with a light")
                GPIO.output(settings.RED_LIGHT_PIN, GPIO.LOW)
                GPIO.output(settings.GREEN_LIGHT_PIN, GPIO.HIGH)
        else:
            print("No bike detected")
            aio.send_data(sensor_state_feed.key, 1)
            GPIO.output(settings.GREEN_LIGHT_PIN, GPIO.LOW)
            GPIO.output(settings.RED_LIGHT_PIN, GPIO.LOW)
            time.sleep(2)

readFeed()
