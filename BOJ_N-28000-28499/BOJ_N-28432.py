def main():
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    A = [input() for _ in range(M)]

    if N == 1:
        print(S[0])
        exit(0)

    for i in range(N):
        if S[i] != "?":
            continue

        for j in range(M):
            if A[j] in S:
                continue
                
            if i == 0 and A[j][-1] == S[i+1][0]:
                print(A[j])
                break
            elif i == N-1 and A[j][0] == S[i-1][-1]:
                print(A[j])
                break
            else:
                if A[j][0] == S[i-1][-1] and A[j][-1] == S[i+1][0]:
                    print(A[j])
                    break
        else:
            continue
        break


if __name__ == "__main__":
    main()
