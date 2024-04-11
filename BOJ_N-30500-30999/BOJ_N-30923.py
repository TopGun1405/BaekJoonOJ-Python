def main():
    N = int(input())
    h = list(map(int, input().split()))

    # s = sum([abs(h[i+1] - h[i]) for i in range(N - 1)])
    # print(s + 2*sum(h) + h[0] + h[-1] + 2*N)

    s = 0 if N > 1 else h[0]
    for hi, hj in zip(h[:-1], h[1:]):
        s += abs(hi - hj)

    for i, hi in enumerate(h):
        if i == 0 or i == N - 1:
            s += hi
        s += 2 + 2*hi

    print(s)


if __name__ == "__main__":
    main()
