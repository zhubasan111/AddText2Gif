from PIL import Image, ImageDraw, ImageFont
import math

name = "catTrain"
im = Image.open(name+".gif")

imgs = [im.copy()]

tp = im.size[0]//2-40
bt = im.size[0]//2+120
lf = im.size[1]-331
rt = im.size[1]-61

try:
	while 1:
		im.seek(im.tell()+4)
		im2 = im.copy()
		im2 = im2.crop((lf, tp, rt, bt))
		imgs.append(im2)
# do something to im
except EOFError:
	pass # end of sequence


imgs[0] = imgs[0].crop((lf, tp, rt, bt))


text = ['每天起床第一句', '早安我的阿加西!']


basej = imgs[0].size[0]//2
basei = 40
zbsFont = ImageFont.truetype('./MaShanZheng-Regular.ttf', 25)
div = math.ceil(len(imgs)/len(text))


for i in range(len(imgs)):
	draw = ImageDraw.Draw(imgs[i])
	posi = (basej - len(text[i//div])*12, basei)
	draw.text(posi, text[i//div], fill=0, font=zbsFont, anchor=None)


imgs[0].save('./savedCat.gif',
               save_all=True, append_images=imgs[1:], optimize=False, duration=120, loop=0)
