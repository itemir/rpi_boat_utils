class BasePlugin(object):
    enabled = False
    def __init__(self, boat_sensord):
        self.boat_sensord = boat_sensord
        self.running = False
        self.init()

    def init(self):
        pass

    def start(self):
        self.running = True
        self.main()

    def stop(self):
        self.running = False

    def main(self):
        pass
