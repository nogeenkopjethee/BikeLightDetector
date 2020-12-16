import RPi.GPIO as GPIO
from Adafruit_IO import Client, Feed, Data
import private_settings
import settings
import time

import asyncio

light_sensor_pin = settings.LIGHT_SENSOR_PIN
motion_sensor_pin = settings.MOTION_SENSOR_PIN

aio = Client(private_settings.ADAFRUIT_IO_USERNAME, private_settings.ADAFRUIT_IO_KEY)

light_sensor_feed = aio.feeds("bike-light-detector.light-sensor")
motion_sensor_feed = aio.feeds("bike-light-detector.motion-sensor")

# GPIO Setup
GPIO.setmode(GPIO.BCM) # Use BCM board layout. Hint: use https://pinout.xyz
GPIO.setup(light_sensor_pin, GPIO.IN) # Configure Light Sensor Pin to what is needed.
GPIO.setup(motion_sensor_pin, GPIO.IN) # Configure Motion Sensor Pin to what is needed.


async def sendSensorData(pin, feed):
    if GPIO.input(pin):
        aio.send_data(feed.key, 1)
    else:
        aio.send_data(feed.key, 0)

async def main():
    while True:
        await sendSensorData(motion_sensor_pin, motion_sensor_feed)
        await asyncio.sleep(1)
        await sendSensorData(light_sensor_pin, light_sensor_feed)
        await asyncio.sleep(1)

asyncio.run(main())