def main():
    A, B = map(int, input().split())

    A, B = max(A, B), min(A, B)
    while B != 0:
        A, B = B, A % B

    print(A)


if __name__ == "__main__":
    main()
