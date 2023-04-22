def main():
    solution_1()


def solution_1():
    N = int(input())
    parent = list(map(int, input().split()))
    d = int(input())

    tree = {n: [] for n in range(N)}
    for i in range(len(parent)):
        if parent[i] != -1:
            tree[parent[i]].append(i)

    for node in tree:
        for i in range(len(tree[node])):
            if tree[node][i] == d:
                del tree[node][i]
                break
    delete_tree(tree, d)

    count = 0
    for node in tree:
        if not tree[node]:
            count += 1
    print(count)


def delete_tree(tree: dict, d: int):
    if not tree[d]:
        del tree[d]
    else:
        for n in tree[d]:
            delete_tree(tree, n)
        del tree[d]


if __name__ == "__main__":
    main()
