def main():
    F = [0] * 21
    F[0], F[1] = 1, 2

    for i in range(2, 21):
        F[i] = F[i-1] + F[i-2]

    t = int(input())
    for _ in range(t):
        x = int(input())

        y = 0
        for i in range(20, 0, -1):
            if x >= F[i]:
                x -= F[i]
                y += F[i-1]

        print(y)


if __name__ == "__main__":
    main()
