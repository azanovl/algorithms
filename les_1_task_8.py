# https://drive.google.com/file/d/14qNm64W6adDGt68CtxS0MOHLBA9Ze8lo/view?usp=sharing

year = int(input('Введите год и узнайте является ли он високосным: '))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f'Год {year} не является високосным!')
    else:
        print(f'Год {year} является високосным!')
else:
    print(f'Год {year} не является високосным!')

