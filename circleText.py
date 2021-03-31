from PIL import Image, ImageDraw, ImageFont

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)


zbsFont = ImageFont.truetype('./MaShanZheng-Regular.ttf', 20)

draw = ImageDraw.Draw(images[0])
draw.text((0,0), '宝贝!', fill=255, font=zbsFont, anchor=None)

images[0].save('./expandingCircle.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
