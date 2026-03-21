def main():
    N = int(input())
    num = {}
    for _ in range(N):
        X_i = int(input())
        try:
            num[X_i] += 1
        except KeyError:
            num[X_i] = 1
    num = sorted(num.items(), key=lambda k: (-k[1], k[0]))

    print(num[0][0])


if __name__ == "__main__":
    main()
