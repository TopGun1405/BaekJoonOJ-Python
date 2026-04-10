def main():
    s = input()

    cnt = 10 if s[0] == "d" else 26
    for i in range(1, len(s)):
        if s[i] == "d":
            cnt *= 9 if s[i-1] == s[i] else 10
        else:
            cnt *= 25 if s[i-1] == s[i] else 26
        cnt %= 1_000_000_009

    print(cnt)


if __name__ == "__main__":
    main()
