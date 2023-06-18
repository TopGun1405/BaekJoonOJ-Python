def main():
    N, K = map(int, input().split())
    print(factorial(N) // (factorial(K) * factorial(N - K)))


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == "__main__":
    main()
