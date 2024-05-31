def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    stress, cnt_s = 0, 0
    for A_N in A:
        stress = (stress + A_N) if stress + A_N >= 0 else 0
        if stress >= M:
            cnt_s += 1

    print(cnt_s)


if __name__ == "__main__":
    main()
