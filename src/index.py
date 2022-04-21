from PIL import Image, ImageDraw

#画像ファイル名宣言
pic_name="let_me_know.png"
pic_name_out="out.png"
#追加枠ピクセル数


im = Image.open(pic_name).convert("RGB")
draw = ImageDraw.Draw(im)

x,y = im.size
eX, eY = int(x/5),int(x/5)
bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw.ellipse(bbox , fill=(0, 0, 0), outline=(0, 0, 0))


im.save('pillow_imagedraw.png', quality=95)