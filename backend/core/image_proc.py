from PIL import Image
import os

TMPPATH = '/var/tmp'

def removeQrcodeBG(filename):
	img = Image.open(filename + "_pregen.png")
	img = img.convert("RGBA")
  
	datas = img.getdata()
  
	newData = []
  
	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)
  
	img.putdata(newData)
	img.save(filename + "_rm_bg.png", "PNG")

def convertBackground(filename):
	im1 = Image.open(filename + '_pregen.png')
	width, height = im1.size

	im_rgb = Image.open('core/images/background.jpg')
	im_rgb = im_rgb.resize((width-160, height-160))
	im_rgba = im_rgb.copy()
	im_rgba.putalpha(128)
	im_rgba.save(filename + '_bg_transperent.png')

def mergeLayer(filename):
	im2 = Image.open(filename + "_rm_bg.png")
	im1 = Image.open(filename + '_bg_transperent.png')

	im1.paste(im2, (-80, -80), im2)
	im1.save(filename + '.png', quality=95)
	



def procImg(filename):
	removeQrcodeBG(filename)
	convertBackground(filename)
	mergeLayer(filename)
	os.remove(filename + "_rm_bg.png")
	os.remove(filename + '_bg_transperent.png')
	os.remove(filename + "_pregen.png")
	print('Successfully proccess images')