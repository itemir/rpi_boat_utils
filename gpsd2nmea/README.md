gpsd2nmea - A daemon for making gpsd messages available for NMEA receivers
---

[gpsd](http://www.catb.org/gpsd/) is a service daemon that monitors one or more GPSes or AIS receivers attached to a host computer through serial or USB ports, making them available to be queried on TCP port 2947 of the host computer. It is very handy to link GPS or AIS receivers but not all clients support it directly. For example OpenCPN does support it but iNavX and iSailor don't. They do require raw NMEA sentences over wifi/network.

gpsd2nmea bridges that gap. It can connect to a gpsd server and translate the messages to raw NMEA to sentences, so clients that do not support gpsd can connect.

Usage:
```
./gpsd2nmea --gpsd-server 192.168.100.1 & 
```

With above example multiple end points can access the data over port 2948. You can specify port numbers as well, see the help.

```
$ ./gpsd2nmea --gpsd-server 192.168.100.1 &
[2] 22704
$ telnet localhost 2948
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
!AIVDM,1,1,,B,15MoQF0P01o@1f0EUu=qMwvn2D2:,0*48
!AIVDO,1,1,,,B52`qV000=kt:VUHn;KQ3wf5oP06,0*65
!AIVDM,1,1,,B,33P>JdQ0@0o@006EUTn=V:JP0Dg:,0*25
!AIVDM,1,1,,B,15NLR3PP00o@5Q<Ebj=U8Ovp2@@Q,0*02
!AIVDM,1,1,,A,15N6Ll0P00o@5gPEbhh>4?vp28Fc,0*0C
!AIVDM,1,1,,B,35Mv4LP025o?hiHE`OwGTn>r00Q@,0*23
!AIVDO,1,1,,,B52`qV000=kt:VUHn;KQ3wfUoP06,0*05
!AIVDM,1,1,,B,15Mv2aPP00o?iJfEWG6UPwvr2<24,0*41
!AIVDM,1,1,,B,15NBTh0000G@6P<Ea5BG1I:p0@A6,0*6D
!AIVDM,3,1,0,B,803Ovk@0E050b6qlilmjkj0r4TBe@0V4a@WbB;P3wP10b0qliljqhiw2RTDq,0*2D
!AIVDM,3,2,0,B,p2<<d@wwisP3wP10b0qlilomhj0@bTDaN0P4rtwwj7P3wP10b0qlilpnkiwQ,0*70
!AIVDM,3,3,0,B,04EjqQR72Owwj3P3wP10b6qlimillj2:RTFg42r<t>000:10,0*72
^]
telnet> close
Connection closed.
$
```

