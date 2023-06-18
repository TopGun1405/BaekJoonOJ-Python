def main():
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    score = [0 for _ in range(N)]
    for i in range(M):
        B = list(map(int, input().split()))
        for j in range(N):
            if A[i] == B[j]:
                score[j] += 1
            else:
                score[A[i] - 1] += 1
    print(*score, sep='\n')


if __name__ == "__main__":
    main()
