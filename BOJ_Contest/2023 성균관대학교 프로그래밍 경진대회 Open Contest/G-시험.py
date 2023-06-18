def main():
    N, K = map(int, input().split())
    PQ = [list(map(int, input().split())) for _ in range(N)]

    low, high = 0, 1
    for _ in range(20):
        mid = (low + high) / 2
        c = sum(sorted([-pq[1] * mid + pq[0] for pq in PQ], reverse=True)[:K])
        if c >= 0:
            low = mid
        else:
            high = mid
    print(low)


if __name__ == "__main__":
    main()
