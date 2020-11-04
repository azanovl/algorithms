# https://drive.google.com/file/d/14qNm64W6adDGt68CtxS0MOHLBA9Ze8lo/view?usp=sharing

x = int(input('Введите целое трехначное число: '))

a = abs(x) // 100
b = (abs(x) - 100 * a) // 10
c = (abs(x) - 100 * a) % 10

s = a + b + c
p = a * b * c

print(f'Сумма всех цифр трехзначного числа равна {s}')
print(f'Произведение всех цифр трехзначного числа равна {p}')