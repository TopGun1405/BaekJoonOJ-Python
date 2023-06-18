def main():
    N = int(input())
    coord = [list(map(int, input().split())) for _ in range(N)]
    coord.sort(key=lambda k: (k[1], k[0]))
    for i in range(N):
        print(coord[i][0], coord[i][1])


if __name__ == "__main__":
    main()
