def main():
    N = int(input())

    cnt_team = 0
    for _ in range(N):
        T = list(map(int, input().split()))

        if sum(T) == -3:
            continue

        for i in range(3):
            if T[i] == -1:
                T[i] = 121

        if T[0] <= T[1] <= T[2]:
            cnt_team += 1

    print(cnt_team)


if __name__ == "__main__":
    main()
