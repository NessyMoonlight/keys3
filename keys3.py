# Case-study #3
# Developers:
#

taxpayer_category = int(input('Укажите котегорию налогоплатильщика:'))

MAX_MONTH = 1


def f_1():
    amount = 0
    nal = 0
    beznal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('месечный доход доход:'))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input('месечный доход без налога:'))
        beznal += value
    bezamount = amount - beznal  # годовой доход неучитываемый налогом
    # Налог если доход < 9075
    if bezamount <= 9075:
        nal = (bezamount / 10)
    # Налог если доход < 36900
    elif 36901 > bezamount > 9075:
        nal = ((((bezamount - 9075) / 100) * 15) + (9075 / 100) * 10)
        # Налог если доход > 36900
    else:
        nal = ((((bezamount - 36900) / 100) * 25) + (((36900 - 9075) / 100) * 15) + (9075 / 100) * 10)
    print(beznal, bezamount, nal, nal / 12)
    return amount, beznal


def f_2():
    amount = 0
    nal = 0
    beznal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('Годовой доход:'))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input('месечный доход без налога:'))
        beznal += value
    bezamount = amount - beznal  # годовой доход неучитываемый налогом
    # Налог если доход < 18150
    if bezamount <= 18150:
        nal = (bezamount / 10)
    # Налог если доход < 73800
    elif 73801 > bezamount > 18150:
        nal = ((((bezamount - 18150) / 100) * 15) + (18150 / 100) * 10)
        # Налог если доход > 73800
    else:
        nal = ((((bezamount - 73800) / 100) * 25) + (((73800 - 18150) / 100) * 15) + (18150 / 100) * 10)
    print(beznal, bezamount, nal, nal / 12)
    return amount, beznal


def f_3():
    amount = 0
    nal = 0
    beznal = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input('Годовой доход:'))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input('месечный доход без налога:'))
        beznal += value
    bezamount = amount - beznal  # годовой доход неучитываемый налогом
    # Налог если доход < 12950
    if bezamount <= 12950:
        nal = (bezamount / 10)
    # Налог если доход < 49400
    elif 49401 > bezamount > 12950:
        nal = ((((bezamount - 12950) / 100) * 15) + (12950 / 100) * 10)
        # Налог если доход > 49400
    else:
        nal = ((((bezamount - 49400) / 100) * 25) + (((49400 - 12950) / 100) * 15) + (12950 / 100) * 10)
    print(beznal, bezamount, nal, nal / 12)
    return amount, beznal


if taxpayer_category == 1:
    f_1()
elif taxpayer_category == 2:
    f_2()
elif taxpayer_category == 3:
    f_3()
else:
    print('Такой котегории нет')
