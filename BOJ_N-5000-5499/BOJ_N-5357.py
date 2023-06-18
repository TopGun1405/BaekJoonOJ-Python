def main():
    N = int(input())
    for _ in range(N):
        sr = input()
        ans = sr[0]
        for s in sr:
            if ans[-1] != s:
                ans += s
        print(ans)


if __name__ == "__main__":
    main()
