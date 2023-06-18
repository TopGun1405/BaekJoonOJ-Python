from itertools import combinations


def main():

    def StartLink():
        pass

    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    player = list(range(N))
    teams = list(combinations(player, N//2))
    print(teams)
    minVal = 100
    for n in range(len(teams) // 2):
        start, link = teams[n], teams[-n-1]
        sPoint = 0
        for i in start[:-1]:
            for j in start[1:]:
                sPoint += S[i][j] + S[j][i]
        lPoint = 0
        for i in link[:-1]:
            for j in link[1:]:
                lPoint += S[i][j] + S[j][i]
        minVal = min(minVal, abs(sPoint - lPoint))
        print(sPoint, lPoint)
        print(start, link)
    print(minVal)


if __name__ == "__main__":
    main()
