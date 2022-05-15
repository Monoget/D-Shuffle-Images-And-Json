from PIL import Image

# Image.open() can also open other image types
img = Image.open("data/images/1.png")
# WIDTH and HEIGHT are integers
resized_img = img.resize((1600, 1578))
resized_img.save("1.png",optimize=True,quality=10)