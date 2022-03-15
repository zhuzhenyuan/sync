# coding: utf8
import os
import sys
import mmap
png_head = b'\x89PNG'
zip_head = b'PK\x03\x04'

def check_operate(bdata):
    if png_head in bdata:
        return 'decrypt'
    if zip_head in bdata:
        return 'encryption'


def run(file):
    new_file = '.'.join(file.split('.')[:-1])
    with open(file, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 4)
        head_data = mm.readline()
        op = check_operate(head_data)
        if op == "decrypt":
            mm[:4] = zip_head
            new_file += '.zip'
            print('png -> zip')
        elif op == "encryption":
            mm[:4] = png_head
            new_file += '.png'
            print('zip -> png')
        else:
            print("not support: " + file)
            return
        mm.flush(0, 4)
        mm.close()

    os.rename(file, new_file)
    print("done")


if __name__ == "__main__":

    # print(sys.argv)
    # if len(sys.argv) != 2:
    #     print("just support one file")
    #     exit(0)
    
    # run(sys.argv[1])
    run("E:\万华镜\美少女万華鏡2.5 -かつて少女だった君へ-献给曾是少女的你.png")
