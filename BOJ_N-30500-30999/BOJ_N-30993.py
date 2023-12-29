def main():

    def factorial(n: int) -> int:
        tot = 1
        for n in range(n, 0, -1):
            tot *= n
        return tot

    N, A, B, C = map(int, input().split())
    print(factorial(N) // (factorial(A) * factorial(B) * factorial(C)))


if __name__ == "__main__":
    main()
