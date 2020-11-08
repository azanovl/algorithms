'''
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
'''

# https://drive.google.com/file/d/1VTc176gEfBTKtljzqgwKHWEsj_oIQFh5/view?usp=sharing

import random
rnd_num = int(random.random() * 100)

count = 1
count_max = 10

while count < count_max + 1:
    try_num = int(input(f'Попытка {count} из {count_max}\n'
                    f'Попытайтесь угадать число от 0 до 100, Ваш вариант: '))
    count += 1
    if rnd_num < try_num and count <= count_max:
        print(f'Меньше')
    elif rnd_num > try_num and count <= count_max:
        print(f'Больше')
    elif rnd_num == try_num:
        print(f'Вы угадали. Загаданное число {rnd_num}!')
        break

if try_num != rnd_num:
    print(f'Вы не угадали. Загаданное число {rnd_num}.')

