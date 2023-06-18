def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        votes = [0] * N
        for _ in range(M):
            v = map(int, input().split())
            for idx, val in enumerate(v):
                votes[idx] += val
        print(votes.index(max(votes)) + 1)


if __name__ == "__main__":
    main()
