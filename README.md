# Boat and Raspberry Pi Utilities

This repository contains a collection of utilities and tools for Raspberry Pi. They are primarily for usage on a boat, for integrating marine electronics, sensors and marine protocols.

That being said, some of the utilities are relevant for non-boat usage (like uart_control) and some of the utilities do not require to be run on a Raspberry Pi (like gpsd2nmea, aisd or aisplay). 

[uart_control](https://github.com/itemir/rpi_boat_utils/tree/master/uart_control)
---
Tool for configuring the UART on a Raspberry Pi.

[gpsd2nmea](https://github.com/itemir/rpi_boat_utils/tree/master/gpsd2nmea)
---
Daemon for translating gpsd messages to raw NMEA messages to be used in iNavX, iSailor etc.

[monitoringd](https://github.com/itemir/rpi_boat_utils/tree/master/monitoringd)
---
Daemon for retrieving pressure, temperature and humidity from a BME280 based sensor and storing them in InfluxDB, for visualizing on a Grafana dashboard.

[aisplay](https://github.com/itemir/rpi_boat_utils/tree/master/aisplay)
---
Web Service for displaying AIS vessels on a map.

[sensord](https://github.com/itemir/rpi_boat_utils/tree/master/sensord)
---
Signal K Daemon for integrating a variety of different DIY Raspberry Pi sensors to a Signal K network.

[aisd](https://github.com/itemir/rpi_boat_utils/tree/master/aisd) (Obsolete)
---
Daemon for making a serial or USB based AIS (Automatic Identification System) receiver wireless enabled.


