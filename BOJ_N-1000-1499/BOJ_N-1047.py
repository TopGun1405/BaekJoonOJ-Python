def main():
    N = int(input())
    trees = [list(map(int, input().split())) for _ in range(N)]
    tree_x = sorted(trees, key=lambda k: k[0])
    tree_y = sorted(trees, key=lambda k: k[1])
    tree_h = sorted(trees, key=lambda k: k[2])
    minVal = 1e9
    for idxX, L1 in enumerate(tree_x):
        for L2 in tree_x[idxX:]:
            for idxY, L3 in enumerate(tree_y):
                for L4 in tree_y[idxY:]:
                    inRange, outRange, fenceLen = [], 0, 0
                    x1, y1 = L1[0], L3[1]
                    x2, y2 = L2[0], L4[1]
                    rect = 2 * (x2 - x1) + 2 * (y2 - y1)
                    for tree in tree_h:
                        x, y, h = tree[0], tree[1], tree[2]
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            inRange.append(h)
                        else:
                            outRange += 1
                            fenceLen += h
                    while rect > fenceLen and inRange:
                        fenceLen += inRange.pop()
                        outRange += 1
                    minVal = min(minVal, outRange)
    print(minVal)


if __name__ == "__main__":
    main()
