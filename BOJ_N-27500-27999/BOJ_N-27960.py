def main():
    SA, SB = map(int, input().split())
    print(int(bin(SA ^ SB)[2:], 2))


if __name__ == "__main__":
    main()
