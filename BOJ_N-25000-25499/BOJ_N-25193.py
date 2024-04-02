def main():
    N = int(input())
    S = list(input())
    C = S.count("C")

    print(C // (N - C + 1) + (1 if (C % (N - C + 1)) else 0))


if __name__ == "__main__":
    main()
