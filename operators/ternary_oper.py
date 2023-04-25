# sentence = input('vvedite predlojenie: ')

# if sentence[-1] == '?':
#     print('Yes, Vopros')
# else:
#     print('No, normal one!')

# print('Yes, Vopros' if sentence[-1] == '?' else 'No, normal one!')


# ?---------------------------------------------------------------

# Ternary Operators(Тернарные операторы) - это конструкция которая по своему действия  аналогично конструкции if\else,
# но при этом записывается в одну стрoчку

# number = int(input('VVEDITE CHISLO: '))
# res = 'even number' if number % 2 == 0 else 'odd number'
#         # четное                                  нечетное

# print(res)


# <выражение если True> if <условие> else <выражение если False>

# # # ls = [55, 65, 75, 89, 100, 15, 6]

# print(ls)

# choice = input('Vvedite Max/Min: ')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls)


# print(res)

# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('invalid choice')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid choice!'

# print(res)

# ------------------------------------------

flag = True
symbols = '0123456789' + '-' + '.' 

while flag:
    print()
    num1 = input('Введите первое число: ') # 51-r
    is_correct_number = True
    for x in num1:
        if x not in symbols:
            print('Вы вывели неправильное число')
            is_correct_number = False
            break

    if not is_correct_number:
        continue
    # num1 = float(num1) if '.' in num1 else int (num1)

    num2 = input('Введите второе число: ')
    for x in num2:
        if x not in symbols:
            print('Вы вывели неправильное число')
            is_correct_number = False
            break
    
    if not is_correct_number:
        continue
    num1 = float(num1) if '.' in num1 else int (num1)
    num2 = float(num2) if '.' in num2 else int (num2)
    # if ('-' in num1 and num1[0] == '-') or '-' not in num1:
    

    # print(num1, type(num1))
    # print(num2, type(num2))

    operator = input('Введите оператор (+,-,*,/): ').strip()
    
    

    if operator == '+' :
        print(f'Результат: {num1 + num2}')
        print('jf')

    elif operator == '-':
        print(f'Результат: {num1 - num2}')

    elif operator == '*':
        print(f'Результат: {num1 * num2}')

    elif operator == '/':
        if num2 == 0:
            print('На ноль делить нельзя')
        else:
            print(f'Результат: {num1 / num2}')
    
    else:
        print('Вы ввели неверный оператор!')


    choice = input('Хотите продолжить (y/n)?')
    if choice.lower().strip() != 'y':
        flag = False
        print('Пока пока!')







