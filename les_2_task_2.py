'''
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

# https://drive.google.com/file/d/1VTc176gEfBTKtljzqgwKHWEsj_oIQFh5/view?usp=sharing

number = input('Введите многозначное целое число: ')

even_num = 0
odd_num = 0

for i in number:
    if int(i) % 2 == 0 or int(i) == 0:
        even_num += 1
    else:
        odd_num += 1

print(f'В числе {number} количество:\n'
      f'четных чисел    - {even_num}\n'
      f'нечетных чисел  - {odd_num}.')