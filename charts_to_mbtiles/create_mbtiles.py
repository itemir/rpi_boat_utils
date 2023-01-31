#!/usr/local/bin/python3
from pymbtiles import MBtiles, Tile, TileCoordinate 
import os
import sys
import math
import requests
import json
import hashlib

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)

if len(sys.argv) != 2 or not sys.argv[1].endswith('.json'):
    print('You need to provide a json configuration file')
    sys.exit(1)

with open(sys.argv[1]) as config_file:
    configuration = json.load(config_file)

metadata = configuration['metadata']
boxes = configuration['boxes']
zoom_start = configuration['minimum_zoom']
zoom_end = configuration['maximum_zoom']
headers = configuration['additional_headers']
mbtiles_file = configuration['output_file']

unique_key = json.dumps([zoom_start, zoom_end, boxes]).encode('utf-8')
boxes_tiles_filename = '%s.boxes' %  hashlib.md5(unique_key).hexdigest()
print('Checking if previous box file exists:', boxes_tiles_filename)
if os.path.exists(boxes_tiles_filename):
    print('Preconfigured tiles exist, loading from %s' % boxes_tiles_filename)
    with open(boxes_tiles_filename) as boxes_tiles_file:
        tiles = json.load(boxes_tiles_file)
else:
    tiles = []
    print('Processing %s boxes' % len(boxes))
    box_counter = 0
    for item in boxes:
        box_counter = box_counter + 1
        print('Processing box', box_counter)
        top_left = item[0]
        bottom_right = item[1]
        lat_start = top_left['lat']
        lng_start = top_left['lng']
        lat_end = bottom_right['lat']
        lng_end = bottom_right['lng']
        for zoom in range(zoom_start, zoom_end+1):
            (x_start, y_start) = deg2num(lat_start, lng_start, zoom)
            (x_end, y_end) = deg2num(lat_end, lng_end, zoom)
            for x in range(x_start, x_end+1):
                for y in range(y_start, y_end+1):
                    tileset = TileCoordinate(zoom, x, y)
                    if tileset not in tiles:
                        tiles.append(tileset)
    with open(boxes_tiles_filename, 'w') as boxes_tiles_file:
        boxes_tiles_file.write(json.dumps(tiles))

if not os.path.exists(mbtiles_file):
    print('Creating new MBTiles file:', mbtiles_file)
    f = open(mbtiles_file, 'w')
    f.close()
else:
    print('Using existing MBTiles file:', mbtiles_file)

with MBtiles(mbtiles_file, mode='r+') as mbtiles: 
     mbtiles.meta = metadata
     existing_tile_list = mbtiles.list_tiles()
     total_tiles = len(tiles)
     print('%s tiles in total to be inserted' % total_tiles)
     counter = 0
     for tile in sorted(tiles, key=lambda x: x[0]):
         counter = counter + 1
         print('%s of %s' % (counter, total_tiles))

         (z, x, y) = tile
         row = 2**z - 1 - y
         if TileCoordinate(z,x,row) not in existing_tile_list:
             print('Downloading tile (%s, %s, %s)' % (z, x, y))

             url = configuration['tile_server']
             url = url.replace('{z}', str(z))
             url = url.replace('{x}', str(x))
             url = url.replace('{y}', str(y))

             try:
                 response = requests.get(url, headers=headers, timeout=5)
                 if response.status_code == 200:
                      mbtiles.write_tile(z=z, x=x, y=row, data=response.content)
                      print ('Inserted as %s, %s, %s' % (z, x, row))
                 else:
                      print ('Download error', response.status_code, response.content)
             except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
                 print ('Read timeout or connection reset')
         else:
             print('Tile (%s, %s, %s) was already downloaded' % (z, x, y))

sys.exit()

tiles = []

headers = {
#  'authority':'backend.navionics.com',
#  'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#  'accept-language':'en-US,en;q=0.9,tr;q=0.8',
#  'origin':'https://webapp.navionics.com',
  'referer':'https://webapp.navionics.com/',
#  'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
#  'sec-ch-ua-mobile':'?0',
#  'sec-ch-ua-platform':'"macOS"',
#  'sec-fetch-dest':'image',
#  'sec-fetch-mode':'cors',
#  'sec-fetch-site':'same-site',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


for zoom in range(zoom_start, zoom_end+1):
     print('Processing zoom level %d' % zoom)
     (x_start, y_start) = deg2num(lat_start, lng_start, zoom)
     (x_end, y_end) = deg2num(lat_end, lng_end, zoom)
     for x in range(x_start, x_end+1):
         for y in range(y_start, y_end+1):
             tile = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%s/%s/%s' % (zoom, y, x)
             tile = 'https://backend.navionics.com/tile/%s/%s/%s?LAYERS=config_2_60.00_0&TRANSPARENT=FALSE&UGC=TRUE&theme=0&navtoken=eyJrZXkiOiJOQVZJT05JQ1NfV0VCQVBQX1AwMSIsImtleURvbWFpbiI6IndlYmFwcC5uYXZpb25pY3MuY29tIiwicmVmZXJlciI6IndlYmFwcC5uYXZpb25pY3MuY29tIiwicmFuZG9tIjoxNjc1MDE3MDQwMDg1fQ' % (zoom, x, y)
             (lat_tmp, lng_tmp) = num2deg(x, y, zoom)
             print (tile)
             response = requests.get(tile, headers=headers)
             if response.status_code == 200:
                  row = 2**zoom - 1 - y
                  tiles.append (Tile(z=zoom, x=x, y=row, data=response.content))
                  print ('Inserted as %s, %s, %s' % (zoom, x, row))
             else:
                  print ('error!')

with MBtiles('my2.mbtiles', mode='w') as out:
    bounds = '%s,%s,%s,%s' % (lng_end,lat_end,lng_start,lat_start)
    bounds = '-180.0,-85,180,85'
    center = '%s,%s,%s' % ((lng_start+lng_end) / 2, (lat_start+lat_end)/2, int((zoom_start+zoom_end)/2))
    meta = {'name': 'ILKER', 'format': 'png', 'bounds': bounds , 'center': center, 'minzoom': zoom_start, 'maxzoom': zoom_end}
    #meta = {'name': 'ILKER', 'format': 'jpg', 'bounds': bounds}
    out.meta=meta
    out.write_tiles(tiles)
