'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

def total():
    tot_pr = profit_4_ + profit_3_ + profit_2_ + profit_1_
    return tot_pr

Company = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4, total_profit')
x = int(input('Введите количество предприятий: '))
i = 0
company_list = []
for i in range(x):
    name_ = input(f'Введите наименование компании {i + 1}: ')
    profit_1_ = float(input('Прибыль за первый квартал: '))
    profit_2_ = float(input('Прибыль за второй квартал: '))
    profit_3_ = float(input('Прибыль за третий квартал: '))
    profit_4_ = float(input('Прибыль за четвертый квартал: '))
    firm = Company(name_, profit_1_, profit_2_, profit_3_, profit_4_, total())
    company_list.append(firm)

sum_profit = 0
for i in range(len(company_list)):
    sum_profit += company_list[i].total_profit
av_profit = sum_profit / len(company_list)

list_over = []
list_under = []
for i in range(len(company_list)):
    if company_list[i].total_profit > av_profit:
        list_over.append(company_list[i].name)
    elif company_list[i].total_profit < av_profit:
        list_under.append(company_list[i].name)

print(f'Предприятия, чья прибыль выше среднего: {list_over}:\n'
      f'Предприятия, чья прибыль ниже среднего: {list_under}')