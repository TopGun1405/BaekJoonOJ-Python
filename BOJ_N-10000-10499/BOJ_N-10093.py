def main():
    A, B = map(int, input().split())
    A, B = min(A, B), max(A, B)
    if B - A <= 1:
        print(0)
    else:
        print(B - A - 1)
        for i in range(A + 1, B):
            print(i, end=' ')


if __name__ == "__main__":
    main()
