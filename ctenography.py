from PIL import Image, ImageDraw
from random import randint
import os
from tkinter import filedialog as fd
from tkinter import Tk


def get_path(type):
    root = Tk()
    if type:
        name_file = fd.askopenfilename(title='Выберите изображение')
    else:
        name_file = fd.askopenfilename(title='Файл "key.txt"')
    root.destroy()
    return name_file


def encode():
    if not os.path.exists('coding_img'):
        os.mkdir('coding_img')

    keys = open('coding_img/key.txt', 'w')

    img = Image.open(get_path(1))
    draw = ImageDraw.Draw(img)

    width = img.size[0]
    height = img.size[1]
    pixels = img.load()

    list_elem = []
    for i in input('Ваше сообщение: '):
        if ord(i) < 1040:
            list_elem.append([ord(i)])
        else:
            list_elem.append([ord(i) - 1000, 'r'])

    for elem in list_elem:
        key = (randint(1, width - 1), randint(1, height - 1))
        red, green = pixels[key][:2]
        draw.point(key, (red, green, elem[0]))

        if elem[-1] == 'r':
            keys.write(str(key[0]) + ' ' + str(key[-1]) + ' ' + 'r' + '\n')
        else:
            keys.write(str(key[0]) + ' ' + str(key[-1]) + '\n')

    img.save('coding_img/coded_img.png', 'PNG')
    keys.close()


def decode():
    keys = open(get_path(0))
    keys = [i.strip().split(' ') for i in keys.readlines()]

    img = Image.open(get_path(1))

    pixels = img.load()
    message = ''

    for i in keys:
        if i[-1] == 'r':
            message += chr(pixels[int(i[0]), int(i[1])][2] + 1000)
        else:
            message += chr(pixels[int(i[0]), int(i[1])][2])

    print('Ваше сообщение: ' + message)


while True:
    a = input('1 - закодировать, 2 - декодировать: ')
    if a == '1':
        encode()
    elif a == '2':
        decode()
    else:
        break
