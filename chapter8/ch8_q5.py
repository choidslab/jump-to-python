def fibonacci(n):
    if n == 0:
        return 0          # n이 0일 때는 0을 반환
    elif n == 1:
        return 1          # n이 1일 때는 1을 반환
    else:
        return fibonacci(n-2) + fibonacci(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환


if __name__ == "__main__":
    n = int(input("숫자입력: "))
    for i in range(n):
        print(fibonacci(i), end=", ")
