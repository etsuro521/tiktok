from PIL import Image, ImageDraw
import shutil
import glob
import os

files = glob.glob("../img/*")
ims = [Image.open(file) for file in files]
if (ims[0].size[0]+ims[0].size[1]) > (ims[1].size[0]+ims[1].size[1]):
    ims =  {"album":ims[1],"play":ims[0]}
else:
    ims = {"album":ims[0],"play":ims[1]}

al = ims["album"]
pl = ims["play"]

al = al.crop((0,0,al.size[0],al.size[0]))
ims["album"] = al

pl = pl.crop((0,1635,pl.size[0],2478))
ims["play"] = pl

