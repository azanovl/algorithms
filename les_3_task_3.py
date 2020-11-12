'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in  range(SIZE)]
print(array)

max_el = 0
min_el = MAX_ITEM

for i in array:
    if max_el < i:
        max_el = i
    elif min_el > i:
        min_el = i

max_pos = array.index(max_el)
min_pos = array.index(min_el)

array[max_pos], array[min_pos] = array[min_pos], array[max_pos]

print(array)
print(f'Максимальный элемент = {max_el}\nМинимальный элемент = {min_el}')



