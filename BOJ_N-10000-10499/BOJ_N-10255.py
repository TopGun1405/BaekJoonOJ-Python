def main():
    def ccw(V2: list) -> list:
        x3, y3, x4, y4 = V2

        if max(x1, x2) < min(x3, x4):
            return [0, False, False]
        if min(x1, x2) > max(x3, x4):
            return [0, False, False]
        if max(y1, y2) < min(y3, y4):
            return [0, False, False]
        if min(y1, y2) > max(y3, y4):
            return [0, False, False]

        v1 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        v2 = (x2 - x1) * (y4 - y1) - (x4 - x1) * (y2 - y1)
        v3 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
        v4 = (x4 - x3) * (y2 - y3) - (x2 - x3) * (y4 - y3)

        # 평행, 선분의 끝점이 겹칠 시 잘못 분류
        if v1 * v2 <= 0 and v3 * v4 <= 0:
            if v1 == v2 == v3 == v4 == 0:
                if max(x1, x2) == min(x3, x4) or min(x1, x2) == max(x3, x4):
                    # 평행 and 끝점
                    if [x1, y1] in [[x3, y3], [x4, y4]] and 1:
                        return [1, [x1, y1] == [x3, y3], [x1, y1] == [x4, y4]]
                    # 평행 and 끝점
                    elif [x2, y2] in [[x3, y3], [x4, y4]]:
                        return [1, [x2, y2] == [x3, y3], [x2, y2] == [x4, y4]]
                # 평행 and 겹침
                return [4, False, False]
            else:
                # 평행 x and 끝점
                d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                pre = (x1 * y2 - y1 * x2)
                post = (x3 * y4 - y3 * x4)
                x = (pre * (x3 - x4) - (x1 - x2) * post) / d
                y = (pre * (y3 - y4) - (y1 - y2) * post) / d
                return [1, [x, y] == [x3, y3], [x, y] == [x4, y4]]
        else:
            return [0, False, False]

    T = int(input())
    cnt = [None] * 4
    num_intersection = []
    for _ in range(T):
        x_min, y_min, x_max, y_max = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())

        cases = [
            [x_min, y_min, x_min, y_max],
            [x_min, y_max, x_max, y_max],
            [x_max, y_max, x_max, y_min],
            [x_max, y_min, x_min, y_min]
        ]

        for i, case in enumerate(cases):
            cnt[i] = ccw(case)

        print('#' * 10)
        print(cnt)
        tot = 0
        for i, j in zip([0, 1, 2, 3], [1, 2, 3, 0]):
            cnt1, l1, r1 = cnt[i]
            cnt2, l2, r2 = cnt[j]
            if r1 and r1 == l2:
                tot -= cnt2
            tot += cnt2
        # print(tot)

        num_intersection.append(tot if tot < 4 else 4)

    print(*num_intersection, sep='\n')


if __name__ == "__main__":
    main()
