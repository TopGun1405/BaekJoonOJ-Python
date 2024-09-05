def main():
    R, C = map(int, input().split())

    kayaks = dict(zip(range(1, 10), [0] * 9))
    for _ in range(1, R+1):
        sat_map = list(input())

        if sat_map.count(".") == C-2:
            continue

        dis = 0
        for c in sat_map[1:-1]:
            if c.isdigit():
                kayaks[int(c)] = dis
            dis += 1
    kayaks = sorted(kayaks.items(), key=lambda k: -k[1])

    curr, prev = 1, -1
    ranks = [0] * 10
    for i, dis in kayaks:
        if prev < 0:
            prev = dis
        if prev != dis:
            curr += 1

        ranks[i], prev = curr, dis

    print(*ranks[1:], sep="\n")


if __name__ == "__main__":
    main()
