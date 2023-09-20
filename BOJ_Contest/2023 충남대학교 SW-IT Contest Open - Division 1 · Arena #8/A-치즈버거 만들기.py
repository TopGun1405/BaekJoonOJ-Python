def main():
    A, B = map(int, input().split())
    # if A > B:
    #     print(B + (B + 1))
    # else:
    #     print(A + (A - 1))
    print(2 * B + 1 if A > B else 2 * A - 1)


if __name__ == "__main__":
    main()
