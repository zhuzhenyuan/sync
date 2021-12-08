from PIL import Image

im = Image.open('test.png', 'r').resize((32, 32), Image.NEAREST)
print(im.size, im.format, im.mode)
# im.resize((32, 32), Image.LANCZOS)
print(im.size, im.format, im.mode)
# im.show()

# im.save("./dst.ico")

# Image.BICUBIC
# Image.LANCZOS
# Image.BILINEAR
# Image.NEAREST

