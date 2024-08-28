def main():
    while True:
        N, D = map(int, input().split())

        if N == D == 0:
            break

        X = [list(map(int, input().split())) for _ in range(D)]
        cnt = [sum(X[j][i] for j in range(D)) for i in range(N)]

        print("yes" if D in cnt else "no")


if __name__ == "__main__":
    main()
