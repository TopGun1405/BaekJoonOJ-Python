def main():
    N, K = map(int, input().split())
    A = list(enumerate(map(int, input().split())))
    B = sorted(sorted(A, key=lambda k: k[1])[-K:], key=lambda k: k[0])
    score, j = 0, 0
    for i, Ai in A:
        score += Ai * K
        if i == B[j][0]:
            K, j = K - 1, j + 1
        if K == 0:
            break
    print(score)


if __name__ == "__main__":
    main()
