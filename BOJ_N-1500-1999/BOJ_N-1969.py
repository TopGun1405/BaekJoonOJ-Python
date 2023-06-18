def main():
    N, M = map(int, input().split())
    DNA = [input() for _ in range(N)]
    HDistance, dna = M + 1, ''
    for i in range(N):
        temp = 0
        for j in range(N):
            for k in range(M):
                if DNA[i][k] != DNA[j][k]:
                    temp += 1
        if temp < HDistance:
            HDistance, dna = temp, DNA[i]
    print("{}\n{}".format(dna, HDistance))


if __name__ == "__main__":
    main()
