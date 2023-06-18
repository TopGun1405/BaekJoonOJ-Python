def main():
    P = int(input())
    paper = [[0 for _ in range(100)] for _ in range(100)]
    for _ in range(P):
        x, y = map(int, input().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                paper[i - 1][j - 1] = 1

    ans = 0
    for r in paper:
        ans += r.count(1)
    print(ans)


if __name__ == "__main__":
    main()
