def main():
    STR, DEX, INT, LUK, N = map(int, input().split())
    TOT = STR + DEX + INT + LUK
    print(0 if TOT >= 4 * N else 4 * N - TOT)


if __name__ == "__main__":
    main()
