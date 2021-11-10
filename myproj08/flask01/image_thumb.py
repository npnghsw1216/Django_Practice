# pip install pillow

from PIL import Image

im = Image.open("static/cat.jpg")
im.thumbnail((800, 600))
im.save("static/cat.jpg")
