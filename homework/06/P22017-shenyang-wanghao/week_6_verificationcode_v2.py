from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
for j in range(100):
	def getRandomColor():
		"""get 6 random color with (r,g,b) format"""

		color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		return color

	def getRandomStr():
		"""get 6 random string"""

		char = random.choice([chr(random.randint(65,90)), str(random.randint(0,9))])
		return char
		
	image = Image.new('RGB', (180, 30),getRandomColor())
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("kumo.ttf",size=26)

	for i in range(6):

		random_char = getRandomStr()
		draw.text((10+i*30,0),random_char,getRandomColor(),font=font)
	image.save(open(str(j)+".png",'wb'),'png')


"""
函数可以抽出来，单独放，最好不要放到for 循环体内
"""
		
