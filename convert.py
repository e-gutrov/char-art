import json


d = {}


def init():
    global chars
    with open('chars.json', 'r') as fin:
        chars = json.load(fin)


def main():
    init()
    fin = open(input('Введите путь к файлу: '), 'r')
    fout = open(input('Введите путь к файлу: '), 'w')
    txt = list(map(lambda x: x.strip(), fin.readlines()))
    for i in range(len(txt)):
        for j in txt[i]:
            print(chars[len(chars) - d[j] - 1], end='', file=fout)
        print(file=fout)
    fin.close()
    fout.close()


main()
