def main():
    N = int(input())
    seat = input()
    couple = seat.count("LL")
    print(N - couple + (1 if couple > 0 else 0))


if __name__ == "__main__":
    main()
