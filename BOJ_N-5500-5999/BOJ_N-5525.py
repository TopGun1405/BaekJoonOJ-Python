def main():
    N = int(input())
    M = int(input())
    S = input()

    cnt, idx, res = 0, 0, 0
    while idx < M - 1:
        if S[idx:idx+3] == "IOI":
            cnt, idx = cnt + 1, idx + 2
            if cnt == N:
                cnt, res = cnt - 1, res + 1
        else:
            cnt, idx = 0, idx + 1

    print(res)


if __name__ == "__main__":
    main()
