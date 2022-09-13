def main():
    n, m = map(int, input().split())
    pic = [list(input()) for _ in range(n)]
    rev = {'B': 'W', 'W': 'B'}
    input()
    fixed = [list(input()) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if fixed[i][j] != rev[pic[i][j]]:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
