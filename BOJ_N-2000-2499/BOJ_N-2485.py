def gcd(n, m):
    if m == 0:
        return n
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def main():
    N = int(input())
    trees = [int(input()) for _ in range(N)]
    dis = [x2 - x1 for x1, x2 in zip(trees[:-1], trees[1:])]
    tree = gcd(max(dis[0], dis[1]), min(dis[0], dis[1]))
    for d in dis[2:]:
        tree = gcd(max(tree, d), min(tree, d))
    print((trees[-1] - trees[0]) // tree + 1 - N)


if __name__ == "__main__":
    main()
