import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def randcolor(start=0, end=255):
	return tuple(random.randint(start, end) for _ in range(3))

def randcode():
	strs = string.ascii_uppercase + string.digits
	return random.choice(strs)

width = 60 * 6
height = 60
image = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('C:/Windows/Fonts/ALGER.TTF', 36)
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=randcolor(50, 80))
for t in range(6):
	draw.text((60 * t + 10, 10), randcode(), font=font, fill=randcolor())
image.save('code.jpg', 'jpeg')