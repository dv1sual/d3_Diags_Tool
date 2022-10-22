from PIL import Image
from random import randrange

rand_color = (randrange(255), randrange(255), randrange(255))

width = 1920
height = 1080

img  = Image.new( mode = "RGB", size = (width, height), color = rand_color)
img.show()
#img.save()