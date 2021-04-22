from budget import Budget


class ISS(object):

    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.1


class ICMS(object):

    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.06
