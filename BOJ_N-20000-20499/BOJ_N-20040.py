def main():

    # def find(v):
    #     if v != node[v]:
    #         node[v] = find(node[v])
    #     return node[v]

    def find(v):
        while v != node[v]:
            v = node[v]
        return v

    def union(a, b):
        s, e = find(a), find(b)
        if s > e:
            node[s] = e
        else:
            node[e] = s

    n, m = map(int, input().split())
    node = list(range(n))

    num = 0
    for c in range(m):
        A, B = map(int, input().split())
        if find(A) != find(B):
            union(A, B)
        else:
            num = c + 1
            break
    print(num)


if __name__ == "__main__":
    main()
