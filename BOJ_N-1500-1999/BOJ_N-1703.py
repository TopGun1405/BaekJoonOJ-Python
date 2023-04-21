def main():
    while True:
        tree = list(map(int, input().split()))
        if tree[0] == 0:
            break
        ans = 1
        for t in range(tree[0]):
            sf, p = tree[2 * t + 1], tree[2 * t + 2]
            ans = ans * sf - p
        print(ans)


if __name__ == "__main__":
    main()
