def main():
    def find(v: int) -> int:
        if v != node[v]:
            node[v] = find(node[v])
        return node[v]

    def union(A: int, B: int) -> None:
        s, e = find(A), find(B)
        # RecursionError
        # if s > e:
        #     node[s] = e
        if s < e:
            node[s] = e
        else:
            node[e] = s

    n, m = map(int, input().split())
    node = list(range(n + 1))

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(a, b)
        else:
            print("YES" if find(a) == find(b) else "NO")


if __name__ == "__main__":
    main()
