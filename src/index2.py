from PIL import Image, ImageDraw
import numpy as np

im_name = "IMG_4008"
im = Image.open("../img/"+im_name+".jpg")
im_x,im_y= im.size
if im_x > im_y:
    im_2r = im_y
else:
    im_2r = im_x

im_a = Image.new(im.mode, im.size,0)
mask = Image.new("L", im.size,0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,im_2r,im_2r),fill=255)

im_rgba = im.copy()
im_a.paste(im_rgba,(0,0),mask)

im_a.show()

