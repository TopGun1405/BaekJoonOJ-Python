from bisect import bisect_left


def main():
    N = int(input())
    wires = sorted([list(map(int, input().split())) for _ in range(N)])
    print(wires)
    wireB, idx = [], []

    for wire in wires:
        i = bisect_left(wireB, wire[1])
        if len(wireB) != i:
            wireB[i] = wire[1]
        else:
            wireB.append(wire[1])
        idx.append(i)
    print(wireB, idx)

    res = []
    ci = len(wireB) - 1
    for i in range(len(idx) - 1, -1, -1):
        if idx[i] != ci:
            res.append(wires[i + 1][0])
        else:
            ci -= 1

    print(N - len(wireB))
    print(*res[::-1], sep='\n')


if __name__ == "__main__":
    main()
