# num1 = 1
# while num1 >= 0:
#     num1 = input('vvedite chislo: ')
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('встретилось отриц число!')

# -----------------------------------------
# from random import randint

# ls = []
# for x in range(0,100):
#     ls.append(randint(0, 100))

# ls.sort()

# print(ls, len(ls))

# res = []
# for x in ls:
#     if x not in res:
#         print(x)
#         res.append(x)
# print(res, len(res))
# --------------------------------------------------

# x1 = int(input('1 coor: '))
# y1 = int(input('2 coor: '))
# ladya = [x1, y1]

# x2 = int(input('1 coor: '))
# y2 = int(input('2 coor: '))
# target = [x2, y2]

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)
    
# ----------------------------------------------

# from random import choice

# ls = ['Plov', 'BeshBarmak', 'Kuurdak', 'Oromo', 'Lagman']
# # print(choice(ls))
# p = 0 
# b = 0
# k = 0
# o = 0 
# l = 0

# for x in range(0, 1000000):
#     meal = choice(ls)
#     # print(meal)
#     if meal.lower() == 'plov':
#         p += 1
#     elif meal.lower() == 'beshbarmak':
#         b += 1
#     elif meal.lower() == 'kuurdak':
#         k += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     else:
#         l +=1 
# print('Результаты голодных игр: ')
# print(f'Plov: {p} \nBeshbarmak: {b} \nKuurdak:{k} \nOromo:{o} \nLagman:{l}')

# -----------------------------------------------------

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [4,11,2,5,1,6]
target = 8


for i in range(0, len(nums)):
 
    num = target - nums[i]
    if num in nums:
        if num != nums[i]:
            print(f'otvet: {i} {nums.index(num)}')
            break



