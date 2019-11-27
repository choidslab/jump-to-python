class FourCal:

    def __init__(self, first, second):
        self.num1 = first
        self.num2 = second

    def set_data(self, first, second):
        self.num1 = first
        self.num2 = second

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


class MoreFourCal(FourCal):

    def pow(self):
        return self.num1 ** self.num2


class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2


if __name__ == "__main__":

    cal2 = MoreFourCal(2, 10)
    print(cal2.add())
    print(cal2.sub())
    print(cal2.mul())
    print(cal2.div())
    print(cal2.pow())

    cal3 = SafeFourCal(4, 1)
    print(cal3.div())
