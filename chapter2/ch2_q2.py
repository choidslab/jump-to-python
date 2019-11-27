def dicriminator_of_num(num):
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')


if __name__ == "__main__":
    num = int(input('숫자입력: '))
    dicriminator_of_num(num)
