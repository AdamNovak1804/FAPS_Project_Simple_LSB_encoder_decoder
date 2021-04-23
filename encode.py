import os
import sys
import imghdr
from PIL import Image, UnidentifiedImageError

DIGITS = 6
RGB = 3
FRACTION_OF_BYTE = 8


def encode(src_data, pixels, src_len, width):
    num = src_len
    ext = (DIGITS-len(str(num)))*'0' + str(num) + src_data
    ext_list = list()
    todo = list()

    for i in range(0, len(ext)):
        ext_list.append(ord(ext[i]))

    for i in range(0, len(ext_list)):
        for j in range(0, 8):
            todo.append((ext_list[i] >> (7-j)) & 1)

    del ext_list
    j = 0
    a = 0
    b = 0
    buf = list(pixels[a, b])
    for i in range(1, len(todo)+1):
        if todo[i-1]:
            buf[j] |= 1 << 0
        else:
            buf[j] &= ~(1 << 0)
        j += 1
        pixels[a, b] = tuple(buf)
        if i % 3 == 0:
            j = 0
            if b > width:
                a += 1
                b = 0
            else:
                b += 1
            buf = list(pixels[a, b])


def main():
    try:
        src_path = sys.argv[1]
        try:
            src = open(src_path, 'r')
            src_len = os.path.getsize(src_path)
        except FileNotFoundError:
            print('ERROR: Source file not found')
            return 0
    except IndexError:
        print('ERROR: No source file argument given')
        return 0

    try:
        dst_path = sys.argv[2]
        try:
            dst = Image.open(dst_path)
        except (FileNotFoundError, UnidentifiedImageError):
            print('ERROR: Destination file invalid/not found')
            return 0
    except IndexError:
        print('ERROR: No destination file argument given')
        return 0

    src_data = src.read(src_len)
    pixels = dst.load()
    width, height = dst.size

    img_bytes = int((width * height) * (RGB/FRACTION_OF_BYTE)) - DIGITS

    if src_len > img_bytes:
        print('ERROR: Source file cannot be inserted, choose larger file')
        return 0

    encode(src_data, pixels, src_len, width)

    dst.save("output.png")


main()
