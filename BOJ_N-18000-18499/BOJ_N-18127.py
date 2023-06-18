def main():
    A, B = map(int, input().split())
    a = b = 1
    for _ in range(B):
        a += A - 2
        b += a
    print(b)


if __name__ == "__main__":
    main()
