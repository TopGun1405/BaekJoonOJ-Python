def main():
    distance = [
        lambda d: d <= 9,
        lambda d: 9 < d <= 36,
        lambda d: 36 < d <= 81,
        lambda d: 81 < d <= 144,
        lambda d: 144 < d <= 225
    ]
    point = [100, 80, 60, 40, 20]

    T = int(input())
    for _ in range(T):
        pos = list(map(float, input().split()))

        N, M = 0, 0
        pos_n, pos_m = pos[:6], pos[6:]
        for x_n, y_n in zip(pos_n[::2], pos_n[1::2]):
            dis_n = x_n**2 + y_n**2
            for i in range(5):
                if not distance[i](dis_n):
                    continue
                N += point[i]

        for x_m, y_m in zip(pos_m[::2], pos_m[1::2]):
            dis_m = x_m**2 + y_m**2
            for i in range(5):
                if not distance[i](dis_m):
                    continue
                M += point[i]

        result = "PLAYER 1 WINS" if N > M else "PLAYER 2 WINS" if N < M else "TIE"
        print(f"SCORE: {N} to {M}, {result}.")


if __name__ == "__main__":
    main()
