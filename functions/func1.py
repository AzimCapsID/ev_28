# найти квадрат, куб, результат деления на 100
# num1 = 5 
# -> {'num': 5, '2': 25, '3': 125, '100': 0.05}

# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31

# def operations(num):
#     print({'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)


# print({'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100})
# print({'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100})
# print({'num': num4, '2': num4 ** 2, '3': num4 ** 3, '100': num4 / 100})
# print({'num': num5, '2': num5 ** 2, '3': num5 ** 3, '100': num5 / 100})

# DRY - dont repeat yourself

# ------------------------------------------------------------------

# функция это именнованная часть программы которая содержит всебе определенный набор инструкция, и может вызыватся других частях программы
# столько раз сколько угодно при помощи его названия

# def name_of_func(<a, b> #параметры):
    # <body> # код, какая то логика которая будет давать конечный результат
    # <return> оператор который помогает вернуть результат

# {1: 'one'}.items()

# name_of_func(5, 6 #аргументы)

# пареметры функции - это переменные которые будут принимать данные от пользователя и хранить в себе эти данные

# аргументы функции- данные которые мы передаем в функцию, в моменте вызова
                 

# print(len('str'))

# ls = [1,2,3,4,5]
# str1 = 'hello world s vami Kani i John Snow!'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f'result: {i}')

# our_len(str1)
# our_len(ls)

# def isEven(obj):
#     # if obj % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return True if obj % 2 == 0 else False
# res = isEven(6)
# print(res)       
# print(isEven(5))

# isEven()

# def isEven(num: int) -> bool:
#     '''Our function returns True or False while checking number for even number'''
#     return True if num % 2 == 0 else False

# print(isEven(5))



# def get_polin(words):
#     if words == words.reverse():
        
#         print(words)
#         return True
#     else:
#         return False
# ls = ['lalal', 'Hello', 'apa', 'radar']
# # get_polin(ls)

# def get_polin(ls):
#     res = []
#     for word in ls:
#         if word.lower() == word[::-1].lower():
#             res.append(word)
#     return res

# pol = get_polin(ls)
# print(pol)

# def get_percenage(money, period):
#     if money < 30000:
#         raise ValueError('Вложить можно более 30000')
#     if period < 3:
#         raise ValueError('Период должен быть не менее 3 лет')
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
    
#     return money
# try:
#     money = float(input('Введите сумму вложеня: '))
#     period = int(input('Введите период: '))
#     print(get_percenage(money, period))

# except ValueError:
#     print('Неправильный ввод!!')


# def test_func(a = 1,b = 4):
#     pass
# test_func(1,4)

# def range(stop, start = 0, step = 1):
#     pass
# range(4, 3, step = 2)








