def main():
    N, M, A, B = map(int, input().split())

    C = N * 3 - M

    print(C * A + B if C > 0 else 0)


if __name__ == "__main__":
    main()
