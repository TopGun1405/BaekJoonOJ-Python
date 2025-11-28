def main():
    X, Y = map(int, input().split())
    N = int(input())
    for _ in range(N):
        x_i, y_i = map(int, input().split())

        if X != x_i and Y != y_i:
            print(1)
        elif X != x_i or Y != y_i:
            print(0)


if __name__ == "__main__":
    main()
