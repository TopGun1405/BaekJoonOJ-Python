def main():
    N, M = map(int, input().split())
    truth = set(input().split()[1:])
    party = [set(input().split()[1:]) for _ in range(M)]

    for _ in range(M):
        for p_i in party:
            if p_i & truth:
                truth = truth.union(p_i)

    cnt = 0
    for p_i in party:
        if not p_i & truth:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
