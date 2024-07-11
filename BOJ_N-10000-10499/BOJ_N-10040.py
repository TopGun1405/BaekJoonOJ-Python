def main():
    N, M = map(int, input().split())
    A = [[n+1, int(input())] for n in range(N)]
    B = [int(input()) for _ in range(M)]

    votes = {n: 0 for n in range(1, N+1)}
    for B_j in B:
        for i, A_i in A:
            if A_i > B_j:
                continue
            votes[i] += 1
            break
    votes = sorted(votes.items(), key=lambda k: k[1], reverse=True)

    print(votes[0][0])


if __name__ == "__main__":
    main()
