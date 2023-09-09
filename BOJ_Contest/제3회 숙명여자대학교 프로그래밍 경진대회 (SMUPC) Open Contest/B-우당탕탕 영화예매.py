def main():
    N, M, K = map(int, input().split())
    seats = [input() for _ in range(N)]
    cnt = 0
    for seat in seats:
        for i in range(M-K+1):
            if seat[i:i+K] == '0' * K:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
