# Decorators
# Scope
# Built in functions


# Декораторы - функция высшего порядка (функция которая принимает другую функцию в качестве аргумента)

# def deco(func):
#     def wrapper():
#         print(f'this function named {func.__name__}')
#         return func()
#     return wrapper



# @deco
# def hello():
#     print('Hello')


# def sq(func):
#     def wrapper(num):
#         nums = func(num)
#         return list(map(lambda x: x ** 2, nums))
#     return wrapper


# @sq
# def func(num: int):
#     return list(range(1, num))

# @sq
# def func2(num):
#     return list(range(1, num, 2))

# # print(func(5))
# print(func2(6))



# size1 = 100
# def second():
#     size2 = 50
#     global size1
#     size1 += size2
#     def third():
#         size3 = 25
#         global size1
#         size1 += size3
#     third()

# second()
# print(size1)



