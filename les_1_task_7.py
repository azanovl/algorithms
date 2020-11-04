# https://drive.google.com/file/d/14qNm64W6adDGt68CtxS0MOHLBA9Ze8lo/view?usp=sharing

a = int(input('Введите длину стороны a треуголника abc: '))
b = int(input('Введите длину стороны b треуголника abc: '))
c = int(input('Введите длину стороны c треуголника abc: '))

if a + b > c and b + c > a and a + c > b:
    if a != b and b != c and a != c:
        print('Такой треугольник существует и является разносторонним!')
    elif a == b and b == c and a == c:
        print('Такой треугольник существует и является равносторонним!')
    else:
        print('Такой треугольник существует и является равнобедренным!')
else:
    print('Такого треугольника сущестовать не может!')



