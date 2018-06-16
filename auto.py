from subprocess import *
call("sudo ifconfig wlan 10.10.0.10",shell=True)
call("sudo /etc/init.d/isc-dhcp-server restart",shell=True)
call("sudo hostapd /etc/hostapd/hostapd.conf",shell=True)

