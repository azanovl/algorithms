# https://drive.google.com/file/d/14qNm64W6adDGt68CtxS0MOHLBA9Ze8lo/view?usp=sharing

num = int(input('Введите номер буквы в алфавите, целое число от 1 до 26: '))

if num not in range(1, 27):
    print('Введено неверное число. Программа завершена!')
else:
    letter = chr(ord('a') - 1 + num)

print(f'В алфавите под номером {num} расположена буква "{letter}".\nПрограмма завершена.')