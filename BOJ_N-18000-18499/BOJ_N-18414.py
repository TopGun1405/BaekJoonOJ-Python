def main():
    X, L, R = map(int, input().split())
    num = {abs(X - i): i for i in range(L, R + 1)}
    print(num[min(num.keys())])


if __name__ == "__main__":
    main()
