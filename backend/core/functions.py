import os
import base64
import string
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *
from core.image_proc import *


class genQR():
    def __init__(self, filename):
        self.qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=4,
        )
        self.filename = filename

    def __del__(self):
        os.remove(self.filename + '.png')

    def genURL(self,data):
        img = self.qr.add_data(data)
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string

    def genText(self,data):
        img = self.qr.add_data(data)
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string

    def genWifi(self,ssid,password,type):
        data = "WIFI:T:{type};S:{ssid};P:{password};;".format(type=type, ssid=ssid, password=password)
        img = self.qr.add_data(data)
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string

    def genSms(self,phonenumber):
        data = 'sms:+' + phonenumber
        img = self.qr.add_data(data)
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string

    def genEmail(self,email,subject,msg):
        data = 'mailto:'+email+'?subject='+subject+'&body='+msg
        img = self.qr.add_data(data)
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string


    def genVcard(self,data):
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
        img = self.qr.add_data(tmp.format_map(data))
        #type(img)
        img = self.qr.make_image(image_factory= StyledPilImage,
                            module_drawer=CircleModuleDrawer(),
                            color_mask=SquareGradiantColorMask(),
                            embeded_image_path="core/images/logo.png")
        img.save(self.filename + '_pregen.png')
        procImg(self.filename)
        with open(self.filename + '.png','rb') as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string



