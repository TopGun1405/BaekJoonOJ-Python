def main():
    X = str(int(input()) + 1)
    while int(X) <= 9999:
        if (int(X[:2]) + int(X[2:])) ** 2 == int(X):
            print(X)
            break
        X = str(int(X) + 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
