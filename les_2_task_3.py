'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''

# https://drive.google.com/file/d/1VTc176gEfBTKtljzqgwKHWEsj_oIQFh5/view?usp=sharing

def rev(num, i):
    if num == 0:
        return f'{i}'
    else:
        return f'{rev(num // 10, i * 10 + num % 10)}'

number = int(input('Введите многозначное целое число: '))

outcome = rev(number, 0)

print(f'{outcome}')


