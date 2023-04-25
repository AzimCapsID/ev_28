'''
Встроенные функции
'''

'''
Анонимная функция - lambda(оБычная функция с одной особенность, у нее нет имени)
Принимает сколько угодно параметров но всегда возвращает одно выражение
'''

# def hello():
#     return 'hello'

# # print(hello())

# x = lambda: 'hello'
# print(x())



# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 5))

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2

# print(x(5, 5, 3))
# print(x(5, 5))

# def myfunc(n):
#     return lambda num: num * n

# mydo = myfunc(2)
# print(mydo(50))

# dict_ = ['hello', 'bil', 'john', 'dan']

# a = sorted(dict_, key = len, reverse=True)

# print(a)

# dict_ = {
#     'john': 500,
#     'tir': 160_000,
#     'tom': 150,
#     'ayana': 200_000
# }

# print(dict_.items())
# new_dict = dict(sorted(dict_.items(), key=lambda x: x[1]).reversed=True))
# print(new_dict)

'''
map(function, iterable) - применяется к каждому элементу внутри iterable функцию, которую мы ей передаем
в function, закидывая в результат те данные, которые возвращает функция. В результате мы поллучаем 
mapobject(iterator), в которм хранятся все наши данные
'''

# ls = ['one', 'two', 'three', 'four']
# ls = ['1', '2', '3']

# # new_list = list(map(lambda x: x.capitalize(), ls))
# # print(new_list)

# new_list = list(map(int, ls))
# print(new_list)

# ls = ['Azim', 'john', 'aria', 'baku', 'bakberdi']

# # new_list = list(map(lambda x:'hello, mr/mrs' x, ls))

# newls = list(map(lambda x: f'hello mr/mrs {x}', ls))

# print(newls)

'''
Функция высшего порядка - функция, которая принимает в качестве аргументе другую функцию
'''
# map(int, names)

'''
filter(finction, iterable) - принимает ко всем элементам  iterable функцию которую мы
передали  и возвращает filterobject(iterator) только с ттеми элементами для которых функция вернула
True
'''

# ls = ['one', 'two', 'oleg', 'billie']

# res = list(filter(lambda x : len(x) > 4, ls))
# res = list(filter(lambda x : x.startswith('o'), ls))
# print(res)


'''
enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее 
собственным индексом
'''

# ls = ['str1', 'str2', 'str3']
# newlist = list(enumerate(ls))
# print(newlist)
'''
# zip(iterables) - она соединяет каждый элемент итерируемых оюбектов между собой в тип данных tuple
# и возвращает iterator
'''

# ls1 = [1,2,3]
# ls2 = [200, 100, 300]

# res = dict(zip(ls1, ls2))
# print((res))

# ls1 = [1,2,3,4,5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [20, 10, 30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

'''
# zip для создания словарей
'''

# dKeys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'Oktober':['bishkek_oktober', 'Gorkaya 212', 'Vefa', 'Cisco', '10.233.255.93'],
#     '1mai':['bishkek_1may', 'Jibek Jolu 212', 'BelyiDom', 'Cisco', '10.33.05.93'],
#     'Svrdl':['bmay', 'Jolu 212', '4Domes', 'Cisco', '10.121.255.93']
# }

# bishkek_data  = {}

# for k in data:
#     bishkek_data[k] = dict(zip(dKeys,data[k]))

# print(bishkek_data)

'''
all(), any()

all(iterable) - Возвращает True, если все элементы итерируемого обьекта истина, иначе False
'''
# ls = [5,6,7]
# print(all(ls)) #True

# ip = '10.42.45.45' #True
# ip1 = '23.5y.66.4' #False

# # res = all(x.isdigit() for x in ip1.split('.')) #False
# res = all(x.isdigit() for x in ip.split('.')) # True
# print(res)

'''
any() - возвращает True, если хотябы один элемент истина
'''

# ls = [1,2,3,[1,2]]
# ls = [0,0,0,[0]]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Введите команду; ')

# if any(z in command for z in ignore):
#     raise Exception('Block you!')

# print('Its oK')

# - ----------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()+-@!#%'
# q_pass = int(input('Vvedite kol-vo passwords:'))

# res = {
#     f(choices(ascii_letters, k = 15), choices(digits, k = 6), choices(symbols, k = 2))
#     for f in repeat(lambda x, y, z: ''.join(set(x + y + z)), q_pass)
# }

# print(res)
# print(f'Quantity of password: {len(res)}')

# from statistics import mean

# avg = mean(len(x)for x in res)
# print(f'Average len of passwords: {avg}')

