def main():
    N = int(input())
    A, B, C, D, E, F = map(int, input().split())
    op = {0: lambda a, b: a + b, 1: lambda a, b: a % b, 2: lambda a, b: a & b,
          3: lambda a, b: a ^ b, 4: lambda a, b: a | b, 5: lambda a, b: a >> b}

    # Bitwise-R-Shift 연산을 수행 시 항상 X가 0이 된다.
    X, k = 0, N // F
    for i in range(k * F + 1, N + 1):
        check = [i % A == 0, i % B == 0, i % C == 0,
                 i % D == 0, i % E == 0, i % F == 0]
        for idx, val in enumerate(check):
            if val:
                X = op[idx](X, i)
    print(X)


if __name__ == "__main__":
    main()
