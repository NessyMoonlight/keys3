# Case-study #3
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

import ru_local as ru

taxpayer_category = int(input(ru.TAXPAYER_CATEGORY))

nl = '\n'

MAX_MONTH = 12


def one_person():
    amount = 0
    tax = 0
    free_tax = 0
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    tax_amount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 9075
    if tax_amount <= 9075:
        tax = (tax_amount * 0.1)
    # Налог если доход < 36900
    elif 9075 < tax_amount < 36901:
        tax = (((tax_amount - 9075) * 0.15) + (9075 * 0.1))
    elif 36901 <= tax_amount < 89351:
        tax = (((tax_amount - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9075 * 0.1))
    elif 89351 <= tax_amount < 186351:
        tax = (((tax_amount - 89351) * 0.28) + ((89351 - 36901) * 0.25) + ((36901-9075) * 0.15) + (9075 * 0.1))
    elif 186351 <= tax_amount < 405101:
        tax = (((tax_amount - 186351) * 0.33) + ((186351 - 89351) * 0.28) + ((89351 - 36901) * 0.25) +
               ((36901 - 9075) * 0.15) + (9075 * 0.1))
    elif 405101 <= tax_amount < 406751:
        tax = (((tax_amount - 405101) * 0.35) + ((405101 - 186351) * 0.33) + ((186351 - 89351) * 0.28) +
               ((89351 - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9075 * 0.1))
    else:
        tax = (((tax_amount - 406751) * 0.396) + ((406751 - 405101) * 0.35) + ((405101 - 186351) * 0.33) +
               ((186351 - 89351) * 0.28) + ((89351 - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9075 * 0.1))
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {tax_amount} {nl} '
          f'{ru.ANNUAL_TAX} {tax} {nl} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


def married_couple():
    amount = 0
    tax = 0
    free_tax = 0
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    tax_amount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 18150
    if tax_amount <= 18150:
        tax = (tax_amount / 10)
    # Налог если доход < 73800
    elif 73801 > tax_amount > 18150:
        tax = ((((tax_amount - 18150) / 100) * 15) + (18150 / 100) * 10)
        # Налог если доход > 73800
    else:
        tax = ((((tax_amount - 73800) / 100) * 25) + (((73800 - 18150) / 100) * 15) + (18150 / 100) * 10)
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {tax_amount} {nl} '
          f'{ru.ANNUAL_TAX} {tax} {nl} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


def one_parent():
    amount = 0
    tax = 0
    free_tax = 0
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    # Годовой доход
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    tax_amount = amount - free_tax  # годовой доход неучитываемый налогом
    # Налог если доход < 12950
    if tax_amount <= 12950:
        tax = (tax_amount / 10)
    # Налог если доход < 49400
    elif 49401 > tax_amount > 12950:
        tax = ((((tax_amount - 12950) / 100) * 15) + (12950 / 100) * 10)
        # Налог если доход > 49400
    else:
        tax = ((((tax_amount - 49400) / 100) * 25) + (((49400 - 12950) / 100) * 15) + (12950 / 100) * 10)
    print(f'{ru.TAX_FREE_INCOME} {free_tax} {nl} {ru.TAX_INCOME} {tax_amount} {nl} '
          f'{ru.ANNUAL_TAX} {tax} {ru.MONTHLY_TAX} {tax/12}')
    return amount, free_tax


if taxpayer_category == 1:
    one_person()
elif taxpayer_category == 2:
    married_couple()
elif taxpayer_category == 3:
    one_parent()
else:
    print(ru.NO_CATEGORY)
