num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
x = input("Выберите операцию из следующих ('+','-','*','/','%','**','//'): ")
if x == '+' :
    print(f'Ответ: {num1 + num2}')
elif x == '*':
    print(f'Ответ: {num1 * num2}')
elif x == '/':
    print(f'Ответ: {num1 / num2}')
elif x == '-':
    print(f'Ответ: {num1 - num2}')
elif x == '//':
    print(f'Ответ: {num1 // num2}')
elif x == '%':
    print(f'Ответ: {num1 % num2}')
elif x == '**':
    print(f'Ответ: {num1 ** num2}')
else:
    print('Данной операции нет в системе')
