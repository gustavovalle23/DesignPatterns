from budget import Budget
from taxes import ISS, ICMS


class Taxes_Calculator(object):

    def do_calculation(self, budget: Budget, tax: object) -> None:
        calculated_tax = tax.calculate(budget)
        print(calculated_tax)


if __name__ == '__main__':

    calculator = Taxes_Calculator()
    budget = Budget(500)

    calculator.do_calculation(budget, ISS())
    calculator.do_calculation(budget, ICMS())
