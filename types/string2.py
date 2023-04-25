# str
# ''
# 'Hello'
# str(5)


# print(dir(str))
# print(dir(int))


# a = 'Hello'
# b = 'john'
# # print(a != b)
# # print('abs' == 'abs')

# print( a > b)
# print( a < b)

# print('a') # 97 -> 1100001
# print('a' > 'b') # 97 -> 98
# print('h' > 'c') # 104 -> 99

# print('Hello' > 'harry')
# print('abs' > 'abs') #False

# a = 'Hello'
# b = 'john snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# >, <, ==, !=, >=, <=

# Методы строк
# replace(old, new, [count]) - меняет в строке  символы old на new, если вы
# укажжете count, то зааменит count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello World! My name is john snow!'
# res = str1.replace('john snow', 'tirion lanister')
# print(res)

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   ' 
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))


# print(dir(str))


# isdigit -     проверяют
# isnumeric - ->  состоит ли наша строка
# isdecimal - польностью из чисел

# num = input('Vvedite chislo: ')
# print(f'Vvedeno chislo?:  {num.isdigit()}')

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chislo')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())


# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского и кирилицского алфавита
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha -> состоит ли наша строкка польностью из символов алфавита

# text = 'Hello World'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())


# islower
# isupper
# istitle

# str1 = 'Is. My name'
# print(str1.islower())
# print(str1.istitle())
# str2 = 'JHHFDK'
# print(str2.isupper())

# index(value, [start], [end]) - выводит индекс значения value, которое мы передаем, в нащей строке.

# text = 'Hello john snow'
# print(text.index('john'))

# text = 'Hello world! My name is John Snow!' # o
# # print(text.index('John'))
# res = text.index('o') 
# print(res) #4
# res = text.index('o', res + 1)
# print(res) #7
# res = text.index('o', res + 1)
# print(res) #25
# res = text.index('o', res + 1)
# print(res) #31

# count(value, [start]) - считает кол-во вхождений value в нашу строку


# text = 'hello o o o hello'

# print(text.count('o'))
# print(text.count('hello'))

# split(separator) - дробит нашу строку на несколько частей по разделителю,
#  все части строк сохраняются в типе list

# text = 'let me speak by my heart in english! Cause my name is John Snow!'

# a = '#hello#hello#hello'
# res = a[1:].split('o')
# print(res)

# res = text.split(' ')
# print(res)
# print(len(res))

# 'connector'.join(list) -> соединяет по connector строки которые находились в list

# text = 'let me speak by my heart in english! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)


# str1 = '#'.join(res)
# print(str1)

# find(value, [start], [end]) - делает тоже самое что и index, но если не нашел то вернется -1

# text = 'Hello'
# print(text.find('l'))
# print((text.find('leyt')), type(text.find('leyt')))

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'hello WorLD, JOHN snow'
# print(f'Orginal: {text}')
# print (text.upper())
# print (text.lower())
# print (text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

# name = input('vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}')

# fio = 'john snow'
# print(fio.title())
print(dir(set))



















