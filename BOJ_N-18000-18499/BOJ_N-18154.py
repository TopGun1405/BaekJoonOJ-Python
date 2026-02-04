def main():
    N = int(input())
    maxV = 0
    t_prev, d_prev = -1, -1
    for _ in range(N):
        t_i, d_i = map(int, input().split())

        if t_prev == d_prev == -1:
            t_prev, d_prev = t_i, d_i
            continue

        maxV = max(maxV, (d_i - d_prev) // (t_i - t_prev))
        t_prev, d_prev = t_i, d_i

    print(maxV)


if __name__ == "__main__":
    main()
