def is_odd(num):
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')


if __name__ == "__main__":
    num = int(input("정수입력: "))
    is_odd(num)
