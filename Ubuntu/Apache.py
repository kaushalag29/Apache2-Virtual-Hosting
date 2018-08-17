#!/usr/bin/env python
import os
from os.path import expanduser
home=expanduser("~")
os.chdir(home)
os.system("cd ..")
os.system("cd ..")
#print os.getcwd()
print "Enter domain.com that you want to host"
site=raw_input()
os.system("sudo mkdir -p /var/www/"+site+"/public_html")
os.system("sudo chown -R $USER:$USER /var/www/"+site+"/public_html")
os.system("sudo chmod -R 755 /var/www")
os.system("sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/"+site+".conf")
x="<"+"VirtualHost *:80"+">"+"\n"
x=x+"ServerAdmin admin@"+site+"\n"
x=x+"ServerName "+site+"\n"
x=x+"ServerAlias www."+site+"\n"
x=x+"DocumentRoot /var/www/"+site+"/public_html"+"\n"
x=x+"ErrorLog ${APACHE_LOG_DIR}/error.log"+"\n"
x=x+"CustomLog ${APACHE_LOG_DIR}/access.log combined"+"\n"
x=x+"<"+"/VirtualHost>"
file = open('/etc/apache2/sites-available/'+site+'.conf', 'w+')
file.write(x)
file.close()
os.system("sudo a2ensite "+site+".conf")
os.system("sudo service apache2 restart")
os.system("systemctl reload apache2")
print "Done"
