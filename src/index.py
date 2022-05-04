from PIL import Image, ImageDraw

def make_circle(im,im_2r):
    im_a = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(im_a)
    draw.ellipse((0,0,im_2r,im_2r),fill=255)
    im_rgba = im.copy()
    im_rgba.putalpha(im_a)
    im_rgba_crop = im_rgba.crop((0,0,im_2r,im_2r))
    return im_rgba_crop



def paste_to_back(pasted_im,im_2r):
    mask_im = Image.new('RGBA',(900,1600),0)
    back_im = mask_im.copy()
    b_x,b_y = mask_im.size
    start_x = int((b_x - im_2r)/2)
    start_y = int((b_y - im_2r)/4)
    im_clear = Image.new("RGBA", back_im.size, (255, 255, 255, 0))
    im_clear.paste(pasted_im,(start_x,start_y))
    back_im = Image.alpha_composite(im_clear,back_im)
    return back_im


def main():
    im_name = "IMG_4008"
    im = Image.open("../img/"+im_name+".jpg").convert('RGBA')
    im_x,im_y= im.size

    if im_x > im_y:
        im_2r = im_y
    else:
        im_2r = im_x

    s_im = make_circle(im,im_2r)
    im_list = []
    for i in range(0,360,1):
        k_im = s_im.rotate(i)
        f_im = paste_to_back(k_im,im_2r)
        im_list.append(f_im)

    im_list[0].save("../img/g_im.gif", save_all=True, append_images=im_list[1:],optimize=True, duration=100, loop=0) 

if __name__ == "__main__":
    main()



 