class Calculator:

    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):

    def minus(self, val):
        self.value -= val


if __name__ == "__main__":
    cal = UpgradeCalculator()
    cal.add(10)
    cal.minus(7)

    print(cal.value)
