def main():
    n = int(input())
    s_f, t_f, f = 0, 0, 0
    for i in range(1, n + 1):
        t_i, s_i = map(int, input().split())
        if s_f < s_i:
            s_f, t_f, f = s_i, t_i, i

    if s_f == 0:
        print(0)
    elif s_f == 1 or s_f == 4:
        print(t_f + (f - 1) * 20)


if __name__ == "__main__":
    main()
