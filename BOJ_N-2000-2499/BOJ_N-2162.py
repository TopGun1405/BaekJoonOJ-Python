def main() -> None:
    def find(V: int) -> int:
        if V != node[V]:
            node[V] = find(node[V])
        return node[V]

    def union(A: int, B: int) -> None:
        s, e = find(A), find(B)
        if s > e:
            node[s] = e
        else:
            node[e] = s

    def ccw(V1: list, V2: list) -> bool:
        x1, y1, x2, y2 = V1
        x3, y3, x4, y4 = V2

        if max(x1, x2) < min(x3, x4):
            return False
        if min(x1, x2) > max(x3, x4):
            return False
        if max(y1, y2) < min(y3, y4):
            return False
        if min(y1, y2) > max(y3, y4):
            return False

        v1 = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
        v2 = (x2-x1) * (y4-y1) - (x4-x1) * (y2-y1)
        v3 = (x4-x3) * (y1-y3) - (x1-x3) * (y4-y3)
        v4 = (x4-x3) * (y2-y3) - (x2-x3) * (y4-y3)

        if v1 == v2 == v3 == v4 == 0:
            return True
        return v1 * v2 <= 0 and v3 * v4 <= 0

    N = int(input())
    node = list(range(N))
    # for _ in range(N):
    #     x1, y1, x2, y2 = map(int, input().split())
    segments = [[x1, y1, x2, y2] for x1, y1, x2, y2 in [map(int, input().split()) for _ in range(N)]]
    segments = list(enumerate(segments))
    for i in range(N):
        for j in range(N):
            _, segment1 = segments[i]
            _, segment2 = segments[j]
            if ccw(segment1, segment2):
                union(i, j)

    for v in range(N):
        find(v)

    group = {}
    for v in node:
        try:
            group[v] += 1
        except KeyError:
            group[v] = 1
    print(len(group))
    print(max(group.values()))


if __name__ == "__main__":
    main()
    