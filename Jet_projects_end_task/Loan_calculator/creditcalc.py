from math import log, ceil, floor
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=['diff', 'annuity'], help="You need to choose only one argument from the list.")
parser.add_argument("--principal", help="You need to choose principal.", type=int)
parser.add_argument("--periods", help="You need to choose only one ingredient from the list.", type=int)
parser.add_argument("--interest", help="You need to choose interest.", type=float)
parser.add_argument("--payment", help="You need to choose only one ingredient from the list.", type=int)


args = parser.parse_args()

if args.type == 'diff':
    if args.principal is None or args.periods is None or args.interest is None or args.payment is not None:
        print("Incorrect parameters.")
        # print(principal, payment, loan_interest)
        exit()
    principal = args.principal
    number_of_months = args.periods
    loan_interest = args.interest  # 10 -
    nominal_interest = (loan_interest * 0.01) / 12  # i
    overpaiment = 0
    for m in range(1, number_of_months + 1):
        diff_payment = principal / number_of_months + nominal_interest * (
                    principal - (principal * (m - 1)) / number_of_months)
        overpaiment += ceil(diff_payment)
        print("Month {0}: payment is {1}".format(m, ceil(diff_payment)))
    print("Overpayment = {}".format(overpaiment - principal))

elif args.type == 'annuity':  # a
    if args.payment == None:
        principal = args.principal  # 1000000 - p
        number_of_months = args.periods  # 60 - n
        loan_interest = args.interest  # 10 -
        nominal_interest = (loan_interest * 0.01) / 12  # i
        a = nominal_interest * (1 + nominal_interest) ** number_of_months
        b = (1 + nominal_interest) ** number_of_months - 1
        annuity_ord = principal * (a / b)
        overpaiment = 0
        for m in range(1, number_of_months + 1):
            overpaiment += ceil(annuity_ord)
        print("Your annuity payment = {0}!".format(ceil(annuity_ord)))
        print("Overpayment = {}".format(overpaiment - principal))

    elif args.principal == None:
        if args.payment is None or args.periods is None or args.interest is None:
            print("Incorrect parameters.")
            exit()
        annuity_ord = args.payment  # - A
        number_of_months = args.periods
        loan_interest = args.interest
        nominal_interest = (loan_interest * 0.01) / 12
        a = nominal_interest * (1 + nominal_interest) ** number_of_months
        b = (1 + nominal_interest) ** number_of_months - 1
        loan_principal = annuity_ord / (a / b)
        overpaiment = 0
        for m in range(1, number_of_months + 1):
            overpaiment += ceil(annuity_ord)
        print("Your loan principal = {0}!".format(floor(loan_principal)))
        print("Overpayment = {}".format(overpaiment - ceil(loan_principal)))

    elif args.periods == None:
        if args.principal is None or args.payment is None or args.interest is None:
            print("Incorrect parameters.")
            exit()
        principal = args.principal  # 1000000 - p
        payment = args.payment  # 15000
        loan_interest = args.interest  # 10 a
        if args.principal is None or args.payment is None or args.interest is None:
            print("Incorrect parameters.")
            exit()

        nominal_interest = (loan_interest * 0.01) / (12 * 1)
        number_of_months = ceil(log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))  # n
        overpaiment = 0
        for m in range(1, number_of_months + 1):
            overpaiment += ceil(payment)

        # вычислить сколько лет и месяцев
        years = int(number_of_months / 12)
        months = number_of_months % 12
        if years == 0:
            print("It will take", months, "months to repay this loan!")
        elif months == 0 or months == 12:
            print("It will take", years, "years to repay this loan!")
        else:
            print("It will take", years, "years and", months, "months to repay this loan!")

        print("Overpayment = {}".format(overpaiment - principal))

    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters1")

