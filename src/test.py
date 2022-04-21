from cgi import print_arguments
from tracemalloc import start
from PIL import Image, ImageDraw

im = Image.open("IMG_3967.jpg")
im2 = Image.open("IMG_4008.jpg")


mask_im = Image.new('RGB',(900,1600),0)

back_im = mask_im.copy()
i_x,i_y = im.size
b_x = mask_im.size[0]
start_x = int((b_x - i_x)/2)
back_im.paste(im,(start_x,10))
back_im.show()
print('test')
