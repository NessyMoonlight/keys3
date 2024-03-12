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
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    tax_amount = amount - free_tax
    if tax_amount < 9076:
        tax = (tax_amount * 0.1)
    elif 9076 <= tax_amount < 36901:
        tax = (((tax_amount - 9076) * 0.15) + (9075 * 0.1))
    elif 36901 <= tax_amount < 89351:
        tax = (((tax_amount - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9076 * 0.1))
    elif 89351 <= tax_amount < 186351:
        tax = (((tax_amount - 89351) * 0.28) + ((89351 - 36901) * 0.25) + ((36901-9075) * 0.15) + (9076 * 0.1))
    elif 186351 <= tax_amount < 405101:
        tax = (((tax_amount - 186351) * 0.33) + ((186351 - 89351) * 0.28) + ((89351 - 36901) * 0.25) +
               ((36901 - 9075) * 0.15) + (9076 * 0.1))
    elif 405101 <= tax_amount < 406751:
        tax = (((tax_amount - 405101) * 0.35) + ((405101 - 186351) * 0.33) + ((186351 - 89351) * 0.28) +
               ((89351 - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9076 * 0.1))
    else:
        tax = (((tax_amount - 406751) * 0.396) + ((406751 - 405101) * 0.35) + ((405101 - 186351) * 0.33) +
               ((186351 - 89351) * 0.28) + ((89351 - 36901) * 0.25) + ((36901 - 9075) * 0.15) + (9076 * 0.1))
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
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    tax_amount = amount - free_tax
    if tax_amount < 18151:
        tax = (tax_amount * 0.1)
    elif 18151 <= tax_amount < 73801:
        tax = (((tax_amount - 18151) * 0.15) + (18151 * 0.1))
    elif 73801 <= tax_amount < 148851:
        tax = (((tax_amount - 73801) * 0.25) + ((73801 - 18151) * 0.15) + (18151 * 0.1))
    elif 148851 <= tax_amount < 226851:
        tax = (((tax_amount - 148851) * 0.28) + ((148851 - 73801) * 0.25) + ((73801-18151) * 0.15) + (18151 * 0.1))
    elif 226851 <= tax_amount < 405101:
        tax = (((tax_amount - 226851) * 0.33) + ((226851 - 148851) * 0.28) + ((148851 - 73801) * 0.25) +
               ((73801 - 18151) * 0.15) + (18151 * 0.1))
    elif 405101 <= tax_amount < 457601:
        tax = (((tax_amount - 405101) * 0.35) + ((405101 - 226851) * 0.33) + ((226851 - 148851) * 0.28) +
               ((148851 - 73801) * 0.25) + ((73801 - 18151) * 0.15) + (18151 * 0.1))
    else:
        tax = (((tax_amount - 457601) * 0.396) + ((457601 - 405101) * 0.35) + ((405101 - 226851) * 0.33) +
               ((226851 - 148851) * 0.28) + ((148851 - 73801) * 0.25) + ((73801 - 18151) * 0.15) + (18151 * 0.1))
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
