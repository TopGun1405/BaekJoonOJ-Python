def main():
    n = int(input())

    fib, num = [], 0
    for i in range(n + 1):
        if i == 0:
            num = 0
        elif i <= 2:
            num = 1
        else:
            num = fib[-1] + fib[-2]
        fib.append(num)
    print(fib[-1])


if __name__ == "__main__":
    main()
