"""import smtplib
import email.utils
#from smtplib import SMTP

massge = "this is just letter from python"

import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
except:
    print ("Something went wrong...")
mail.starttls()

mail.login('boooooo.2018@gmail.com','adgjmpw12345')

mail.sendmail ('boooooo.2018@gmail.com','mohammad.sawas2016@gmail.com',massge)

import smtplib
#import email.utils

gmail_user = "boooooo.2018@gmail.com"
gmail_password = "adgjmpw12345"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print ("Something went wrong...")"""

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("boooooo.2018@gmail.com", "adgjmpw12345")

msg = "this is just my first python massge !"
server.sendmail("boooooo.2018@gmail.com", "mohammad.sawas2016@gmail.com", msg)
server.quit()