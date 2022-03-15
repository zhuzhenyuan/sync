# coding: utf8
import os
import sys
import mmap


def a(op, file_path):
    video_data = None
    with open('camouflage.txt', 'rb') as f:
        video_data = f.read()
    if len(video_data) <= 0:
        print("video not data")
        return
    video_size = len(video_data)
    file_size = os.path.getsize(file_path)  # 文件大小
    if file_size < len(video_data):
        print("文件小于")
        return
    if op == "encode":
        with open(file_path, "r+b") as f:
            mm = mmap.mmap(f.fileno(), file_size + video_size)
            tmp = mm[:video_size]
            mm[:video_size] = video_data
            mm.flush(0, video_size)
            mm[file_size:] = tmp
            mm.flush(file_size, video_size)
            new_file_path = file_path + ".txt"
            mm.close()
    elif op == "decode":
        with open(file_path, "r+b") as f:
            mm = mmap.mmap(f.fileno(), file_size)
            tmp = mm[file_size-video_size:]
            mm[:video_size] = tmp
            mm.flush(0, video_size)
            mm.resize(file_size-video_size)
            new_file_path = file_path[:-4]
            mm.close()
    else:
        return
    os.rename(file_path, new_file_path)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print("args is error")
        exit(0)
    a(sys.argv[1], sys.argv[2])
    # a('encode', 't2.png')


