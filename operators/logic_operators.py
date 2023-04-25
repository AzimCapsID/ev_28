#операторы сравнения
# Условные операторы и логические операторы

# операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 5 -> True
# 7 > 9 -> False

# условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает если в condition if приедет true
# [elif] <condition>:
#     <body elif>
# [else]:
#     <body else>: #сработает если во всех выше стоящих условиях пришло False

# string = input('enter smt: ')

# if string.lower == 'hello': 
#     print('Hello, it\'s me \n was wondering if after all these years you\d like to meet')
# elif string.lower == 'john':
#     print('welcome back John Snow')
# elif string.lower == 'abra':
#     print('kadabra')
# else:
#     print('совпадений не найдено')

# print('Registration Form!')
# email = input('enter email:')
# password = input('Enter the password:')
# if len(password) < 8:
#     raise ValueError('Password is too short! \n Need to be 8 symbols or more!')
#     print('Password too short!')
# elif password.isdigit():
#     raise ValueError('Password is invalid!\n Password must vontain symbols too!')
# elif password.isalpha():
#     raise ValueError('Password invalid@\n Password must contain number or special symbols too!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#     raise ValueError('Password did not much')

# print(f'successfully registered! Hello Mr\Mrs {email}!')

# age = input('Enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year')
# else: 
#     print('you can pass! Welcome to KZ!')

# and - логическое и 
# or - лог или
# not - лог отрицание

# money = 100_000_000
# status = 'base'

# if money < 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re ministr of our club')
# else:
#     print('You\'re honorable membeer of our club')


# str1 = 'Hello World!'
# print(str1)
# symbol = input('Enter the symbol: ')

# # if symbol not in str1:
# #     print(f'The symbol: {symbol} does not exists!')
# # else: 
# #     print(f'The symbol: {symbol} exists')


# if symbol in str1:
#     print(f'The symbol: {symbol} exists')
# else: 
#     print(f'The symbol: {symbol} does not exists!')


# разрешаем доступ если он юзер гита или гугл  и его возраст больше 21 или у него деньги(10000)

# user = 'john'
# is_google_user = False
# is_git_user = True
# age = 19
# user_coins = 9000

# if (is_git_user or is_google_user) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system Mr\Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')

# string = 'Haelo'
# print(string[-2:])

# string = 'hello'
# print (string[-1] + string[1:-1] + string[0])

# a = 332.22212
# print(round(a(2)))








