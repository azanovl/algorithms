'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
'''

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in  range(SIZE)]
print(array)

max_negative = MIN_ITEM

for i in array:
    if i < 0 and i > max_negative:
        max_negative = i

print(f'Макисмальный отрицательный элемент = {max_negative}\nЕго позиция в списке: {array.index(max_negative)}')