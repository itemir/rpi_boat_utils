from base_plugin import BasePlugin
import time
import serial

DEVICE = '/dev/ttyACM1'
COUNTER = 5

class TestPlugin(BasePlugin):
    name = 'Plugin for USB-PA (http://dogratian.com/products/index.php/menu-sensors/menu-usb-pa-type-a-bmp085)'
    enabled = True

    def init(self):
        self.serial = serial.Serial(DEVICE)

    def get_value(self, command):
        self.serial.write(b'%s\n' % command)
        return float(self.serial.readline().strip())

    def main(self):
        while True: 
            pressure = self.get_value('GP')
            temperature = self.get_value('GT') + 273.15
            humidity = self.get_value('GH')

            self.boat_sensord.emit([
              {
                'path': 'environment.inside.temperature',
                'value': temperature
              },
              {
                'path': 'environment.outside.pressure',
                'value': pressure
              },
              {
                'path': 'environment.outside.humidity',
                'value': humidity
              },
            ])

            # Emit every X seconds
            time.sleep(COUNTER)

plugin = TestPlugin
