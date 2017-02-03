AISplay
===

<img src='https://raw.githubusercontent.com/itemir/aisplay/master/screenshot.png' align='left' width='450' hspace='10' vspace='10'>
AISplay is a Python example for visualizing [Automatic Identification System](https://en.wikipedia.org/wiki/Automatic_identification_system)
(AIS) messages for marine traffic. It uses [libais](https://github.com/schwehr/libais) to decode AIS and
[NMEA](https://en.wikipedia.org/wiki/NMEA_0183) messages and visualizes traffic on Google Maps. 

Hardware
---

AISplay requires an AIS receiver and a compatible antenna. It accesses data over the network but any kind of AIS can easily be made to work. AIS receivers come in different form factors and price points. If you don't have an AIS receiver and interested in obtaining a simple one, there is an [open source AIS kit](https://github.com/astuder/dAISy) which is also sold as a kit on Tindie.

If you have an AIS device that is not connected to the network, you can easily make it network aware. Check out my post on this [Tutorial: Build Your Own Cheap Wireless AIS Receiver](https://www.partmarine.com/blog/wireless_ais_howto/).

Installation
---

Clone the repository, 'git clone https://github.com/itemir/aisplay'.

Install libais, 'pip install libais'.

Run AISplay with default options, './aisplay.py' or check options with './aisplay.py -h'.

You can specify AIS server address with '--address' and '--port' CLI options.

Access visualization on 'http://localhost:8888' (assuming default port number).

Contributing
---

AISplay was written in a short period as a fun mini-project while playing with an AIS
receiver. I do not intend to spend much more time on it. Feel free to play, fork, submit
pull requests. 

