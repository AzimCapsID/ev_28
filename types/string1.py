# name = 'john' 
# a = 'john'
# # 
# # 
# # 
# # 
# print(name)
# print(name[2])
# print(a[1], a[-1])

# str1 = 'birthday'

# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# Cрезы п индексам
# [start: end: <step>]
# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])



# text = 'Hello World! My name is John Snow! I \'m King of North!'
# print(text[:13])
# print(text[:])
# print(text[::2])
# print(text[::-1])

# конкатенация строк(соединение)
# a = 'Hello '
# b = 'world'

# print(a + b)


# Экранирование - способ записи символов в строку которые
# невозможно ввести с клавиатуры

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляяция
# \f -> перевод страницы
# \r -> возврат указателя
 
# print('\vHello \tworld! \nMy name is John snow!')

# форматирование строк 
# 1. с помощью %
# 2. с использованием .format()
# 3. Интерполяция строк (преобразование, f-строки)

# % 
# name = input('Vvedite imya: ')
# last_name = input ('Vedite last name: ')
# # print('Добро пж к нам ' + name + ' ' + last_name + '!')
# print('Hello mr %s %s!' %(name, last_name))

# .format
# name = input('Vvedite imya: ')
# last_name = input ('Vedite last name: ')
# print('Приветствую вас, {} {}, в наш клуб!' .format(name, last_name))

# Интерполяция строк
# f- stroki
# a = input('Rust: ')
# name = input('Vvedite imya: ')
# last_name = input ('Vedite last name: ') 
# print(f'Hello {a} {name} {last_name}! Welcome')

text = 'Запомни Питтер, тттт с большой силой приходит и большая ответственность.'
reversed_text = text[::-1]
print(reversed_text)
i = 0 
count_t = 0
len_text = len(reversed_text)
# print(len(reversed_text))
while i < len_text:
    s = reversed_text[i]
    if s == 'т' or s == 'Т':
        count_t += 1
    # print(s)
    i += 1

print(f'В тексте "т" встретилась {count_t} раз!')




















