#!/usr/bin/python
#
# Copyright (c) 2017 Ilker Temir
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

import argparse
import BaseHTTPServer
import re
import datetime
import pytz
from influxdb import InfluxDBClient

host = 'localhost'
port = 8086
user = 'username'
password = 'password'
dbname = 'sensor_data'

try:
    from local_settings import *
except ImportError:
    pass

class http_handler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    This is just a simple web server 
    '''
    def do_GET(s):
        ''' Respond to GET only '''
        if cli_options.verbose:
            print "Received HTTP request (%s)" % s.path
        match = re.match(r'^/\?lte1-rx=(\d+)&lte1-tx=(\d+)&lte2-rx=(\d+)&lte2-tx=(\d+)$', s.path)
        if match:
            lte1_rx=int(match.group(1))
            lte1_tx=int(match.group(2))
            lte2_rx=int(match.group(3))
            lte2_tx=int(match.group(4))
            if cli_options.verbose:
                print "Submitting %d, %d, %d, %d" % (lte1_rx, lte1_tx, lte2_rx, lte2_tx)

            iso = datetime.datetime.now(pytz.timezone('US/Pacific')).isoformat()
            data = [
            {
              "measurement": "internet_traffic",
                  "time": iso,
                  "fields": {
                      "lte1_rx" : lte1_rx,
                      "lte1_tx" : lte1_tx,
                      "lte2_rx" : lte2_rx,
                      "lte2_tx" : lte2_tx,
                  }
              }
            ]
            client = InfluxDBClient(host, port, user, password, dbname)
            client.write_points(data)
            client.close()

            s.send_response(200)
            s.send_header('Content-type', 'text/html')
            s.end_headers()
        else:
            s.send_response(404)
            s.send_header('Content-type', 'text/html')
            s.end_headers()
            s.wfile.write('<h1>HTTP-404</h1>')
    def log_message(self, format, *args):
        ''' Silence stdout messages '''
        return

parser = argparse.ArgumentParser()
parser.add_argument('--http-port',
                    dest='http_port',
                    type=int,
                    default=8888,
                    help='Port number on for the HTTP server'+
                         ' (default: 8888)')
parser.add_argument('-v',
                    '--verbose',
                    dest='verbose',
                    action='store_true',
                    help='Enable debug messages')
cli_options = parser.parse_args()

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', cli_options.http_port),
                                  http_handler)
while True:
    httpd.handle_request()
