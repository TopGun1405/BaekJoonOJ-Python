def main():
    types = {
        "................": 0,
        "****............": 0,
        "********........": 0,
        "************....": 0,
        "****************": 0
    }

    M, N = map(int, input().split())
    windows = [input() for _ in range(5*M+1)]

    patterns = []
    for m in range(1, 5*M+1, 5):
        for n in range(1, 5*N+1, 5):
            patterns.append("".join([windows[m+i][n:n+4] for i in range(4)]))

    for pattern in patterns:
        types[pattern] += 1

    print(*types.values())


if __name__ == "__main__":
    main()
