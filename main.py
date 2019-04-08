from PIL import Image
import numpy as np
import json


chars = []


def init():
    global chars
    with open('chars.json', 'r') as fin:
        chars = json.load(fin)


def to_wb(a):
    return round((int(a[0])+a[1]+a[2]) / 3)


def get_char(x):
    global chars
    return chars[int(91 / 256 * x)]


def scale(a, need_size):
    need_size = (need_size[0], round(need_size[1] * 1.5))
    scale_i = a.shape[0] / need_size[0]
    scale_j = a.shape[1] / need_size[1]
    b = np.zeros(need_size).astype(np.uint8)
    for i in range(need_size[0]):
        for j in range(need_size[1]):
            b[i][j] = a[round(i * scale_i)][round(j * scale_j)]
    return b


def main():
    init()
    name = input('Введите имя файла: ')
    # name = 'test128.png'
    img = Image.open(name)
    rgb_cols = np.asarray(img)
    wb_cols = np.zeros((rgb_cols.shape[0], rgb_cols.shape[1])).astype(np.uint8)

    for i in range(wb_cols.shape[0]):
        for j in range(wb_cols.shape[1]):
            wb_cols[i][j] = to_wb(rgb_cols[i][j][:3])

    tp = input(
        'Размер изобрежения {0}x{1} пикселей. Уменьшить размер в n раз-1, задать свой размер-2.'.format(
            wb_cols.shape[0], wb_cols.shape[1]
        )
    )
    if tp == '1':
        n = float(input('Во сколько раз вы хотите уменьшить размер?'))
        sz = tuple((int(wb_cols.shape[0] / n), int(wb_cols.shape[1] / n)))
    else:
        sz = tuple(map(int, input(
            'Введите итоговый размер картинки (в символах). '
            'Рекомендуется не более {0}x{1} и не менее {2}x{3}: '.format(1, 2, 3, 4)).split()))

    with open('output.txt', 'w') as f:
        char_picture = scale(wb_cols, sz)
        for i in range(char_picture.shape[0]):
            for j in range(char_picture.shape[1]):
                print(get_char(char_picture[i][j]), end='', file=f)
            print(file=f)


main()
