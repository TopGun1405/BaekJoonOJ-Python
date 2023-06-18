def main():
    X = int(input())
    N = int(input())
    able, left = X, 0
    for _ in range(N):
        P = int(input())
        able = X + left
        left = able - P
    print(X + left)


if __name__ == "__main__":
    main()
