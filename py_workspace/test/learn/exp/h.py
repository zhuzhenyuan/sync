import os
import shutil

from PIL import Image


path = "./leishen.gif"
w = 100
h = 100

tag = Image.open(path)
# tag = tag.resize((w, h), Image.NEAREST)
tag = tag.convert("RGB")

ascii_char = list("$@B%8&WM#*oaqwmZO0QLCJrjft/\|()1{}[]?-_+~<>i!LI;:,\"^`'.")


print(tag.mode)
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


ch = ""  # 就是一张图片的字符串化
for i in range(w):
    for j in range(h):
        ch += get_char(*tag.getpixel((j, i)))
    ch += '\n'

print(ch)

# tdy = 0.027
# for i in range(5355):
#     a = '%d' % i
#     t = 4-len(a)
#     if(t==1):
#         a = '0'+a
#     if t==2:
#         a = '00'+1
#     if t==3:
#         a = '000'+a
#     printimg()
