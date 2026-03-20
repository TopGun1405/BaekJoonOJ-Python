def main():
    while True:
        n, m = map(int, input().split())

        if n == m == 0:
            break

        score = [list(map(int, input().split())) for _ in range(m)]
        maxScore = 0
        for i in range(n):
            s_i = 0
            for j in range(m):
                s_i += score[j][i]
            maxScore = max(maxScore, s_i)

        print(maxScore)


if __name__ == "__main__":
    main()
