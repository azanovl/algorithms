'''
    Hаписать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
вычислений. Завершение программы должно выполняться при вводе символа '0'в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак
операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
'''

# https://drive.google.com/file/d/1VTc176gEfBTKtljzqgwKHWEsj_oIQFh5/view?usp=sharing

while True:
    op_sign = input('Введите знак операции +, -, *, или /. Введите "0" для выхода из программы. ')
    if op_sign == 0:
        break
    elif op_sign in '+-*/':
        first_num = float(input('Введите первое число: '))
        second_num = float(input('Введите второе число: '))
    else:
        print('Введено неверное значение знака операции. Повторите запрос!')
        continue


    if op_sign == '+':
        result = first_num + second_num
    elif op_sign == '-':
        result = first_num - second_num
    elif op_sign == '*':
        result = first_num * second_num
    elif second_num == 0:
        print('На ноль делить нельзя. Повторите ввод значений!')
        continue
    else:
        result = first_num / second_num

    print(result)




