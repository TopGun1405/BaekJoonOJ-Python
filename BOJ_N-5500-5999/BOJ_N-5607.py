def main():
    n = int(input())
    A = B = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            A += a + b
        elif a < b:
            B += a + b
        else:
            A, B = A + a, B + b
    print(A, B)


if __name__ == "__main__":
    main()
