def main():
    A, B = map(int, input().split())
    if A < B:
        print((A + B) * (B - A + 1) // 2)
    elif A == B:
        print(A)
    else:
        print((A + B) * (A - B + 1) // 2)


if __name__ == "__main__":
    main()
