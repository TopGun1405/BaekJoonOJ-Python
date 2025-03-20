def main():
    N, L, K = map(int, input().split())
    sub = [list(map(int, input().split())) for _ in range(N)]
    sub.sort(key=lambda k: k[1])

    score, k = 0, 0
    for s in sub:
        if k == K:
            break

        if s[1] <= L:
            k += 1
            score += 140
        elif s[0] <= L:
            k += 1
            score += 100

    print(score)


if __name__ == "__main__":
    main()
