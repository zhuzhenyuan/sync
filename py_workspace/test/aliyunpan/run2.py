# coding: utf8
import os
import sys
import mmap

png_head = b'\x89PNG'
mark = b'6mehm8pZdjeqyobun4cZwXxjY5x6ybu25nACRYeQ'


def check_operate(mm, file_size, mark_size, head_data):
    if file_size - mark_size < 0 and png_head not in head_data:
        # 不是png文件，且长度不足的
        op = 'encryption'
    else:
        mm.seek(file_size - mark_size)
        if mark in mm.readline():
            op = 'decrypt'
        else:
            op = 'encryption'
    return op


def decrypt(mm, file_size, mark_size, file_path):
    sign = mm[file_size - mark_size:file_size]
    original_head = sign[:len(png_head)]

    mm[:4] = original_head
    mm.flush(0, 4)

    mm.resize(file_size - mark_size)

    if '.' not in file_path:
        new_file = file_path+'_recover'
    else:
        new_file = '.'.join(file_path.split('.')[:-1])
    print('%s -> %s' % (file_path, new_file))
    return new_file


def encryption(mm, file_size, mark_size, head_data, file_path):
    mm[:4] = png_head
    mm.flush(0, 4)
    now_mark_size = len(png_head) + len(mark)
    mm[file_size:file_size + now_mark_size] = head_data + mark
    mm.flush(file_size, mark_size)

    new_file = file_path + '.png'
    print('%s -> %s.png' % (file_path, new_file))
    return new_file


def run(file_path):
    file_size = os.path.getsize(file_path)  # 文件大小
    if file_size < len(png_head):
        print("文件小于%d字节，不处理" % len(png_head))
        return

    # 完整签名大小
    mark_size = len(png_head) + len(mark)

    with open(file_path, "r+b") as f:
        try:
            mm = mmap.mmap(f.fileno(), file_size + mark_size)
            head_data = mm.read(len(png_head))  # 当前文件头部

            # 不处理 png源文件
            if png_head in head_data and mark not in mm[file_size - mark_size:]:
                print("png will not handle")
                return
            op = check_operate(mm, file_size, mark_size, head_data)
            if op == "decrypt":
                new_file = decrypt(mm, file_size, mark_size, file_path)
                file_size = file_size - mark_size
            elif op == "encryption":
                new_file = encryption(mm, file_size, mark_size, head_data, file_path)
                file_size = file_size + mark_size
            else:
                print("not support: " + file_path)
                return
        finally:
            print(file_size)
            mm.resize(file_size)
        mm.close()

    os.rename(file_path, new_file)
    print("done")


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        print("just support one file")
        exit(0)

    run(sys.argv[1])
