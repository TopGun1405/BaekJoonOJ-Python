def main():
    N = int(input())
    cnt = 0
    for _ in range(N):
        s_i, c_i, a_i, r_i = map(int, input().split())
        if s_i >= 1_000 or c_i >= 1_600 or a_i >= 1_500 or 1 <= r_i <= 30:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
