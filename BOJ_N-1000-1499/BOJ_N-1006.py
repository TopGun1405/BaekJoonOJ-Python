def main():
    T = int(input())

    for _ in range(T):
        N, W = map(int, input().split())

        area = [list(map(int, input().split())) for _ in range(2)]
        check1 = [[False for _ in range(N)] for _ in range(2)]
        check2 = [[False for _ in range(N)] for _ in range(2)]
        # n = 5
        # [4, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 0]
        # index = [4, 0, 1, 2, 3, 4, 0]
        # o o o o o
        # o o o o o
        #
        find = []
        # print(index)
        for i in range(2):
            # print(-N // 2, N // 2)
            for j in range(-1, N + 1):
                temp1 = []
                temp2 = []
                a = area[i][j % N] + area[i][(j + 1) % N]
                b = area[i][(j + 2) % N] + area[i][(j + 1) % N]
                c = area[i - 1][(j + 1) % N] + area[i][(j + 1) % N]

                # print("center : {} left : {}, right : {}, up/down : {}"
                #       .format(area[i][j], area[i][j - 1],
                #               area[i][j + 1], area[i + 1][j]))
                if a <= W:
                    temp1.append([a, i, j % N, i, (j + 1) % N])
                if b <= W:
                    temp1.append([b, i, (j + 2) % N, i, (j + 1) % N])
                if c <= W:
                    temp1.append([c, i - 1, (j + 1) % N, i, (j + 1) % N])
                temp1.sort(key=lambda k: k[0], reverse=True)
                temp2 = [temp1[k][:] for k in range(len(temp1))]
                temp2.sort(key=lambda k: k[0], reverse=False)
                # print(temp)
                if temp1 and not check1[temp1[0][1]][temp1[0][2]] and not check1[temp1[0][3]][temp1[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check1[temp1[0][1]][temp1[0][2]] = True
                    check1[temp1[0][3]][temp1[0][4]] = True
                if temp2 and not check2[temp2[0][1]][temp2[0][2]] and not check2[temp2[0][3]][temp2[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check2[temp2[0][1]][temp2[0][2]] = True
                    check2[temp2[0][3]][temp2[0][4]] = True
        # print(check)
        # print((check[0].count(True) + check[1].count(True)) // 2 + check[0].count(False) + check[1].count(False))
        find.append((check1[0].count(True) + check1[1].count(True)) // 2 +
                    check1[0].count(False) + check1[1].count(False))
        find.append((check2[0].count(True) + check2[1].count(True)) // 2 +
                    check2[0].count(False) + check2[1].count(False))

        check1 = [[False for _ in range(N)] for _ in range(2)]
        check2 = [[False for _ in range(N)] for _ in range(2)]

        for i in range(-1, 1):
            # print(-N // 2, N // 2)
            for j in range(-1, N + 1):
                temp1 = []
                temp2 = []
                a = area[i][j % N] + area[i][(j + 1) % N]
                b = area[i][(j + 2) % N] + area[i][(j + 1) % N]
                c = area[i - 1][(j + 1) % N] + area[i][(j + 1) % N]

                # print("center : {} left : {}, right : {}, up/down : {}"
                #       .format(area[i][j], area[i][j - 1],
                #               area[i][j + 1], area[i + 1][j]))
                if a <= W:
                    temp1.append([a, i, j % N, i, (j + 1) % N])
                if b <= W:
                    temp1.append([b, i, (j + 2) % N, i, (j + 1) % N])
                if c <= W:
                    temp1.append([c, i - 1, (j + 1) % N, i, (j + 1) % N])
                temp1.sort(key=lambda k: k[0], reverse=True)
                temp2 = [temp1[k][:] for k in range(len(temp1))]
                temp2.sort(key=lambda k: k[0], reverse=False)
                # print(temp)
                if temp1 and not check1[temp1[0][1]][temp1[0][2]] and not check1[temp1[0][3]][temp1[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check1[temp1[0][1]][temp1[0][2]] = True
                    check1[temp1[0][3]][temp1[0][4]] = True
                if temp2 and not check2[temp2[0][1]][temp2[0][2]] and not check2[temp2[0][3]][temp2[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check2[temp2[0][1]][temp2[0][2]] = True
                    check2[temp2[0][3]][temp2[0][4]] = True
        # print(check)
        # print((check[0].count(True) + check[1].count(True)) // 2 + check[0].count(False) + check[1].count(False))
        find.append((check1[0].count(True) + check1[1].count(True)) // 2 +
                    check1[0].count(False) + check1[1].count(False))
        find.append((check2[0].count(True) + check2[1].count(True)) // 2 +
                    check2[0].count(False) + check2[1].count(False))

        check1 = [[False for _ in range(N)] for _ in range(2)]
        check2 = [[False for _ in range(N)] for _ in range(2)]

        for i in range(2):
            # print(-N // 2, N // 2)
            for j in range(0, N):
                temp1 = []
                temp2 = []
                a = area[i][j % N] + area[i][(j + 1) % N]
                b = area[i][(j + 2) % N] + area[i][(j + 1) % N]
                c = area[i - 1][(j + 1) % N] + area[i][(j + 1) % N]

                # print("center : {} left : {}, right : {}, up/down : {}"
                #       .format(area[i][j], area[i][j - 1],
                #               area[i][j + 1], area[i + 1][j]))
                if a <= W:
                    temp1.append([a, i, j % N, i, (j + 1) % N])
                if b <= W:
                    temp1.append([b, i, (j + 2) % N, i, (j + 1) % N])
                if c <= W:
                    temp1.append([c, i - 1, (j + 1) % N, i, (j + 1) % N])
                temp1.sort(key=lambda k: k[0], reverse=True)
                temp2 = [temp1[k][:] for k in range(len(temp1))]
                temp2.sort(key=lambda k: k[0], reverse=False)
                # print(temp)
                if temp1 and not check1[temp1[0][1]][temp1[0][2]] and not check1[temp1[0][3]][temp1[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check1[temp1[0][1]][temp1[0][2]] = True
                    check1[temp1[0][3]][temp1[0][4]] = True
                if temp2 and not check2[temp2[0][1]][temp2[0][2]] and not check2[temp2[0][3]][temp2[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check2[temp2[0][1]][temp2[0][2]] = True
                    check2[temp2[0][3]][temp2[0][4]] = True
        # print(check)
        # print((check[0].count(True) + check[1].count(True)) // 2 + check[0].count(False) + check[1].count(False))
        find.append((check1[0].count(True) + check1[1].count(True)) // 2 +
                    check1[0].count(False) + check1[1].count(False))
        find.append((check2[0].count(True) + check2[1].count(True)) // 2 +
                    check2[0].count(False) + check2[1].count(False))

        check1 = [[False for _ in range(N)] for _ in range(2)]
        check2 = [[False for _ in range(N)] for _ in range(2)]

        for i in range(-1, 1):
            # print(-N // 2, N // 2)
            for j in range(N):
                temp1 = []
                temp2 = []
                a = area[i][j % N] + area[i][(j + 1) % N]
                b = area[i][(j + 2) % N] + area[i][(j + 1) % N]
                c = area[i - 1][(j + 1) % N] + area[i][(j + 1) % N]

                # print("center : {} left : {}, right : {}, up/down : {}"
                #       .format(area[i][j], area[i][j - 1],
                #               area[i][j + 1], area[i + 1][j]))
                if a <= W:
                    temp1.append([a, i, j % N, i, (j + 1) % N])
                if b <= W:
                    temp1.append([b, i, (j + 2) % N, i, (j + 1) % N])
                if c <= W:
                    temp1.append([c, i - 1, (j + 1) % N, i, (j + 1) % N])
                temp1.sort(key=lambda k: k[0], reverse=True)
                temp2 = [temp1[k][:] for k in range(len(temp1))]
                temp2.sort(key=lambda k: k[0], reverse=False)
                # print(temp)
                if temp1 and not check1[temp1[0][1]][temp1[0][2]] and not check1[temp1[0][3]][temp1[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check1[temp1[0][1]][temp1[0][2]] = True
                    check1[temp1[0][3]][temp1[0][4]] = True
                if temp2 and not check2[temp2[0][1]][temp2[0][2]] and not check2[temp2[0][3]][temp2[0][4]]:
                    # print(area[temp[0][1]][temp[0][2]], area[temp[0][3]][temp[0][4]])
                    check2[temp2[0][1]][temp2[0][2]] = True
                    check2[temp2[0][3]][temp2[0][4]] = True
        # print(check)
        # print((check[0].count(True) + check[1].count(True)) // 2 + check[0].count(False) + check[1].count(False))
        find.append((check1[0].count(True) + check1[1].count(True)) // 2 +
                    check1[0].count(False) + check1[1].count(False))
        find.append((check2[0].count(True) + check2[1].count(True)) // 2 +
                    check2[0].count(False) + check2[1].count(False))

        print(find)
        print(min(find))


if __name__ == "__main__":
    main()
