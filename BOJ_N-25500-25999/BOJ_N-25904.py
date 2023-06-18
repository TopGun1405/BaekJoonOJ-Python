def main():
    N, X = map(int, input().split())
    T = list(map(int, input().split()))
    check, ans = True, 0
    while check:
        for i in range(N):
            if X <= T[i]:
                X += 1
            else:
                check, ans = False, i
                break
    print(ans + 1)


if __name__ == "__main__":
    main()
