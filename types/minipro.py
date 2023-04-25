from random import randint
num = randint(1, 10)
num = randint(1, 10)
# # print (num)
i = 0
while i < 4:
    guess = int(input('Ugadai chislo: '))
    if guess == num:
        print('Ty pobedil! ')
        break
    i = i + 1
    i += 1