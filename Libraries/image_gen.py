from PIL import Image  

width = 1920    
height = 1080

img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193))
img.show()