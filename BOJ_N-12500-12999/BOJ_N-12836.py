def main():
    N, Q = map(int, input().split())
    val = [0] * (N + 1)
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            _, p, x = query
            val[p] += x

        elif query[0] == 2:
            _, p, q = query
            print(sum(val[p:q+1]))


if __name__ == "__main__":
    main()
