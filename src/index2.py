from PIL import Image

img_name = input('image : ')
gif_name = input('gif : ')
img = Image.open(img_name)  # 元画像読み出し
width, height = img.size   # サイズの取得

img_list = []   # 画像保存用リスト

# 回転処理
for i in range(0,360,1):
    # 画像を5度ずつ回転し中心を300x300px切り抜いてgif画像リストに追加する    
    img_r = img.rotate(i)

    img_list.append(img_r)

#アニメーションgifファイルを作成(1フレーム100ms,ループ)
img_list[0].save(gif_name, save_all=True, append_images=img_list[1:],optimize=True, duration=100, loop=0)  






