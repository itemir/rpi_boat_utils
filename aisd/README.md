# aisd - Wireless AIS daemon 

aisd allows making a local AIS receiver (connected over serial, USB etc. available over the network).

Usage:
```
sudo ./aisd --port 2000 /dev/ttyUSB0 & 
```

With above example Multiple end points can access the AIS data over the network over port 2000.

```
$ telnet 192.168.1.2 2000
Trying 192.168.1.2...
Connected to 192.168.1.2.
Escape character is '^]'.
!AIVDM,1,1,,A,ENkb9J9Ich@@@@@@@@@@@@@@@@@;V4Bb:fND@00003vP000,2*24
!AIVDM,1,1,,B,15NJQiP04AG@26lEVOsD6kEn00S4,0*1D
!AIVDM,1,1,,A,15Mv9T0042o@7wHEVgP<4aSn0L1e,0*0D
!AIVDM,1,1,,B,35N7G;0P@cG@95VE`0gSnC5n0000,0*6F
!AIVDM,1,1,,B,15MvrUPP46G?q?<E`8cr4?wl0<1l,0*78
!AIVDM,1,1,,A,D03Ovk06AN>40Hffp00Nfp0,2*52
!AIVDM,1,1,,A,D03Ovk@6mN>40Tffp00Nfp0,2*12
```
