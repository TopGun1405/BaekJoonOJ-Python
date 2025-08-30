def main():
    N, M = map(int, input().split())

    X_curr, Y_curr = 0, 0
    score = 0
    targets = {}

    X_maxScore, Y_maxScore = 0, 0
    idx, dis = 0, 0
    for i in range(N):
        x_i, y_i = map(int, input().split())

        if x_i**2 + y_i**2 > dis:
            X_maxScore, Y_maxScore = x_i, y_i
            idx = i
            dis = x_i**2 + y_i**2

        targets[i] = [x_i, y_i]

    X_curr, Y_curr = X_maxScore, Y_maxScore
    score += dis
    del targets[idx]
    cnt = M-1
    for j in range(M):
        x_j, y_j = map(int, input().split())
        targets[N+j] = [x_j, y_j]

        if cnt > 0:
            dis = 0
            for i in targets.keys():
                tmp = (targets[i][0]-X_curr)**2 + (targets[i][1]-Y_curr)**2
                if tmp > dis:
                    X_maxScore, Y_maxScore = targets[i][0], targets[i][1]
                    idx = i
                    dis = tmp

            X_curr, Y_curr = X_maxScore, Y_maxScore
            score += dis
            del targets[idx]
        cnt -= 1

    print(score)


if __name__ == "__main__":
    main()
