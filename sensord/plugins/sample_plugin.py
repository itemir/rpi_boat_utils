from base_plugin import BasePlugin
import time

class TestPlugin(BasePlugin):
    name = 'Test Plugin'
    enabled = False
    def main(self):
        while True: 
            self.boat_sensord.emit({'path': 'some.path',
                                    'vaue': 'some value'})
            # Emit every X seconds
            time.sleep(15)

plugin = TestPlugin
