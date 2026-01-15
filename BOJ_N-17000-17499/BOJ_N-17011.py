def main():
    N = int(input())
    for _ in range(N):
        s = input()

        encoded = []
        c, cnt = s[0], 1
        for i in range(1, len(s)):
            if c == s[i]:
                cnt += 1
            else:
                encoded += [str(cnt), c]
                c, cnt = s[i], 1
        encoded += [str(cnt), c]

        print(*encoded)


if __name__ == "__main__":
    main()
