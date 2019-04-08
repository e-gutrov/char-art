from PIL import Image
import numpy as np


def to_wb(a):
    return round((int(a[0]) + a[1] + a[2]) / 3)


DIR = 'chars_pics/'
all_chars_strs = ['1234567890-=', 'qwertyuiop[]', 'asdfghjkl;\'', 'zxcvbnm,./', '!@#$%^&*()_+', 'QWERTYUIOP{}', 'ASDFGHJKL:"', 'ZXCVBNM<>?']

# shift = 230
# per_char = 82
fout = open('output.txt', 'w')
for i in range(len(all_chars_strs)):
    for j in range(len(all_chars_strs[i])):
        img = None
        if all_chars_strs[i][j] == '.':
            img = Image.open(DIR + 'dot.png')
        elif all_chars_strs[i][j] == '/':
            img = Image.open(DIR + 'slash.png')
        else:
            img = Image.open(DIR + all_chars_strs[i][j] + '.png')
        cnt = 0
        ar = np.asarray(img)
        for k in range(ar.shape[0]):
            for s in range(ar.shape[1]):
                if to_wb(ar[k][s]) > 100:
                    cnt += 1
        print(all_chars_strs[i][j], cnt, file=fout)
        img.close()

fout.close()

# for i in range(1, 4):
#     all_chars_img = Image.open(DIR + str(i) + '_all.png')
#     h = all_chars_img.size[1]
#     # print(all_chars_img.size)
#     for j in range(len(all_chars_strs[i])):
#         print(j, all_chars_strs[i][j])
#         img = all_chars_img.transform((per_char, h), Image.EXTENT,
#                                       data=(shift + per_char * j, 0, shift + per_char * (j + 1), h))
#         if all_chars_strs[i][j] == '.':
#             img.save(DIR + 'dot.png')
#         elif all_chars_strs[i][j] == '/':
#             img.save(DIR + 'slash.png')
#         else:
#             img.save(DIR + all_chars_strs[i][j] + '.png')



# ar = np.asarray(all_chars_img)
# s = set()
# for i in range(ar.shape[0]):
#     for j in range(ar.shape[1]):
#         s.add(tuple(ar[i][j]))
# print(ar)
# print(*s)
# shift = 28
# per_char = 33
# for i in range(10):
#     img = all_chars_img.transform((30, 66), Image.EXTENT, data=(shift + per_char * i, 0, shift + per_char * (i + 1), 66))
#     img.save(DIR + all_chars_str[i] + '.png')