#!/usr/bin/python3
#
# Copyright (c) 2017-2021 Ilker Temir
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import importlib
import json
import os
import socket
import sys
import threading
import time

PORT = 1920
client_list = []

class BoatSensor(object):
    '''
    Main class
    '''
    def __init__(self):
        '''
        All plugins under ./plugins directory will be automatically loaded and
        initialized.
        '''
        self.lock = threading.Lock()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        for root, dirs, files in os.walk(os.path.join(base_dir, 'plugins')):       
            for file in files:
                if file.endswith(".py") and file != '__init__.py':
                    plugin_file = 'plugins.' + file.replace('.py', '')
                    plugin = importlib.import_module(plugin_file).plugin(self)
                    if plugin.enabled:
                        # Each plugin is run on its own thread
                        thread = threading.Thread(target=plugin.start)
                        thread.daemon = True
                        thread.start()

    def emit(self, values):
        '''
        Called by individual plugins to emit messages
        '''
        data = '{"updates":[{"$source":"sensord","values":%s}]}' % json.dumps(values)
        self.sock.sendto(data.encode('utf-8'), ('127.0.0.1', PORT))

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                time.sleep(0.5)
            except KeyboardInterrupt:
                sys.exit()

if __name__ == '__main__':
    sensord = BoatSensor()
    sensord.run()

