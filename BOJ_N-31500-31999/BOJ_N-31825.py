def main():
    N, Q = map(int, input().split())
    S = list(input())
    for _ in range(Q):
        q, l, r = map(int, input().split())

        if q == 1:
            cnt, prev = 1, S[l-1]
            for i in range(l, r):
                if S[i] != prev:
                    cnt += 1
                prev = S[i]

            print(cnt)
        elif q == 2:
            for i in range(l-1, r):
                S[i] = chr((ord(S[i]) - 64) % 26 + 65)


if __name__ == "__main__":
    main()
