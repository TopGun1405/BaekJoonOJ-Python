def main():
    X, Y = map(int, input().split())
    B = (Y - 2 * X) // 2
    A = X - B
    print(A, B)


if __name__ == "__main__":
    main()
