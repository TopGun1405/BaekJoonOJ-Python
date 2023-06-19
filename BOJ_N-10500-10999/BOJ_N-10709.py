def main():
    H, W = map(int, input().split())
    weather = [list(input()) for _ in range(H)]

    for i in range(H):
        cloud, ctr = [], -1
        for j in range(W):
            if weather[i][j] == 'c':
                ctr = 0
            cloud.append(ctr)
            if ctr >= 0:
                ctr += 1
        print(*cloud)


if __name__ == "__main__":
    main()
