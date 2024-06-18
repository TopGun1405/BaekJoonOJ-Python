def main():

    def ready_camp(rec, idx, tot, maximum, minimum):
        if tot > R:
            return

        if rec >= 2 and L <= tot <= R:
            if maximum - minimum >= X:
                res['CNT'] += 1

        for i in range(idx, N):
            ready_camp(rec+1, i+1, tot+A[i], A[i], min(A[i], minimum))

    N, L, R, X = map(int, input().split())
    A = sorted(map(int, input().split()))

    res = {'CNT': 0}
    ready_camp(0, 0, 0, 0, int(1e9))

    print(res['CNT'])


if __name__ == "__main__":
    main()
