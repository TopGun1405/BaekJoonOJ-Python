def main():
    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    temp = {k: [] for k in range(1, n + 1)}
    for i in range(5):
        able = 0
        for j in range(n):
            if S[j][i]:
                able += 1
        temp[able].append(i)
    print(temp)


if __name__ == "__main__":
    main()
