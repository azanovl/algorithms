'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in  range(SIZE)]
print(array)

i = 0
max_el = 0
min_el = MAX_ITEM

while i < len(array):
    if max_el < array[i]:
        max_el = array[i]
    elif min_el > array[i]:
        min_el = array[i]
    i += 1

max_pos = array.index(max_el)
min_pos = array.index(min_el)

sum_ = 0
if max_pos > min_pos and max_pos - min_pos > 1:
    pos = min_pos + 1
    while pos < max_pos:
        sum_ += array[pos]
        pos += 1
elif max_pos < min_pos and abs(max_pos - min_pos) > 1:
    pos = max_pos + 1
    while pos < min_pos:
        sum_ += array[pos]
        pos += 1
else:
    sum_ = None

print(f'Максимальный элемент = \t{max_el}\nМинимальные элемент = \t{min_el}')
print(f'Сумма элементов между макисмальным и минимальным, не включая их самих = {sum_}')