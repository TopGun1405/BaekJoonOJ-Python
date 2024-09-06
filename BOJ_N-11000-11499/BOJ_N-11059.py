def main():
    S = input()

    N, max_len = len(S), 0
    num = list(map(int, S))
    pref_sum = [0] * (N+1)
    for i in range(1, N+1):
        pref_sum[i] = pref_sum[i-1] + num[i-1]

    for l in range(2, N+1, 2):
        for s in range(N-l+1):
            m = s + l // 2
            if pref_sum[m]-pref_sum[s] == pref_sum[s+l]-pref_sum[m]:
                max_len = max(max_len, l)

    print(max_len)


if __name__ == "__main__":
    main()
