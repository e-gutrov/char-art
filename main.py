from PIL import Image
import numpy as np
import json


def init_chars():
    with open('chars.json', 'r') as fin:
        chars = json.load(fin)
    return chars


def to_wb(a):
    return round(sum(a) / len(a))


def get_char(x, chars):
    return chars[int(len(chars) / 256 * x)][0]


def scale(a, need_size, man):
    if not man:
        need_size = (need_size[0], round(need_size[1] * 1.5))  # chars' width is less than height
    scale_i = a.shape[0] / need_size[0]
    scale_j = a.shape[1] / need_size[1]
    b = np.zeros(need_size).astype(np.uint8)
    for i in range(need_size[0]):
        for j in range(need_size[1]):
            b[i][j] = a[round(i * scale_i)][round(j * scale_j)]
    return b


def main():
    chars = init_chars()
    name = input('Enter a filename: ')
    img = Image.open(name)
    rgb_cols = np.asarray(img)
    wb_cols = np.zeros((rgb_cols.shape[0], rgb_cols.shape[1])).astype(np.uint8)
    print('Wait a bit...')
    for i in range(wb_cols.shape[0]):
        for j in range(wb_cols.shape[1]):
            wb_cols[i][j] = to_wb(rgb_cols[i][j][:3])

    operation = input(
        'Image size is {0}x{1} pts.\n'
        'Enter "dec x" to decrease size by x times\n'
        'Enter "man w h" to get image with size w h (in chars): '.format(
            wb_cols.shape[1], wb_cols.shape[0]
        )
    )
    if operation[:3] == 'dec':
        man = False
        times = float(operation.split()[1])
        sz = tuple((int(wb_cols.shape[0] / times), int(wb_cols.shape[1] / times)))
    else:
        man = True
        sz = tuple(map(int, operation.split()[2:0:-1]))

    with open(input('Enter path to output file: '), 'w') as f:
        scaled_picture = scale(wb_cols, sz, man)
        for i in range(scaled_picture.shape[0]):
            for j in range(scaled_picture.shape[1]):
                print(get_char(scaled_picture[i][j], chars), end='', file=f)
            print(file=f)


main()
