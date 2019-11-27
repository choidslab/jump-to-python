class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):

        if self.value + val <= 100:
            self.value += val
        else:
            self.value += (self.value + val) - 100


if __name__ == "__main__":
    cal = MaxLimitCalculator()
    cal.add(50)  # 50 더하기
    print(cal.value)
    cal.add(60)  # 60 더하기
    print(cal.value)  # 100 출력