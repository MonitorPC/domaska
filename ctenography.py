from PIL import Image, ImageDraw
from random import randint
import os

a = input('1 - закодировать, 2 - декодировать: \n')
if a == '1':
    if not os.path.exists('codirovka'):
        os.mkdir('codirovka')

    keys = open('codirovka/key.txt', 'w')

    img = Image.open(input('Путь до картинки: '))
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
        print(elem)
        key = (randint(1, width - 1), randint(1, height - 1))
        red, green = pixels[key][:2]
        draw.point(key, (red, green, elem[0]))
        if elem[-1] == 'r':
            keys.write(str(key[0]) + ' ' + str(key[-1]) + ' ' + 'r' + ' ' + '\n')
        else:
            keys.write(str(key[0]) + ' ' + str(key[-1]) + '\n')

    img.save('codirovka/zacodirovan.png', 'PNG')
    keys.close()

elif a == '2':

    path_file = input('Путь до папки "codirovka": ')

    keys = open(f'{path_file}\key.txt')
    keys = [i.strip().split(' ') for i in keys.readlines()]

    img = Image.open(f'{path_file}\zacodirovan.png')

    pixels = img.load()
    message = ''

    for i in keys:
        print(i)
        if i[-1] == 'r':
            print(pixels[int(i[0]), int(i[1])][2] + 1000)
            message += chr(pixels[int(i[0]), int(i[1])][2] + 1000)
        else:
            message += chr(pixels[int(i[0]), int(i[1])][2])

    print('Ваше сообщение: ' + message)
