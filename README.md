# PiMessagePostLCD

## A python program that takes a message sent to the Raspberry Pi using HTTP POST request and displays it on the Adafruit Pi LCD Plate

#### Required packages

The plan right now is to use apache module mod_wsgi to allow Python to host a wsgi server.  Compiled from source to use the default python v2.7 rather than the 2.6 that the Raspbian package wants to install.

Location: https://code.google.com/p/modwsgi/wiki/QuickInstallationGuide
./configure --with-python=/usr/bin/python

to compile locally, we need apache2-prefork-dev and apache2-threaded-dev (which provide the apache apxs library)

... more details to come as I figure out exactly how this is going to work...
