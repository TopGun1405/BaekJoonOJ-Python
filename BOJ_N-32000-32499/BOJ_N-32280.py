def main():
    N = int(input())
    table = []
    limit_t = 0
    for _ in range(N+1):
        T, C = input().split()
        T = sum(int(t) * 60 ** i for i, t in enumerate(reversed(T.split(":"))))
        if C == "teacher":
            limit_t = T
        else:
            table.append([T, C])
    limit = sum(int(t) * 60 ** i for i, t in enumerate(reversed(input().split(":"))))
    limit = max(limit, limit_t)

    print(len(list(filter(lambda e: e[0] >= limit, table))))


if __name__ == "__main__":
    main()
