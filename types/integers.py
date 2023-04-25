# Типы данных числа -> int, float

# = -> оператор присваивания
# variable (переменная)
# num=5
# print(num) # 5
# num = 79 # переопределение
# print(num)


# abc -> нижний регистр
# ABC -> верхний регистр

# PEP8
# tomorrow_day = '10.03.23' # snake case
# tomorrowDay = '10.03.23' # camel case

# - + 
# num1 = 5 
# num2 = 13

# result = (num1 + num2)
# print('Summa:', result)

# -

# num1 = input('enter the num1: ') # -> '5'
# num2 = input('enter the num2: ') # -> '7'
# num1 = int(num1)
# num2 = int(num2)

# print(num1, '-', num2, '=', num1 - num2)

# *
# num1 = int(input('Enter the num1'))
# num2 = int(input('Enter the num2'))

# print(num1, '*', num2, '=', num1 * num2)

# /

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульная деление (получение остатка от деления)

# num1 = 2.9
# num2 = 3

# print('/', num1 / num2)
# print('//', num1 // num2)
# print('%', num1 % num2)

# ** -> возведение в степень

# print( 5 ** 2)
# print( 16 ** 55)

# print( 5 ** 0.5) квадратный корень

# pow - возведение в степень
# pow( num1, num2, <mod>)
# num1 = 5 
# num2 =  10
# print(pow(num1, num2))
# print( 5 ** 10 % 65)

# a = 5 
# b = 2
# res =pow(a, b, 12)
# print(res)


# round() - округления числа  с плавающей точкой

# a = 5.368232

# print (round(a, 2))

# abs() - абсолютное значение числа -> abs (-5) ->
                                        # |-5| -> 5
# a = abs(-16)
# b = abs (15)
# print(a, b)


# divmod(a, b) -> она выводит два числа, первое число это результат 
# целочисленного деления а на б, а второе это модульное деление(%)

# res = divmod(5, 2)
# print(res)
# print((5 // 2, 5 % 2))

# import math

# a = 5 
# print(round(math.sqrt(a), 2))

# res = math.sqrt(a)
# print(round(res, 2))

# множественное присваивание
# оператор присваивания(=)

# a = 5 
# b = 15
# c = None

# print('a:', a, 'b:', b)

# # c = a
# # a = b
# # b = c

# a, b = b, a
#     #15, #5   

# print('a:', a, 'b:', b)

# num1, num2, num3 = input('Num1'), input('Num2'), input('Num3')

# print(num1)
# print(num2)
# print(num3)

# from math import pi

# print(pi, type(pi))

# r = int(input('vvod: '))
# res_P = 2 * r * pi
# res_S = pi * r ** 2
# print('S okruzhnosti: ', round(res_S, 2))
# print('P okruzhnosti: ', round(res_P, 2))


from random import randint

# print(randint(700, 1000))

# name = input('vvedite imya : ')
# lastName = input('vvedite svoyu famili :')

# num = randint(1_000_000, 9_999_999)

# print(name, lastName, num)
# print('123' + 'ev.28')
# res = name + lastName + str(num)
# print(res)

# num = randint(1, 10)
# # # print (num)
# i = 0
# while i < 4:
#     guess = int(input('Ugadai chislo: '))
#     if guess == num:
#         print('Ty pobedil! ')
#         break
#     i = i + 1
#     i += 1 # increment
