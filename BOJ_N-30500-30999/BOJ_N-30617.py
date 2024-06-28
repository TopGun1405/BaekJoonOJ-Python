def main():
    T = int(input())

    cnt = 0
    l, r = 0, 0
    for _ in range(T):
        l_t, r_t = map(int, input().split())

        if l_t == r_t and l_t != 0:
            cnt += 1
        if l == l_t and l != 0:
            cnt += 1
        if r == r_t and r != 0:
            cnt += 1

        l, r = l_t, r_t

    print(cnt)


if __name__ == "__main__":
    main()
