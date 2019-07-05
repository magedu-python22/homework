import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def randcolor(start=0, end=255):
	return tuple(random.randint(start, end) for _ in range(3))

def randcode():
	strs = string.ascii_uppercase + string.digits
	return random.choice(strs)

font = ImageFont.truetype('C:/Windows/Fonts/ALGER.TTF', 36)
for i in range(100):
	image = Image.new('RGB', (360, 60), (20, 20, 20))
	draw = ImageDraw.Draw(image)
	''' 背景颜色处理，比较耗时
	for x in range(360):
		for y in range(60):
			draw.point((x, y), fill=randcolor(50, 80))
	'''
	for t in range(6):
		draw.text((60 * t + 10, 10), randcode(), font=font, fill=randcolor())
	image.save(f'code{i+1}.jpg', 'jpeg')
