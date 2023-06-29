def main():
    N, M = map(int, input().split())
    DNA = [input() for _ in range(N)]

    s, h_dis = [], 0
    for i in range(M):
        dna = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(N):
            dna[DNA[j][i]] += 1

        maxDNA = max(dna.values())
        for k in dna:
            if dna[k] == maxDNA and len(s) <= i:
                s.append(k)
            else:
                h_dis += dna[k]

    print(''.join(s))
    print(h_dis)


if __name__ == "__main__":
    main()
