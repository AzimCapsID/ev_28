'''
работа c файлам

каретка - указатель - курсор

'''
# open(<путь до файла>)

# file = open('~/Desktop/ev.28/lecture/files.py ') - # абсолютный путь
# file = open('files.py') #относительный путь(относительно той директории в которой вы работаете)
'''
# Режимы работы c файлами

1. чтения - r/r+(read)
2. запис - w/w+ (write)
3. добавления -> a/a+ (append)
# b, x, t
'''

# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# file = open('text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# Контекстный менеджер
# with open('text.txt') as file: #file = open('text.txt')
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')

# print(file, 'outside')

# file.tell() -> возвращает индекс где находится каретка(курсор)

# file.seek(index) -> перемещает курсор на индекс который вы передали

# with open('text.txt', 'r') as file:
#     # print(file.readline().replace('\n', ''))
#     # print(file.tell())
#     # file.seek(0)
#     # print(file.readline().replace('\n', ''))

#     # data = file.read()
#     # index = data.index('\n')
#     # file.seek(index+1)
#     # print(file.readline().replace('\n', ''))
#     # print(file.readlines()[1])

#     print(file.tell())
#     file.read()
#     file.seek(0)
#     print(file.tell())
#     print(file.readline())

# with open('text.txt', 'r') as file:
#     # print(file.readline(3))
#     # print(file.readlines(14))
#     print(file.read(5))

# with open('text.txt', 'w') as file:
#     file.write('Pervaya STRochks\n')
#     file.write('John Snow is bastard of Ned Stark!\n')
#     file.write('This is lesson about files!\n')
#     file.seek(0)
#     data = ['Bilal is Genius\n', 'Tima is good boy!\n']
#     file.writelines(data)

# with open('text.txt', 'r+') as file:
#     file.write('John Snow!')
#     file.seek(0)
#     print(file.read())

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string, type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image = 'imei.jpg'
# get_imei_code(image)

