def main():
    N, Q = map(int, input().split())
    comp = {c: x for c, x in zip(range(1, N+1), list(map(int, input().split())))}
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            C, X = query[1], query[2]

            comp[C] = X
        elif query[0] == 2:
            A, B = query[1], query[2]

            print(abs(comp[B] - comp[A]))


if __name__ == "__main__":
    main()
