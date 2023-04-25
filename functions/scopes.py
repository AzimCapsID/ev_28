# область видимости и пространства имен (scopes) - это технология которая определяет 
# контекст имени(переменные) в рамках которого мы можем ее использовать

# built-ins(ввстроенная область видимости) -> print, len, max

# global(глобальная область видимости) -> область одного файла

# enclosed(не локальная либо замкнутая обл видимости, nonlocal)

# local(локальная) -> обл внутри одной функции

x = 200

def my_func():
    print(x)
    a = 300
    print(a)

my_func()
# try:
#     print(a)
# except NameError:
#     print('Нет такого')

print(x)

# a = 10 #global
# print # built-in
# def hello(): #global
#     a = 'HelloWorld' #local
#     print(a, 'local inside in func')

# hello()
# print(a, ' global')


# LEGB - local enclosed global built-in
        # ---->>>>>>>>>>>>>>>>>>>>>>>>>>>

# -----------------------------------------------------------
# Enclosed - 
# замкнутое пространство имен - лоакльное пространство, у которого есть внутреннее(вложенное) локальное пространство

# x = 'global'
# print(x, '1') #global

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3')# local
#     print(x, '2')
#     local()
#     print(x, '4') #enclosed

# enclosed()
# print(x, '5')


# a = 5

# def func():
#     print(a)
#     a = a + 1

# func()

# global -> позволяет изменять значения глобальной переменной находясь внутри локальной области

# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри локальной области

# var = 100



# def increment(): # LEGB
#     global var 
#     var += 1 # var = var + 1

# print(var)
# increment()
# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)


# def counter():
#     num = 0 
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_wash = counter() # <function counter.<locals>.increment at 0x7f1eb2d8e050>
# c_ask = counter()

# print(c_wash()) # 1
# print(c_wash()) # 2
# print(c_wash()) # 3
# print(c_wash()) # 4 
# print(c_wash()) # 5
# print(c_ask())
# print(c_wash())

# def func():
#     pass

# a = func

# print(dir(__builtins__))
# print(len(dir(__builtins__)))




# globals - func которая возвращает все имена внутри глобальной области видимости

# locals - функция которая возвращает все имена внутри  глобальной области видимости и локальной


def counter():
    num = 0 
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes, mobs):
    print()
    print(f'John Snow  ты убил: \nгероев:{heroes}  \nмобов:{mobs}')
    print()

counter_hero = counter()
counter_mobs = counter()
hero = 0
mobs = 0

print('Приветствую вас, Король Севере John Snow, в Вестеросе!')

while True:
    print('Тебе доступны следующие действия:')
    print('1.Убить героя, 2.Убить моба 3.Посмотреть статистику 4.Выйти из игры')
    choice = input('Введите что хотите сделать: ').strip()
    if choice == '1':
        hero = counter_hero()
        print('Вы обезглавели Ланистера!')
    elif choice == '2':
        mobs = counter_mobs()
        print('Вы убили белого ходака')
    elif choice == '3':
        showStats(hero, mobs)
    elif choice == '4':
        print('Пока Пока! Ждем еще раз!')
        break
    

    









