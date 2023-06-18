def main():
    A, B, C, X, Y = map(int, input().split())
    if A+B < 2*C:
        print(A*X + B*Y)
    else:
        print(2*C*min(X, Y) + min(A, 2*C) * max(0, X-Y) + min(B, 2*C) * max(0, Y-X))


if __name__ == "__main__":
    main()
