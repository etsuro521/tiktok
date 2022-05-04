from PIL import Image






im_name = "IMG_4008"
im = Image.open("../img/"+im_name+".jpg").convert('RGBA')

im_list = []
for i in range(0,360,1):
    k_im = im.rotate(i)
    im_list.append(k_im)

im_list[0].save("../img/g_im.gif", save_all=True, append_images=im_list[1:],optimize=True, duration=100, loop=0) 

