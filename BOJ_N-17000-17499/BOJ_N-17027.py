def main():
    N = int(input())

    cnt = [0, 0, 0]
    gravel = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for _ in range(N):
        a, b, g = map(int, input().split())
        for i in range(3):
            gravel[i][a-1], gravel[i][b-1] = gravel[i][b-1], gravel[i][a-1]

            if gravel[i][g-1]:
                cnt[i] += 1

    print(max(cnt))


if __name__ == "__main__":
    main()
