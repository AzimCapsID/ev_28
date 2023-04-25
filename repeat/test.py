# list_ = [range(1,10)]
# ls = [x * x if x / 2 != 0 else x for x in list_ if x % 2 == 0 ]

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

# a = [ x for x in string_ if x.isdecimal()]
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending' 
# list1 = list(string_.split()) 
# # list_ = [x for x in list1 if x.isdigit()] 
# print(list1)

# dict_ = {'key1': 'value1', 'key2': 'value2'} 

# print(dict_.get('key1'))


# list_ = [1, 2, 3, 4]
# for i in range(0, len(list_) + 1):
#     print(list_[i])

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# ls = []

# for i in colors1:
#     if i != colors2:
#         ls.append(i)
#     else:
#         pass
# for i in colors2:
#     if i != colors1:
#         ls.append(i)
#     else:
#         pass
    
# print(ls)


# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
# fetch_webpage()

# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print arg1, arg2
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print "Меня зовут", first_name, last_name
# print_full_name("Питер", "Венкман")

# name = 'Sandy'
# def func_one():
#     name = 'Andy'
#     def func_two():
#         name = 'Mandy'
#         print(name)
#         print(locals())
#     func_two()
# func_one()


# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# ls = []
# for i in list_:
#     if type(i) == int:
#         ls.append(i)
#     elif type(i) == str:
#         if i.isdigit():
#             o = int(i)
#             ls.append(o)
#         else:
#             pass
#     else:
#         pass

# print(sum(ls))

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# a = max(lists)
# b = min(lists)

# print(f'max_list{a}')
# print(f'min_list{b}')


a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
for k, v in a.items():
    if v % 2 == 0:
        v = 2
        print(v)
