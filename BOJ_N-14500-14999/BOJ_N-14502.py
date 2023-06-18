from collections import deque
from copy import deepcopy


def main():

    def bfsLab():
        tosLab = deepcopy(lab)
        for row in range(N):
            for col in range(M):
                if tosLab[row][col] == 2:
                    queue = deque([(row, col)])
                    while queue:
                        currR, currC = queue.popleft()
                        for i in range(4):
                            r = currR + dx[i]
                            c = currC + dy[i]
                            if 0 <= r < N and 0 <= c < M:
                                if tosLab[r][c] == 0:
                                    tosLab[r][c] = 2
                                    queue.append((r, c))

        notInf = 0
        for r in range(N):
            for c in range(M):
                if tosLab[r][c] == 0:
                    notInf += 1
        ans.append(max(ans[-1], notInf))

    def buildWall(walls):
        if walls == 3:
            bfsLab()
            return
        for n in range(N):
            for m in range(M):
                if lab[n][m] == 0:
                    lab[n][m] = 1
                    buildWall(walls + 1)
                    lab[n][m] = 0

    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = [0]
    buildWall(0)
    print(ans[-1])


if __name__ == "__main__":
    main()
