# str1 = 'hello world! My name is john, last name is snow. Nice to meet you!'
# def get_revers (text):
#     # print(text[::-1])
#     spisok = text.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)

# print(get_revers(str1))

# def sum_of_args(a, b, c = 5, d = 5): #параметры
#     return a + b + c + d

# res = sum_of_args(1, 2, 3, 4) #аргументы
# print(res)

# result = sum_of_args

# print(result, type(result))

# print(result(5, 6, 7, 8))
# print(sum_of_args(5, 5))

# ---------------------------------------------------------
# позиционные и именнованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# print(printParams(1,4,5))
# print()
# printParams(c = 5, b = 15, a = 10)
# print()
# printParams(a = 20, b = 30, c = 15)


# def sum_of_args(a, b, c , d ): 
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) #argements (позиционные аргументы)

# print(sum_of_args(a=5, c=20, b=10, d=15)) #keyword arguments (именованные аргументы)

# print(sum_of_args(5, 10, d=15, c=20))

# -----------------------------------------------------------
# оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

# *args, **kwargs в функциях

# def printScores(student, *args):
#     print(f'Name of student: {student}')
#     # print(args)
#     print(f'AVG: {sum(args) / len(args)}')
#     for x in args:
#         print('Score:', x)

# printScores('John Snow', 100, 90, 80, 95, 88)


# def printPetNames (owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')
#         print(f'{pet}: {name}')

# printPetNames('john snow', dog='Rex', cat='Garfield', fish = ['Nemo', 'Nori', 'Batya'], turtle='Leo' )

# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры a  и  b:', a, b)
#     print('Аргументы: ', args)
#     print('Именованные аргументы:', kwargs)

# get_some_data(1, 2, 3, 4, 5, lang='python', car='BMW')

# ------------------------------------------------------------

def generate_random_str(len_):
    import string as s
    import random
    symbols = s.ascii_letters + s.digits
    
    # print(s.ascii_letters, s.digits, s.punctuation)
    res = list(
        random.choice(symbols) for i in range(1, len_)
    ) + list(random.choice(s.punctuation))
    random.shuffle(res)
    return ''.join(res)


print(generate_random_str(8))









try :
    num1 = int(input())
    num2 = int(input())
except:
    ValueError