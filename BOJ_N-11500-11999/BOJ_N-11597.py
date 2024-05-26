def main():
    n = int(input())
    s = sorted([int(input()) for _ in range(n)])

    X = int(1e9)
    for i in range(n//2):
        X = min(s[i] + s[-i-1], X)

    print(X)


if __name__ == "__main__":
    main()
