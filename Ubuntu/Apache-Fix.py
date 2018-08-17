#!/usr/bin/env python
import os
from os.path import expanduser
home=expanduser("~")
os.chdir(home)
os.system("cd ..")
os.system("cd ..")
os.chdir("/var/www")
print "Enter domain.com that you want to remove"
site=raw_input()
os.system("sudo rm -r "+site)
os.chdir(home)
os.system("cd ..")
os.system("cd ..")
os.system("sudo service apache2 stop")
os.chdir("/etc/apache2/sites-available")
os.system("sudo rm -r "+site+".conf")
os.chdir(home)
os.system("cd ..")
os.system("cd ..")
os.chdir("/etc/apache2/sites-enabled")
os.system("sudo rm -r "+site+".conf")
print "Done"
