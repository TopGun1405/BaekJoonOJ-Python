def main():
    N = int(input())

    A = B = 0
    t = False
    while N:
        x = N - (N >> 1)
        if t:
            A += x
        else:
            B += x

        t = not t
        N //= 2

    print(A, B)


if __name__ == "__main__":
    main()
