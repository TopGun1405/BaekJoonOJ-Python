def factorial(n):
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k


def main():
    n, m = map(int, input().split())
    print(factorial(n) // (factorial(n - m) * factorial(m)))


if __name__ == "__main__":
    main()
