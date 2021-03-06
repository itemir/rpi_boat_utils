# Traffic Counter for Mikrotik and OpenWrt Routers

<img src='https://raw.githubusercontent.com/itemir/rpi_boat_utils/master/traffic_counter/screenshot.png' align='left' width='500' hspace='10' vspace='10'>
This is a working, somewhat hacky and not a particularly well documented repository for monitoring traffic usage on Mikrotik and OpenWrt Routers. The same logic can be applied to almost any system. It is meant to monitor usage/quota on LTE or other interfaces. It consists of several components:

1. Code in this repository that is running on some local or remote server on the same network that Mikrotik can reach (note that there is no authentication, so local network is much more secure). This code doesn't do anything apart from storing the data on a local InfluxDB database. Assumption is that you will use a visualization tool like Grafana on this database. Screenshots are provided from such configuration.
2. A script for Mikrotik or OpenWrt routers that is also included in this repository. It will almost certainly require tweaking to your individual environment. This specific script is for Mikrotik LtAP with dual LTE modems (lte1 and lte2). For Mikrotik, you need to add a configuration like the following for this to run:
```
/ip firewall mangle
  add chain=forward out-interface=lte1 comment=lte1-tx
  add chain=forward in-interface=lte1 comment=lte1-rx
  add chain=forward out-interface=lte2 comment=lte2-tx
  add chain=forward in-interface=lte2 comment=lte2-rx
```

or if you want to do this for a wlan interface
```
/ip firewall mangle
  add chain=forward out-interface=wlan1 comment=wlan-tx
  add chain=forward in-interface=wlan1 comment=wlan-rx
```

On OpenWrt, you do not need any specific configuration.

3. A scheduler that you need to configure on Mikrotik router to run this script every hour. On OpenWrt this will be a cron entry.

This method was influenced by [Mohamed Muhannad's Traffic Counter](https://github.com/muhannad0/mikrotik-traffic-counter), make sure to check his repo for more detailed explanation of Mikrotik configurations.
