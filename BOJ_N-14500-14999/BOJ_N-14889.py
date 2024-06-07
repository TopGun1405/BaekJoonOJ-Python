def main():

    def StartLink(rec, idx):
        if rec == N//2:
            # print(visited)
            sP, lP = 0, 0
            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    if visited[i] and visited[j]:
                        sP += S[i][j]
                    elif not visited[i] and not visited[j]:
                        lP += S[i][j]
            val['MIN'] = min(val['MIN'], abs(sP - lP))
            return

        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                StartLink(rec+1, i+1)
                visited[i] = False

    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    val = {'MIN': 100}

    StartLink(0, 0)
    print(val['MIN'])


if __name__ == "__main__":
    main()
