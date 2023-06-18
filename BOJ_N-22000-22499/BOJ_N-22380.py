def main():
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        A = list(map(int, input().split()))
        ans, m = 0, M // N
        for a in A:
            ans = ans + a if m > a else ans + m
        print(ans)


if __name__ == "__main__":
    main()
