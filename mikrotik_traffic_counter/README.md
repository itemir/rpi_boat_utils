# Traffic Counter for Mikrotik based Routers

This is an incomplete, and not a particularly well documented repository for monitoring traffic usage on Mikrotik Routers. It is meant to monitor usage/quota on LTE interfaces. It consists of several components:

1. Code in this repository that is running on some local or remote server on the same network that Mikrotik can reach (note that there is no authentication, so local network is much more secure). This code doesn't do anything apart from storing the data on a local InfluxDB database. Assumption is that you will use a visualization tool like Grafana on this database. Screenshots are provided from such configuration.
2. A script for Mikrotik routers that is also included in this repository. It will almost certainly require tweaking to your individual environment. This specific script is for Mikrotik LtAP with dual LTE modems (lte1 and lte2). You need add a configuration like the following for this to run:
```
/ip firewall mangle
  add chain=forward out-interface=lte1 comment=lte1-tx
  add chain=forward in-interface=lte1 comment=lte1-rx
  add chain=forward out-interface=lte2 comment=lte2-tx
  add chain=forward in-interface=lte2 comment=lte2-rx
```
3. A scheduler that you need to configure on Mikrotik router to run this script every hour.

This method was influenced by [Mohamed Muhannad's Traffic Counter](https://github.com/muhannad0/mikrotik-traffic-counter), make sure to check his repo for more detailed explanation of Mikrotik configurations.
