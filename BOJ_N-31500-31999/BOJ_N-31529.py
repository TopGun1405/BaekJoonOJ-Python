def main():
    X, Y = map(int, input().split())

    if Y < X or 2 * X < Y:
        print(-1)
    else:
        print(1012 * X - 506 * Y)


if __name__ == "__main__":
    main()
