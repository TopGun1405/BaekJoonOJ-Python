def main():
    N = int(input())
    stst = input()
    ans = 0
    for i in range(N // 2):
        if stst[i] != stst[-(i + 1)]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
