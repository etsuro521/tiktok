from PIL import Image, ImageDraw
import numpy as np

def make_circle(im,im_2r):
    mask = Image.new("L", im.size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,im_2r-100,im_2r-100),fill=255)
    im_rgba = im.copy()

    mask_r_size = im_2r+200
    mask_r = Image.new(im.mode, (mask_r_size,mask_r_size),0)
    draw = ImageDraw.Draw(mask_r)
    draw.ellipse((0,0,mask_r_size,mask_r_size),(51,51,51))
    start_x = int((mask_r_size - im.size[0]+100)/2)
    start_y = int((mask_r_size - im.size[1]+100)/2)
    mask_r.paste(im_rgba,(start_x,start_y),mask)
    return mask_r

def paste_to_back(pasted_im):
    back_im = Image.new(pasted_im.mode,(900,1600),(0,0,0))
    b_x,b_y = back_im.size
    start_x = int((b_x - pasted_im.size[0])/2)
    start_y = int((b_y - pasted_im.size[1])/4)
    back_im.paste(pasted_im,(start_x,start_y))
    return back_im

def main():
    im_name = "IMG_4008"
    im = Image.open("../img/"+im_name+".jpg")
    im_x,im_y= im.size

    if im_x > im_y:
        im_2r = im_y
    else:
        im_2r = im_x
    im_list = []
    s_im = make_circle(im,im_2r)

    for i in range(0,360,1):
        k_im = s_im.rotate(i)
        p_im = paste_to_back(k_im)
        im_list.append(p_im)
        

    im_list[0].save("../img/g_im.gif", save_all=True, append_images=im_list[1:],optimize=True, duration=100, loop=0) 

if __name__ == "__main__":
    main()
 