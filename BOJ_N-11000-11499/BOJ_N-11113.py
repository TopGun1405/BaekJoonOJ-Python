def main():
    n = int(input())
    pos = [list(map(float, input().split())) for _ in range(n)]
    m = int(input())
    for _ in range(m):
        p = int(input())
        idx = list(map(int, input().split()))

        s = 0
        for i, j in zip(idx[1:], idx[:-1]):
            s += ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2) ** 0.5

        print(int(s) + (1 if s - int(s) >= 0.5 else 0))


if __name__ == "__main__":
    main()
