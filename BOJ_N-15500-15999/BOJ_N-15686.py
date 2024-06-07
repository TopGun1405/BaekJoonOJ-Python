def main():
    INF = int(1e9)

    def chickenDelivery(rec, idx):
        if rec == M:
            city_dis = 0
            for r1, c1 in home:
                dis = INF
                for i in range(CL):
                    if not opened[i]:
                        continue
                    r2, c2 = chicken[i]
                    dis = min(dis, abs(r1 - r2) + abs(c1 - c2))
                city_dis += dis
            val['MIN'] = min(val['MIN'], city_dis)
            return

        for i in range(idx, CL):
            if not opened[i]:
                opened[i] = True
                chickenDelivery(rec+1, i+1)
                opened[i] = False

    N, M = map(int, input().split())
    home, chicken = [], []
    for r in range(N):
        city = list(map(int, input().split()))
        for c in range(N):
            if city[c] == 1:
                home.append([r, c])
            elif city[c] == 2:
                chicken.append([r, c])

    CL = len(chicken)
    opened = [False] * CL
    val = {'MIN': INF}

    chickenDelivery(0, 0)

    print(val['MIN'])


if __name__ == "__main__":
    main()
