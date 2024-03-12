# Case-study #3
# Developers:
#

import ru_local as ru

taxpayer_category = int(input(ru.TAXPAYER_CATEGORY))

nl = '\n'

MAX_MONTH = 12


def f_1():
    amount = 0
    tax = 0
    free_tax = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.ANNUAL_INCOME_VALUE} {ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE_AMOUNT} {ru.TAX} {ru.NAME[month]} [USD]: '))
        free_tax += value
    bezamount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 9075
    if bezamount <= 9075:
        tax = (bezamount / 10)
    # Налог если доход < 36900
    elif 36901 > bezamount > 9075:
        tax = ((((bezamount - 9075) / 100) * 15) + (9075 / 100) * 10)
        # Налог если доход > 36900
    else:
        tax = ((((bezamount - 36900) / 100) * 25) + (((36900 - 9075) / 100) * 15) + (9075 / 100) * 10)
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {bezamount} {nl} {ru.ANNUAL_TAX} {tax} {nl} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


def f_2():
    amount = 0
    tax = 0
    free_tax = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.ANNUAL_INCOME_VALUE} {ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE_AMOUNT} {ru.TAX} {ru.NAME[month]} [USD]: '))
        free_tax += value
    bezamount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 18150
    if bezamount <= 18150:
        tax = (bezamount / 10)
    # Налог если доход < 73800
    elif 73801 > bezamount > 18150:
        tax = ((((bezamount - 18150) / 100) * 15) + (18150 / 100) * 10)
        # Налог если доход > 73800
    else:
        tax = ((((bezamount - 73800) / 100) * 25) + (((73800 - 18150) / 100) * 15) + (18150 / 100) * 10)
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {bezamount} {nl} {ru.ANNUAL_TAX} {tax} {nl} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


def f_3():
    amount = 0
    tax = 0
    free_tax = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.ANNUAL_INCOME_VALUE} {ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE_AMOUNT} {ru.TAX} {ru.NAME[month]} [USD]: '))
        free_tax += value
    bezamount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 12950
    if bezamount <= 12950:
        tax = (bezamount / 10)
    # Налог если доход < 49400
    elif 49401 > bezamount > 12950:
        tax = ((((bezamount - 12950) / 100) * 15) + (12950 / 100) * 10)
        # Налог если доход > 494000
    else:
        tax = ((((bezamount - 49400) / 100) * 25) + (((49400 - 12950) / 100) * 15) + (12950 / 100) * 10)
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {bezamount} {nl} {ru.ANNUAL_TAX} {tax} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


if taxpayer_category == 1:
    f_1()
elif taxpayer_category == 2:
    f_2()
elif taxpayer_category == 3:
    f_3()
else:
    print(ru.NO_CATEGORY)
