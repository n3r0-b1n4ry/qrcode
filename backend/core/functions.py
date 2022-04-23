import os
import base64
import string
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *
from core.image_proc import *

import datetime

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)

def genURL(data):
    img = qr.make(data)
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string

def genText(data):
    img = qr.make(data)
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string

def genWifi(ssid,password,type):
    data = "WIFI:T:{type};S:{ssid};P:{password};;".format(type=type, ssid=ssid, password=password)
    img = qr.add_data(data)
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string

def genSms(phonenumber):
    data = 'sms:+' + phonenumber
    img = qr.add_data(data)
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string

def genEmail(email,subject,msg):
    data = 'mailto:'+email+'?subject='+subject+'&body='+msg
    img = qr.add_data(data)
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string


def genVcard(data):
    tmp = """BEGIN:VCARD
VERSION:3.0
N:{firstname};{lastname}
FN:{fullname}
ORG:{organize}
TITLE:
ADR;TYPE=intl,work,postal,parcel:;;{addr};{city};;{taxcode};{country}
TEL;WORK;VOICE:
TEL;CELL:{phonenumber}
TEL;FAX:
EMAIL:{email}
URL:{website}
END:VCARD"""
    # data = tmp.format(firstname = pfirstname ,lastname = plastname,fullname = pfullname,organize = porganize,
    #     addr = paddr,city = pcity,taxcode = ptaxcode,country = pcountry,phonenumber = pphonenumber,email = pemail)
    img = qr.add_data(tmp.format_map(data))
    #type(img)
    img = qr.make_image(image_factory= StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=SquareGradiantColorMask(),embeded_image_path="core/images/logo.png")
    filename = os.path.join(TMPPATH, '{}'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))
    img.save(filename + '_pregen.png')
    # img.save(filename + '.png')
    procImg(filename)
    with open(filename + '.png','rb') as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove(filename + '.png')
    return my_string



