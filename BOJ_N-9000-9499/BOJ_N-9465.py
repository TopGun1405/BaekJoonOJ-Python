def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        scores = [list(map(int, input().split())) for _ in range(2)]
        s = [[0] * (n + 2) for _ in range(2)]
        for i in range(1, n + 1):
            s[0][i] = max(s[1][i-1], s[1][i-2]) + scores[0][i-1]
            s[1][i] = max(s[0][i-1], s[0][i-2]) + scores[1][i-1]
        print(max(s[0][n], s[1][n]))


if __name__ == "__main__":
    main()
