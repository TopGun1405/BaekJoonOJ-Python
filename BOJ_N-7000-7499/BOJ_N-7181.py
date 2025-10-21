def main():
    pw = input()
    N = int(input())
    for _ in range(N):
        guess = input()

        num, pos = 0, 0
        for i in range(4):
            if guess[i] in pw:
                num += 1
            if guess[i] == pw[i]:
                pos += 1

        print(num, pos)


if __name__ == "__main__":
    main()
