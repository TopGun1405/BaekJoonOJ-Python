def main():
    N = int(input())
    drinks = sorted(map(int, input().split()))

    mixed = drinks[-1]
    for drink in drinks[:-1]:
        mixed += drink / 2
    print(mixed)


if __name__ == "__main__":
    main()
