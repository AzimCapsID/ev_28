# lists() -> (списки, массив) -  изменяемый, итерируемый,  последовательный тип данных, который представляет из себя итерируемый
# коллекцию  каких либо обьектов(значения).

# my_list = [1, 'string', False, None, [1,2,3,4,5,6]]

# print(my_list, type(my_list))

# range() - возврашает последовательность элементов (чисел)

# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

# list()
# my_list = list('Hello world')
# print(my_list)

# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_, type(tuple_))

# ls = list(tuple_)
# print(ls, type(ls))

# ИНдексцация в списках 
# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls, len (ls))
# print(ls[1], ls[2])
# print(ls[4:]) # [5, 'string', [True, False, None]]

# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls[6][:2])

# ls = list(range(1, 11))
# print(ls)
# for number in ls:
#     print("hello world")

# ls = ['John', 'Tirion', 'Sansa', 'Jamie']
# print(ls, len(ls))
# for x in ls:
#     print(f'Hello Mr/mrs {x}! Welcome To Hell')
#     print('1')
# print('2')


# ls = list(range(1, 21))

# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'чет,{num**2}')
#     else:
#         print(f'{num}, нечет {num**3}')



#------------------------------------------------------------------------------------------------------]
#методы списков

# print(dir([]))

# append (element) - Добавляет элемент в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True, False])
# print(ls)

# extend(object) - расширает список

# ls = [1, 2, 3]
# ls.append('hello')
# print(ls)
# ls.extend('hello')
# print(ls)

# ls = [1, 2, 3]
# ls1 = [5, 5, 6]
# print(ls + ls1)

# sort() - сортирует список, если передатьь reversw = True,  то список отсортируется в убываещим порядке4

# from random import randint

# ls = []
# for x in range(1, 100):
#     num = randint(0, 1000)
#     ls.append(num)



# print(ls)
# ls.sort(reverse=True)
# print('After: ')
# print(ls)

# ls = ['John', 'Deineris', 'Ai', 'zax']
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element) - добавляет элемент ао указаному индексу

# ls = ['string', 2, 3, False]

# ls.insert(1, {'fr': 12})
# print(ls)

# remove (element) - удаляет element из списка если нет такого то выводиться ошибка
# pop(index) - удаляет и возвратщает элемент из списка по index, но если index не  передать, то удаляет последний элемнет

# ls = [2, 3, 5, 6, 6, 6, 5]
# ls.remove()
# print(ls)
ls = [2, 'makers', ['23', 13], True]
print(ls.index(True))

# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)

# pop 
# ls = [2, 3, 4, 5, 6, 3, 6]
# deleted = ls.pop(0)
# print(ls.remove(4)) #None
# print(ls)
# print(deleted)

# -------------------------------------------------------------------------------
# update
# ls = [1, 'h', '3']
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza: 
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)

# string1 = 'America'
# string2 = 'Japan'
# print(string1[0] + string2[0] + string1[3] + string2[2] + string1[-1] + string2[-1])

# string = '  hello   '
# a = (string.strip())
# print (a, len(a))























