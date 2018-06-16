from subprocess import *
import fileinput 
call("ls",shell=True)
call("sudo su",shell=true)

#Update the Raspberry Pi and its packages

call("apt update && apt upgrade",shell=True)

#Install Apache web server

call("apt install apache2 -y",shell=True)

#Start and enable Apache on boot

call("systemctl start apache2",shell=True)
call("systemctl enable apache2",shell=True)

#We need to install  additional packages required by Owncloud Server

call("apt install -y apache2 mariadb-server libapache2-mod-php7.0 \
    php7.0-gd php7.0-json php7.0-mysql php7.0-curl \
    php7.0-intl php7.0-mcrypt php-imagick \
    php7.0-zip php7.0-xml php7.0-mbstring",shell=True)



call("cd /tmp",shell=True)

#Download Owncloud 10 package

call("wget https://download.owncloud.org/community/owncloud-10.0.3.tar.bz2",shell=True)

#Extract Owncloud and change the permission

call("tar -xvf owncloud-10.0.3.tar.bz2",shell=True)

call("chown -R www-data:www-data owncloud",shell=True)

#it will produce a new directory called owncloud. We need to move this directory to /var/www/html/ directory

call("mv owncloud /var/www/html/",shell=True)

#Exit /tmp directory.

call("cd",shell=True)

#Configure Apache Web Server

call("sudo nano /etc/apache2/sites-available/owncloud.conf",shell=True)

with open('/etc/apache2/sites-available/owncloud.conf','w+')as cloud:
	cloud.write('Alias /owncloud "/var/www/html/owncloud/\n\n'

'<Directory /var/www/html/owncloud/\n>'
 'Options +FollowSymlinks\n'
 'AllowOverride All\n'

'<IfModule mod_dav.c>\n'
 'Dav off\n'
 '</IfModule>\n'

'SetEnv HOME /var/www/html/owncloud\n'
'SetEnv HTTP_HOME /var/www/html/owncloud\n\n'

'</Directory>')
		
#Create Symbolic link

call("sudo su",,shell=True)

call("ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf",shell=True)

#Additional apache configuration

call("a2enmod headers",shell=True)
call("systemctl restart apache2",shell=True)
call("a2enmod env",shell=True)
call("a2enmod dir",shell=True)
call("a2enmod mime",shell=True)

#Create a MySQL database and user:

call("mysql -u root -p",shel=True)

#Install iw to check wifi dongle

call("sudo apt-get install iw",shell=True)

#Remove wpa supplicant

call("sudo apt-get purge wpasupplicant",shell=True)

#install dhcp server

call("sudo apt-get install isc-dhcp-server",shell=True)

#setup dhcp
call("sudo nano /etc/dhcp/dhcpd.conf",shell=True)
with open("/etc/dhcp/dhcpd.conf")as dhcpfile:
	dhcpfile.write("subnet 10.10.0.0 netmask 255.255.255.0 {\n"
"range 10.10.0.25 10.10.0.50;\n"
"option domain-name-servers 8.8.4.4;\n"
"option routers 10.10.0.1;\n"
"interface wlan0;\n"
"}")

call("sudo apt-get install hostapd",shell=True)

with open("/etc/hostapd/hostapd.conf")as hostapdfile:
	hostapdfile.write("interface=wlan0\n"
"driver=nl80211\n"
"ssid=Pi_STATION\n"
"hw_mode=g\n"
"channel=11\n"
"wpa=1\n"
"wpa_passphrase=123456789\n"
"wpa_key_mgmt=WPA-PSK\n"
"wpa_pairwise=TKIP CCMP\n"
"wpa_ptk_rekey=600\n"
"macaddr_acl=0\n")

