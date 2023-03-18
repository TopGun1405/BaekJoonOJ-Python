def main():
    while True:
        S = input()
        if S == '0':
            break
        while len(S) > 1:
            print(S, end=' ')
            ans = 1
            for s in S:
                ans *= int(s)
            S = str(ans)
        print(S)


if __name__ == "__main__":
    main()
