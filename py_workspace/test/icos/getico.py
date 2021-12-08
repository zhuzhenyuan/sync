import os
import shutil
from PIL import Image

gif_path = [
    # "./src/shenlilinhua.gif",
    "./src/leishen.gif",
]
sizes = ['32x32', '18x18']


def create_dir(new_path):
    if os.path.exists(new_path):
        shutil.rmtree(new_path)
    os.makedirs(new_path)


def change2ico(new_path):
    # 获取目录下文件名
    files = os.listdir(new_path)

    for size in sizes:
        ico_dir = os.path.join(new_path, size)
        create_dir(ico_dir)

        size = list(map(int, size.split('x')))

        for file in files:
            # 分离文件名与扩展名
            filename, suffix = os.path.splitext(file)
            # 因为python文件跟图片在同目录，所以需要判断一下
            if suffix == '.png':
                out_name = filename + '.ico'

                try:
                    # 打开图片并设置大小
                    im = Image.open(os.path.join(new_path, file)).resize(size)
                    # 图标文件保存至icon目录
                    im.save(os.path.join(ico_dir, out_name))

                    # import PythonMagick
                    #
                    # img = PythonMagick.Image(os.path.join(new_path, file))
                    #
                    # # 这里要设置一下尺寸，不然会报ico尺寸异常错误
                    # img.sample(size)
                    # img.write(os.path.join(ico_dir, out_name))

                except IOError:
                    print('connot convert :', file)


def get_imgs(gif_path):
    print(os.path.dirname(gif_path))
    print(os.path.basename(gif_path))
    file_name = os.path.basename(gif_path).split('.')[0]
    new_path = os.path.join(os.path.dirname(gif_path), file_name)
    create_dir(new_path)

    gif = Image.open(gif_path)
    try:
        gif.save(f"{new_path}/{file_name}_light_{gif.tell()}.png")
        gif.save(f"{new_path}/{file_name}_dark_{gif.tell()}.png")
        while True:
            gif.seek(gif.tell() + 1)
            gif.save(f'{new_path}/{file_name}_light_{gif.tell()}.png')
            gif.save(f'{new_path}/{file_name}_dark_{gif.tell()}.png')
    except Exception as e:
        print("get imgs end")

    # change2ico(new_path)


if __name__ == "__main__":
    for p in gif_path:
        get_imgs(p)
