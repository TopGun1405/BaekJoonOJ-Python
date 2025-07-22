def main():
    N = int(input())
    internet = []
    for _ in range(N):
        T_i, M_i = map(int, input().split())

        if M_i == 1:
            internet += [0] * (T_i - len(internet)-1) + [1]
        else:
            internet += [0] * (T_i - len(internet))

    t_max, t_prev = 0, 0
    for i, t_i in enumerate(internet):
        if t_i == 1:
            t_max = max(t_max, i - t_prev)
            t_prev = i

    print(t_max)


if __name__ == "__main__":
    main()
