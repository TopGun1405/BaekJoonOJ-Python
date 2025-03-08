def main():
    F = [1, 1]
    for N in range(2, 46):
        F.append(F[N - 1] + F[N - 2])

    n = int(input())
    for _ in range(n):
        x = int(input())

        print(F[x])


if __name__ == "__main__":
    main()
