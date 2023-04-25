# ОБработка исключений
# операторы try .. except

# Errors -> связаны кодом 
    # SyntaxError
    # IndentationError
    # TabError

# Исключения exceptions -> связаны с неправильным данными которые передаются в код
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # BaseException -> прородитель всех исключений


# try:
#     a = int(input('enter the number:'))
# except:
#     print('Неправильные данные')
# else:
#     print(a * 5)

# try:
#     <body> если есть ошибка
# except:
#     <body> если нет ошибки
# else:
#     <body> если нет ошибки
# finally:
#     <body> сработает в любом случае

# ls = ['John Snow', 'Snow', 'Tirion']
# print(ls)

# try:
#     i = int(input('Vvvedite index:'))
#     print(ls[i])

# # except (ValueError, IndexError):
# #     print('ЧТо то пошло не так!')

# except ValueError:
#     print('Вы ввели неправильные данные!')
# except IndexError:
#     print('Вы ввели неправильный индекс!')

# -------------------------------------------------------
# Отображение ошибки
# Exception a e (error)

# dict_ = {'1': 'one', '2': 'two','name': 'John'}

# try:
#     key = input('Vvedite key: ')
#     print(dict_[key])
    
# except:
#     print('Opps error')

# dict_ = {'1': 'one', '2': 'two','name': 'John'}


# try:
#     key = input('Vvedite key: ')
#     print(dict_[key])
    
# except Exception as e:
#     print(f'Opps error {e.__class__}')


# try:
#     num1 = int(input('Enter num 1: '))
#     num2 = int(input('Enter num 2: '))
#     result = num1 / num2

# except ValueError:
#     print('Invalid input')

# except ZeroDivisionError:
#     print('Na 0 delit nelzya!')

# else:
#     print(result)

# finally:
#     print('The End!')

