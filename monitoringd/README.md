monitoringd
===

<img src='https://raw.githubusercontent.com/itemir/rpi_boat_utils/master/monitoringd/screenshot.png' align='left' width='450' hspace='10' vspace='10'>
This is a simple Python code to read pressure, temperature and humidity readings from a [USB-PA](http://dogratian.com/products/index.php/menu-sensors/menu-usb-pa-type-a-bmp085) sensor (based on BME280) and store them in InfluxDB, a time series database.

Stored data can be visualized by tools like [Grafana](https://grafana.com/) as shown in the screenshot.

It is an easy means of monitoring the weather conditions at or remotely.
