#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer

sense = SenseHat()
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="q37KUCDGB9jjsDjxrXiitYz98dqOGqDg")
sense.clear()

try:
      while True:
           temp = sense.get_temperature()
           temp = 1.8 * round(temp, 1)+ 32
           logger.log("Temperature F",temp)

           humidity = sense.get_humidity()
           humidity = round(humidity, 1)
           logger.log("Humidity :",humidity)

