def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(factorial(M) // (factorial(N) * factorial(M - N)))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    main()
