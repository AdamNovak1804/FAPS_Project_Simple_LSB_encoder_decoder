import sys
import math
from PIL import Image

DIGITS = 6
RGB = 3
FRACTION_OF_BYTE = 8


def clr_lists(out, out_str):
    del out
    del out_str


def list_bits(pixels, width, iters, a, b):
    out = list()
    for i in range(0, iters):
        buf = list(pixels[a, b])
        buf[0] &= 1
        buf[1] &= 1
        buf[2] &= 1
        out.append(buf[0])
        out.append(buf[1])
        out.append(buf[2])
        if b > width:
            a += 1
            b = 0
        else:
            b += 1
    return out, a, b


def merge_nums(out, length):
    out_str = list()
    char = 0
    j = 0
    for i in range(0, length):
        if i % 8 == 0 and i != 0:
            char = int('{:08b}'.format(char)[::-1], 2)
            out_str.append(chr(char))
            char = 0
            j = 0
        if out[i]:
            char |= 1 << j
        j += 1

    char = int('{:08b}'.format(char)[::-1], 2)
    out_str.append(chr(char))
    return out_str


def main():
    try:
        path = sys.argv[1]
        try:
            img = Image.open(path)
        except FileNotFoundError:
            print('ERROR: Wrong file/file not found')
            return 0
    except IndexError:
        print('No file argument given')
        return 0

    pixels = img.load()
    width, height = img.size

    out, end_a, end_b = list_bits(pixels, width, 16, 0, 0)
    out_str = merge_nums(out, len(out))

    try:
        length = int(''.join([str(elem) for elem in out_str]))
    except ValueError:
        print('ERROR: File has invalid number range')
        return 0

    img_bytes = int((width * height) * (RGB / FRACTION_OF_BYTE)) - DIGITS

    if length > img_bytes:
        length = img_bytes

    iters = math.ceil((length * 8) / 3)

    clr_lists(out, out_str)

    out, end_a, end_b = list_bits(pixels, width, iters, end_a, end_b)
    out_str = merge_nums(out, int(len(out) - (len(out) % 8)))

    print(''.join([str(elem) for elem in out_str]))


main()
