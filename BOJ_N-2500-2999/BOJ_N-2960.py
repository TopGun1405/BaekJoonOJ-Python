def main():
    N, K = map(int, input().split())

    cnt = 0
    sieve = [False, False] + [True] * (N - 1)
    for i in range(2, N + 1):
        if not sieve[i]:
            continue
        for j in range(i, N + 1, i):
            if sieve[j]:
                cnt += 1
                sieve[j] = False
            if cnt == K:
                print(j)
                break
        else:
            continue


if __name__ == "__main__":
    main()
