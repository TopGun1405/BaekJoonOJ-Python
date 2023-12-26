def main():
    N, M, K = map(int, input().split())

    sub = {}
    for _ in range(N):
        si, pi = map(lambda e: int(e) if e.isdigit() else e, input().split())
        sub[si] = pi

    tot = 0
    for _ in range(K):
        ti = input()
        tot += sub[ti]
        sub.pop(ti)

    scores = sorted(sub.values())
    # print(tot + sum(scores[:M - K]), tot + (sum(scores[-M + K:]) if M != K else 0))
    print(tot + sum(scores[:M-K]), tot + sum(scores[::-1][:M-K]))


if __name__ == "__main__":
    main()
