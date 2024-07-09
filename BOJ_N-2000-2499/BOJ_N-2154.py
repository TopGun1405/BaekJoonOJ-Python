def main():
    N = input()

    S = "".join(map(str, range(1, 100_001)))
    print(S.index(N) + 1)


if __name__ == "__main__":
    main()
