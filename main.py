IntelliJ IDEAPyCharm   
from math import ceil, floor, log
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", default=None)
parser.add_argument("--principal", type=int, default=None)
parser.add_argument("--periods", type=int, default=None)
parser.add_argument("--interest", type=float, default=None)
parser.add_argument("--payment", type=int, default=None)
args = parser.parse_args()

principal, periods, interest, month_pay = args.principal, args.periods, args.interest, args.payment


def diff_payment():
    global interest
    interest /= 1200

    total_diff_paid = 0

    for i in range(1, periods + 1):
        mth_diff_payment = ceil(
            principal / periods + interest * (principal - (principal*(i - 1)) / periods))
        total_diff_paid += mth_diff_payment
        print(f"Month {i}: paid out {mth_diff_payment}")
    print()
    print(f"Overpayment = {total_diff_paid - principal}")


def annuity_payment():
    global interest
    interest /= 1200

    annuity_payment = ceil((principal * interest * pow(
        1 + interest, periods)) / (pow(1 + interest, periods) - 1))
    print(f"Your annuity payment = {annuity_payment}!")


def count_of_months():
    global interest
    interest /= 1200
    num_months = ceil(
        log(month_pay/(month_pay - interest * principal), interest + 1))

    years_needed, months_needed = num_months // 12, num_months % 12

    if not years_needed and months_needed == 1:
        print("You need 1 month to repay this credit!")
    elif not months_needed:
        print(f"You need {years_needed} years to repay this credit!")
    elif years_needed == 1 and not months_needed:
        print("You need 1 year to repay this credit!")
    elif not years_needed:
        print(f"You need {months_needed} months to repay this credit!")
    else:
        print(
            f"You need {years_needed} years and {months_needed} months to repay this credit!")

    print(f"Overpayment = {num_months * month_pay - principal}")


def find_principal():
    global interest
    interest /= 1200
    principal = floor(month_pay / (interest * pow(1 + interest,
                                                  periods) / (pow(1 + interest, periods) - 1)))
    print(f"Your credit principal = {principal}!")
    print(f"Overpayment = {month_pay * periods - principal}")


def main():
    if args.type == "diff":
        conditions = all([args.type is not None, principal is not None and principal >
                          0, periods is not None and periods > 0, interest is not None and interest > 0])
        if conditions:
            diff_payment()
        else:
            print("Incorrect parameters")
    elif args.type == "annuity":
        if principal and periods and interest:
            annuity_payment()
        elif principal and month_pay and interest:
            count_of_months()
        elif month_pay and periods and interest:
            find_principal()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")


main()
