def main():
    N, C = map(int, input().split())

    x, y = N, N
    for _ in range(C):
        X, Y = map(int, input().split())
        if 0 <= X <= x and 0 <= Y <= y:
            if X * y < Y * x:
                y = Y
            else:
                x = X

    print(x * y)


if __name__ == "__main__":
    main()
