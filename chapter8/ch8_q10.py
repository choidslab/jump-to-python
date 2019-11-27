class Calculator:
    def __init__(self, data):
        self.num = data
        self.sum = 0
        self.avg = 0.0

    def sum_of_data(self):
        for item in self.num:
            self.sum += item
        return self.sum

    def avg_of_data(self):
        self.avg = float(self.sum / len(self.num))
        return self.avg


if __name__ == "__main__":
    cal1 = Calculator([1, 2, 3, 4, 5])
    # print(cal1.num)
    print(cal1.sum_of_data())
    print(cal1.avg_of_data())

    cal2 = Calculator([6, 7, 8, 9, 10])
    print(cal2.sum_of_data())
    print(cal2.avg_of_data())
