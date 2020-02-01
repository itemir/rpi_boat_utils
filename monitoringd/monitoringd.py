#!/usr/bin/python

import serial
import datetime
import pytz 
import time
from influxdb import InfluxDBClient

def get_value(sensor, command):
    sensor.write(b'%s\n' % command)
    return float(sensor.readline().strip())

host = 'localhost'
port = 8086 
user = 'username'
password = 'password'
sensor_device = '/dev/ttyACMX'
location = 'BoatName'
dbname = 'sensor_data'
interval = 60
measurement = 'measurement'

try:
    from local_settings import *
except ImportError:
    pass

try:
    while True:
        sensor = serial.Serial(sensor_device, timeout=1)
        pressure = get_value(sensor, 'GP')
        temperature = get_value(sensor, 'GT') 
        humidity = get_value(sensor, 'GH')
        sensor.close()
        iso = datetime.datetime.now(pytz.timezone('US/Pacific')).isoformat()

        data = [
        {
          "measurement": measurement,
              "tags": {
                  "location": location,
              },
              "time": iso,
              "fields": {
                  "pressure" : pressure,
                  "temperature" : temperature,
                  "humidity": humidity
              }
          }
        ]
        client = InfluxDBClient(host, port, user, password, dbname)
        client.write_points(data)
        client.close()
        time.sleep(interval)
 
except KeyboardInterrupt:
    pass

