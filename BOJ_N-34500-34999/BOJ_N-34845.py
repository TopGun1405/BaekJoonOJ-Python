def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    cnt, tot = 0, sum(A)
    while True:
        if tot / (N + cnt) >= X:
            print(cnt)
            break
        cnt += 1
        tot += 100


if __name__ == "__main__":
    main()
