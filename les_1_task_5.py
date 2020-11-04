# https://drive.google.com/file/d/14qNm64W6adDGt68CtxS0MOHLBA9Ze8lo/view?usp=sharing

f = input('Введите первую букву в диапазоне a..z: ' )
s = input('Введите вторую букву в диапазоне a..z: ' )

f = ord(f)
s = ord(s)

if f and s not in range(97, 123):
    print('Введены неверные данные данные. Программа завершена.')
else:
    start = ord('a')

    pos_f = f - start + 1
    pos_s = s - start + 1
    dist = abs(s - f) - 1


    print(f'Буквы {chr(f)} и {chr(s)} находятся d алфавите на {pos_f} и {pos_s} местах, соответственно.')
    print(f'Количество букв между ними - {dist}.')