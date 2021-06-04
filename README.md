# PiMessagePostLCD

## A python program that takes a message sent to the Raspberry Pi using HTTP POST request and displays it on the Adafruit Pi LCD Plate

#### Requirements

python3
apache2 (sudo a2dismod mpm_event && sudo a2enmod mpm_prefork cgi)
/etc/apache2/sites-enabled/000-default.conf
	<Directory /var/www/marquee>
		Options +ExecCgi
		DirectoryIndex index.py
	</Directory>
	AddHandler cgi-script .py
	
	DocumentRoot /var/www/marquee

place index.py in /var/www/marquee
chmod 755 /var/www/marquee/index.py

