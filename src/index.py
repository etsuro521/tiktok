from PIL import Image, ImageDraw
import shutil
import glob
import os

def get_files():
    files = glob.glob("../img/*")
    ims = [Image.open(file) for file in files]
    if (ims[0].size[0]+ims[0].size[1]) > (ims[1].size[0]+ims[1].size[1]):
        ims =  {"album":ims[1],"play":ims[0]}
    else:
        ims = {"album":ims[0],"play":ims[1]}

    al,pl = ims["album"], ims["play"]

    al = al.crop((0,0,al.size[0],al.size[0]))
    ims["album"] = al.convert("RGB")

    pl = pl.crop((0,1635,pl.size[0],2478))
    ims["play"] = pl.convert("RGB")

    return ims

def arces(draw,size,diameter):
    for i in range(50,70):
        diameter -= i
        start_point = int((size - diameter)/2)
        draw.arc((start_point, start_point, start_point+diameter, start_point+diameter), start=335, end=25, fill=(153, 153, 153))
        draw.arc((start_point, start_point, start_point+diameter, start_point+diameter), start=155, end=205, fill=(153, 153, 153))

def make_circle(im,im_2r):
    mask = Image.new("L", im.size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,im_2r-150,im_2r-150),fill=255)
    im_rgba = im.copy()

    mask_r_size = im_2r+200
    mask_r = Image.new(im.mode, (mask_r_size,mask_r_size),0)
    draw = ImageDraw.Draw(mask_r)
    draw.ellipse((0,0,mask_r_size,mask_r_size),(51,51,51))

    arces(draw,mask_r_size,mask_r_size)

    start_x = int((mask_r_size - im.size[0]+150)/2)
    start_y = int((mask_r_size - im.size[1]+150)/2)
    mask_r.paste(im_rgba,(start_x,start_y),mask)

    return mask_r

def make_play_im(im,size):
    im2 = im.resize((size, int(size*0.66)))
    w,h=im2.size
    for x in range(w):
        for y in range(h):
            r,g,b=im2.getpixel((x,y))
            total = r+g+b
            if total > 230:
                im2.putpixel((x,y), (255,255,255))
            else:
                im2.putpixel((x,y), (0,0,0))
    return im2

def paste_to_back(pasted_im,play_im):
    back_im = Image.new(pasted_im.mode,(900,1600),(0,0,0))
    b_x,b_y = back_im.size
    start_x = int((b_x - pasted_im.size[0])/2)
    start_y = int((b_y - pasted_im.size[1])/4)
    back_im.paste(pasted_im,(start_x,start_y))

    back_im.paste(play_im,(int((back_im.size[0]-play_im.size[0])/2),1000))
    return back_im

def main():
    gif_name = input("file name : ")
    ims = get_files()
    im = ims["album"]
    im_x,im_y= im.size

    if im_x > im_y:
        im_2r = im_y
    else:
        im_2r = im_x
    im_list = []
    s_im = make_circle(im,im_2r)
    play_im = make_play_im(ims["play"],im_2r+200)

    for i in range(0,360,1):
        k_im = s_im.rotate(i)
        p_im = paste_to_back(k_im,play_im)
        im_list.append(p_im)

    im_list[0].save("../gif/"+gif_name+".gif", save_all=True, append_images=im_list[1:],optimize=True, duration=100, loop=0) 

    shutil.rmtree("../img/")
    os.mkdir("../img")

if __name__ == "__main__":
    main() 