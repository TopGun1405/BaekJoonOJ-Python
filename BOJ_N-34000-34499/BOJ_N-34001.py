def main():
    A = [[200, 210, 220], [210, 220, 225], [220, 225, 230],
         [225, 230, 235], [230, 235, 245], [235, 245, 250]]
    G = [[260, 265, 270], [265, 270, 275], [270, 275, 280],
         [275, 280, 285], [280, 285, 290], [285, 290, 295], [290, 295, 300]]

    L = int(input())
    Q1 = []
    for i in range(len(A)):
        cnt = 0
        for j in range(3):
            if L >= A[i][j]:
                if j == 0:
                    cnt = 500
                else:
                    cnt -= 200
        Q1.append(cnt)

    Q2 = []
    for i in range(len(G)):
        cnt = 0
        for j in range(3):
            if L >= G[i][j]:
                if j == 0:
                    cnt = 500
                else:
                    cnt -= 200
        Q2.append(cnt)

    print(*Q1)
    print(*Q2)


if __name__ == "__main__":
    main()
