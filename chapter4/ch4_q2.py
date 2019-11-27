def sum_of_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    avg = float(sum / len(args))
    return avg


if __name__ == "__main__":
    print(sum_of_numbers(1, 2, 3, 4, 5))
    print(sum_of_numbers(1, 2, 3))
    print(sum_of_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
