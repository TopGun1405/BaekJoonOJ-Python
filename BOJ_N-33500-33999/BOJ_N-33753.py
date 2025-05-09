def main():
    A, B, C = map(int, input().split())
    T = int(input())

    if T <= 30:
        print(A)
    else:
        T -= 30
        T = T // B + (1 if T % B != 0 else 0)

        print(A + T * C)


if __name__ == "__main__":
    main()
