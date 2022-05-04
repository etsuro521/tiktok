from PIL import Image, ImageDraw
import numpy as np

im_name = "IMG_4008"
im = Image.open("../img/"+im_name+".jpg")
im_x,im_y= im.size

if im_x > im_y:
    im_2r = im_y
else:
    im_2r = im_x


mask = Image.new("L", im.size,0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,im_2r,im_2r),fill=255)
im_rgba = im.copy()

mask_r_size = im_2r+250
mask_r = Image.new(im.mode, (mask_r_size,mask_r_size),0)
draw = ImageDraw.Draw(mask_r)
draw.ellipse((0,0,mask_r_size,mask_r_size),(51,51,51))
start_x = int((mask_r_size - im.size[0])/2)
start_y = int((mask_r_size - im.size[1])/2)
mask_r.paste(im_rgba,(start_x,start_y),mask)
mask_r.show()
