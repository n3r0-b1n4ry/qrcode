import os
import base64
import string
import qrcode
import wifi_qrcode_generator as qr
from segno import helpers

import datetime

TMPPATH = 'C:/Windows/Temp'
# TMPPATH = '/var/tmp'

def genURL(url):
    img = qrcode.make(url)
    filename = '{}\{}.png'.format(TMPPATH, datetime.datetime.now().strftime("%d_%m_%Y"))
    img.save(filename)
    with open(filename,'rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename)
    return my_string.decode()

def genText(text):
    img = qrcode.make(text)
    filename = '{}\{}.png'.format(TMPPATH, datetime.datetime.now().strftime("%d_%m_%Y"))
    img.save(filename)
    with open(filename,'rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename)
    return my_string.decode()

def genWifi(ssid,password,type):
    img = qr.wifi_qrcode(ssid, False, type, password)
    filename = '{}\{}.png'.format(TMPPATH, datetime.datetime.now().strftime("%d_%m_%Y"))
    img.save(filename)
    with open(filename,'rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename)
    return my_string.decode()

def genSms(phonenumber):
    data = 'sms:+' + phonenumber
    img = qrcode.make(data)
    filename = '{}\{}.png'.format(TMPPATH, datetime.datetime.now().strftime("%d_%m_%Y"))
    img.save(filename)
    with open(filename,'rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename)
    return my_string.decode()

def genEmail(email,subject,msg):
    data = 'mailto:'+email+'?subject='+subject+'&body='+msg
    img = qrcode.make(data)
    filename = '{}\{}.png'.format(TMPPATH, datetime.datetime.now().strftime("%d_%m_%Y"))
    img.save(filename)
    with open(filename,'rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename)
    return my_string.decode()