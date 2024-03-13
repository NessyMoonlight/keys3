# Case-study #3
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

import ru_local as ru

taxpayer_category = int(input(ru.TAXPAYER_CATEGORY))

MAX_MONTH = 12


def one_person():
    '''
    The function determines the
    amount of tax for one entity.
    '''
    amount = 0
    tax = 0
    free_tax = 0
    nl = '\n'
    # Calculating annual income by month.
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    print(f'{ru.ANNUAL_INCOME} ${amount:.2f}')
    # Calculating of the annual tax-free amount by month.
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    # Annual taxable income.
    tax_amount = amount - free_tax
    # Tax calculation by stages.
    if tax_amount < 9076:
        tax = (tax_amount * 0.1)
    elif 9076 <= tax_amount < 36901:
        tax = (((tax_amount - 9075) * 0.15) + (9075 * 0.1))
    elif 36901 <= tax_amount < 89351:
        tax = (((tax_amount - 36900) * 0.25) + ((36900 - 9075) * 0.15) + (9075 * 0.1))
    elif 89351 <= tax_amount < 186351:
        tax = (((tax_amount - 89350) * 0.28) + ((89350 - 36900) * 0.25) + ((36900-9075) * 0.15) + (9075 * 0.1))
    elif 186351 <= tax_amount < 405101:
        tax = (((tax_amount - 186350) * 0.33) + ((186350 - 89350) * 0.28) + ((89350 - 36900) * 0.25) +
               ((36900 - 9075) * 0.15) + (9075 * 0.1))
    elif 405101 <= tax_amount < 406751:
        tax = (((tax_amount - 405100) * 0.35) + ((405100 - 186350) * 0.33) + ((186350 - 89350) * 0.28) +
               ((89350 - 36900) * 0.25) + ((36900 - 9075) * 0.15) + (9075 * 0.1))
    else:
        tax = (((tax_amount - 406750) * 0.396) + ((406750 - 405100) * 0.35) + ((405100 - 186350) * 0.33) +
               ((186350 - 89350) * 0.28) + ((89350 - 36900) * 0.25) + ((36900 - 9075) * 0.15) + (9075 * 0.1))
    print(f'{ru.TAX_FREE_INCOME} ${free_tax:.2f} {nl} {ru.TAX_INCOME} ${tax_amount:.2f} {nl} '
          f'{ru.ANNUAL_TAX} ${tax:.2f} {nl} {ru.MONTHLY_TAX} ${(tax/12):.2f}')
    return amount, free_tax


def married_couple():
    '''
    The function determines the
    amount of tax for a married couple.
    '''
    amount = 0
    tax = 0
    free_tax = 0
    nl = '\n'
    # Calculating annual income by month.
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    print(f'{ru.ANNUAL_INCOME} ${amount:.2f}')
    # Calculating of the annual tax-free amount by month.
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    # Annual taxable income.
    tax_amount = amount - free_tax
    # Tax calculation by stages.
    if tax_amount < 18151:
        tax = (tax_amount * 0.1)
    elif 18151 <= tax_amount < 73801:
        tax = (((tax_amount - 18150) * 0.15) + (18150 * 0.1))
    elif 73801 <= tax_amount < 148851:
        tax = (((tax_amount - 73800) * 0.25) + ((73800 - 18150) * 0.15) + (18150 * 0.1))
    elif 148851 <= tax_amount < 226851:
        tax = (((tax_amount - 148850) * 0.28) + ((148850 - 73800) * 0.25) + ((73800-18150) * 0.15) + (18150 * 0.1))
    elif 226851 <= tax_amount < 405101:
        tax = (((tax_amount - 226850) * 0.33) + ((226850 - 148850) * 0.28) + ((148850 - 73800) * 0.25) +
               ((73800 - 18150) * 0.15) + (18150 * 0.1))
    elif 405101 <= tax_amount < 457601:
        tax = (((tax_amount - 405100) * 0.35) + ((405100 - 226850) * 0.33) + ((226850 - 148850) * 0.28) +
               ((148850 - 73800) * 0.25) + ((73800 - 18150) * 0.15) + (18150 * 0.1))
    else:
        tax = (((tax_amount - 457600) * 0.396) + ((457600 - 405100) * 0.35) + ((405100 - 226850) * 0.33) +
               ((226850 - 148850) * 0.28) + ((148850 - 73800) * 0.25) + ((73800 - 18150) * 0.15) + (18150 * 0.1))
    print(f'{ru.TAX_FREE_INCOME} ${free_tax:.2f} {nl} {ru.TAX_INCOME} ${tax_amount:.2f} {nl} '
          f'{ru.ANNUAL_TAX} ${tax:.2f} {nl} {ru.MONTHLY_TAX} ${(tax/12):.2f}')
    return amount, free_tax


def one_parent():
    '''
    The function determines the
    amount of tax for one parent.
    '''
    amount = 0
    tax = 0
    free_tax = 0
    nl = '\n'
    # Calculating annual income by month.
    print(ru.ANNUAL_INCOME_VALUE)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    print(f'{ru.ANNUAL_INCOME} ${amount:.2f}')
    # Calculating of the annual tax-free amount by month.
    print(ru.TAX_FREE_AMOUNT)
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TAX_FREE} {ru.NAME[month]} [USD]: '))
        free_tax += value
    # Annual taxable income.
    tax_amount = amount - free_tax
    # Tax calculation by stages.
    if tax_amount < 12951:
        tax = (tax_amount * 0.1)
    elif 12951 <= tax_amount < 49401:
        tax = (((tax_amount - 12950) * 0.15) + (12950 * 0.1))
    elif 49401 <= tax_amount < 127551:
        tax = (((tax_amount - 49400) * 0.25) + ((49400 - 12950) * 0.15) + (12950 * 0.1))
    elif 127551 <= tax_amount < 206601:
        tax = (((tax_amount - 127550) * 0.28) + ((127550 - 49400) * 0.25) + ((49400 - 12950) * 0.15) + (12950 * 0.1))
    elif 206601 <= tax_amount < 405101:
        tax = (((tax_amount - 206600) * 0.33) + ((206600 - 127550) * 0.28) + ((127550 - 49400) * 0.25) +
               ((49400 - 12950) * 0.15) + (12950 * 0.1))
    elif 405101 <= tax_amount < 432201:
        tax = (((tax_amount - 405100) * 0.35) + ((405100 - 206600) * 0.33) + ((206600 - 127550) * 0.28) +
               ((127550 - 49400) * 0.25) + ((49400 - 12950) * 0.15) + (12950 * 0.1))
    else:
        tax = (((tax_amount - 432200) * 0.396) + ((406751 - 405100) * 0.35) + ((405100 - 206600) * 0.33) +
               ((206600 - 127550) * 0.28) + ((127550 - 49400) * 0.25) + ((49400 - 12950) * 0.15) + (12950 * 0.1))
    print(f'{ru.TAX_FREE_INCOME} ${free_tax:.2f} {nl} {ru.TAX_INCOME} ${tax_amount:.2f} {nl} '
          f'{ru.ANNUAL_TAX} ${tax:.2f} {nl} {ru.MONTHLY_TAX} ${(tax / 12):.2f}')
    return amount, free_tax


def main():
    if taxpayer_category == 1:
        one_person()
    elif taxpayer_category == 2:
        married_couple()
    elif taxpayer_category == 3:
        one_parent()
    else:
        print(ru.NO_CATEGORY)


if __name__ == '__main__':
    main()
