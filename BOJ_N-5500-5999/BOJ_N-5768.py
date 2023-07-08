def main():
    while True:
        M, N = map(int, input().split())

        if M == N == 0:
            break

        X = Y = 0
        for x in range(M, N + 1):
            y = 0
            for n in range(1, int(x ** 0.5) + 1):
                if x % n == 0:
                    y = y + (2 if n ** 2 != x else 1)

            if y >= Y:
                X, Y = x, y
        print(X, Y)


if __name__ == "__main__":
    main()
