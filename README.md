# Raspberry Pi Utilities

Utilities for Raspberry Pi

uart_control
---
Allows auto configuration of UART. UART is normally used by the console on Raspberry Pi 0, 1 and 2. On Raspberry Pi 3, UART is used by the Bluetooth module and console is assigned to a software based UART known as mini UART. Many custom boards require access to UART via GPIO pins 14 and 15. This requires a set of configuration changes that differ per platform. This command line utility allows making UART available to custom applications.

```
$ sudo ./uart_control
Usage:
  ./uart_control [ OPTION ]
      default Restores original state
      gpio    Makes UART available on GPIO pins 14 & 15
      status  Displays current status
$
```

You can see the status of UART with the status option:
```
$ sudo ./uart_control status
Console  : disabled
UART     : enabled
Bluetooth : enabled

UART is available to GPIO 14 & 15.
$
```

gpio option makes the UART available to GPIO pins 14 and 15:

```
$ sudo ./uart_control gpio
Enabling UART.
Disabling console on UART.
Disabling Bluetooth.
Removed symlink /etc/systemd/system/multi-user.target.wants/hciuart.service.

UART made available on GPIO 14 & 15.
You now need to reboot
$
```
default option changes the state back to its original:
```
$ sudo ./uart_control default
Enabling UART.
Enabling console on UART.
Enabling Bluetooth.
Created symlink from /etc/systemd/system/multi-user.target.wants/hciuart.service to /lib/systemd/system/hciuart.service.

Default system settings restored.
You now need to reboot.
$
```
