# Case-study #3
# Developers:
#

kt = int(input('Укажите котегорию налогоплатильщика:'))

MAX_MONTH = 12


def f_1():
    amount = 0
    nal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('Годовой доход:'))
        amount += value
    # Налог если доход < 9075
    if amount <= 9075:
        nal = (amount / 10)
    # Налог если доход < 36900
    elif 36901 > amount > 9075:
        nal = ((((amount - 9075) / 100) * 15) + (9075 / 100) * 10)
        # Налог если доход > 36900
    else:
        nal = ((((amount - 36900) / 100) * 25) + (((36900 - 9075) / 100) * 15) + (9075 / 100) * 10)
    print(amount, nal)
    return amount


def f_2():
    amount = 0
    nal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('Годовой доход:'))
        amount += value
    # Налог если доход < 18150
    if amount <= 18150:
        nal = (amount / 10)
    # Налог если доход < 73800
    elif 73801 > amount > 18150:
        nal = ((((amount - 18150) / 100) * 15) + (18150 / 100) * 10)
        # Налог если доход > 73800
    else:
        nal = ((((amount - 73800) / 100) * 25) + (((73800 - 18150) / 100) * 15) + (18150 / 100) * 10)
    print(amount, nal)
    return amount


def f_3():
    amount = 0
    nal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('Годовой доход:'))
        amount += value
    # Налог если доход < 12950
    if amount <= 12950:
        nal = (amount / 10)
    # Налог если доход < 49400
    elif 49401 > amount > 12950:
        nal = ((((amount - 12950) / 100) * 15) + (12950 / 100) * 10)
        # Налог если доход > 49400
    else:
        nal = ((((amount - 49400) / 100) * 25) + (((49400 - 12950) / 100) * 15) + (12950 / 100) * 10)
    print(amount, nal)
    return amount


if kt == 1:
    f_1()
elif kt == 2:
    f_2()
elif kt == 3:
    f_3()
else:
    print('Такой котегории нет')