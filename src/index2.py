from PIL import Image, ImageDraw

im = Image.open("../img/back.jpg").convert("RGBA")
print(im.mode)
 