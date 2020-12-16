# import RPi.GPIO as GPIO
from Adafruit_IO import Client, Feed, Data
import private_settings
import time

aio = Client(private_settings.ADAFRUIT_IO_USERNAME, private_settings.ADAFRUIT_IO_KEY)

light_sensor_feed = aio.feeds("bike-light-detector.light-sensor")


while True:
    aio.send_data(light_sensor_feed.key, 0.5)
    time.sleep(4)
    aio.send_data(light_sensor_feed.key, 0.2)



