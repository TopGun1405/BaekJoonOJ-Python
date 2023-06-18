def main():
    N = int(input())
    num = list(str(factorial(N)))

    count = 0
    while True:
        if not num[-1] == '0':
            break
        count = count + 1
        del num[-1]
    print(count)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    main()
