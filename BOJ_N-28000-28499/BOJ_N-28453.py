def main():
    N = int(input())
    M = list(map(int, input().split()))

    for Mi in M:
        if Mi == 300:
            print(1, end=' ')
        elif 275 <= Mi < 300:
            print(2, end=' ')
        elif 250 <= Mi < 275:
            print(3, end=' ')
        elif Mi < 250:
            print(4, end=' ')


if __name__ == "__main__":
    main()
