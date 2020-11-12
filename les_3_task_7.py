'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 7

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in  range(SIZE)]
print(array)

i, k = 0, 0
min_el_0, min_el_1 = MAX_ITEM, MAX_ITEM

while i < len(array):
    if min_el_0 > array[i]:
        min_el_0 = array[i]
    i += 1

while k < len(array):
    if k != array.index(min_el_0):
        if min_el_1 > array[k]:
            min_el_1 = array[k]
    k += 1

print(f'{min_el_0 = }\n{min_el_1 = }')

exit = input()
