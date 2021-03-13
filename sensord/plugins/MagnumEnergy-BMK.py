import time
from magnum import magnum
from base_plugin import BasePlugin

DEVICE = '/dev/ttyUSB0'
SIGNALK_KEY = 'houseBattery'
SLEEP = 5

class MagnumPlugin(BasePlugin):
    name = 'Plugin for Magnum Energy Batter Monitor Kit (ME-BMK)'
    enabled = True

    def init(self):
        self.reader = magnum.Magnum(DEVICE)

    def main(self):
        while True: 
            devices = self.reader.getDevices()
            for device in devices:
                if device['device'] == 'BMK':
                    soc = float(device['data']['soc'])/100
                    vdc = device['data']['vdc']
                    self.boat_sensord.emit([
                    {
                        'path': 'electrical.batteries.%s.capacity.stateOfCharge' % SIGNALK_KEY,
                        'value': soc
                    },
                    {
                        'path': 'electrical.batteries.%s.voltage' % SIGNALK_KEY,
                        'value': vdc
                    }
                    ])

            # Emit every X seconds
            time.sleep(SLEEP)

plugin = MagnumPlugin
