def fibonacci_rec(n):
    if n == 1 or n == 2:
        # code 1
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_dp(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n):
        # code 2
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def main():
    n = int(input())
    fib = [0, 1]
    for i in range(39):
        fib.append(fib[-1] + fib[-2])
    # print(fibonacci_rec(n), n - 2)
    print(fib[n], n - 2)


if __name__ == "__main__":
    main()
