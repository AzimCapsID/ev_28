# dict_ = {'Murat' : 24, 'Erjan': 21, 'Karina': 24, 'Altynai': 19, 'Aibek' : 16}

# for i in dict.keys():
#     if dict_ [i] >= 17:
#         print(f'{i} You can come in')
#     else:
#         print(f'{i} You cant come in')


# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# # keys -> 'a'
# b = {}
# # for inner_dict in a.values(): # a['a'] -> i => {'e' : 32}
# #     print(inner_dict)
# #     for key, value in inner_dict.items(): # i ['e']
# #         print(value)

# for i, j in a.items():
#     for i_in, j_in in j.items():
#         b[i] = j_in 
# print(b)


# fruit = {'orange': 230, 'apple': 247, 'banana': 120}
# # for i in fruit.copy():
# #     print(fruit[i])
# #     if fruit[i]%2 != 0: #dict['key'] = value
# #         fruit.pop(i)

# # print(fruit)

# for i, j in fruit.copy().items():
#     if j% 2 == 0:
#         fruit.pop(i)
# print(fruit)


# dct = {1:23, 2:34, 3:43, 4:25}
# total = 0 
# for i in dct.values():
#     total += i
# print(total)

# dct = {}
# for i in range(1,10):
#     dct[i] = i ** 2
# print(dct)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}

# s  = {}

# for key, value in my_dict.items():
#     for i_v in value.values():
#         s[key] = i_v
# print(s)

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sortef = sorted(dict_.values()) # -> список всех значений
# print(sortef)
# # [0,1,2,3,4]
# sorted_dict = {}
# for i in sortef: # 0 
#     for key, value in dict_.items: # 2 4
#         if value == i:
#             sorted_dict[key] = value
#             break

# print(sorted_dict)



# num = int(input('Enter the amount: '))
# if  num < 0:
#     print('CСумма н еможет быть отрицательной')

# task 26 lists
# res = []
# size = 3 
# for i in range (1, 4):
#     grid = []
#     for j in range(1,4):
#         grid.append(j)
#     res.append(grid)
# print(res)

# x = int(input()) 
# y = int(input()) 
# if x % y == 0: 
#     print('x делится на y') 
#     d = x//y 
#     print(f'Частное: {d}') 
# else: 
#     print('x не делится на y') 
#     a = x // y 
#     print(f'Частное: {a}') 
#     b = x % y 
#     print(f'Остаток: {b}')



# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# a = range(1, 10)
# print(a)
# if x2 == y2 or x1 > x2 and y1 < y2 or x1 < x2 and y1 > y2:
#     print('YES')
# elif x1 not in a or y1 not in a or x2 not in a or y2 not in a:
#     print('NO')
# else:
#     print('NO')
# i = list(range(0,10))
# print(i)
# a =reversed(i)
# print(a)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# numbers2 = list(numbers)
# print(numbers2)

# n = input().split(',')
# list_ = []
# for i in n:
#     list_.append(list(i))
#     list_.sort()
# print(list_)

