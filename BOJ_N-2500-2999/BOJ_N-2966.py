def main():
    N = int(input())
    ans = input()

    score = [[0, "Adrian"], [0, "Bruno"], [0, "Goran"]]
    ABG = [
        "ABC" * (N // 3) + "ABC"[:N % 3],
        "BABC" * (N // 4) + "BABC"[:N % 4],
        "CCAABB" * (N // 6) + "CCAABB"[:N % 6]
    ]

    for i in range(N):
        for ii in range(3):
            if ans[i] == ABG[ii][i]:
                score[ii][0] += 1

    score.sort(key=lambda k: (-k[0], k[1]))
    k = score[0][0]
    print(k)
    print(*map(lambda e: e[1], filter(lambda e: e[0] == k, score)), sep="\n")


if __name__ == "__main__":
    main()
