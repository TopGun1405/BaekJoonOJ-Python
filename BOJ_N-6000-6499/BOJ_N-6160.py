def main():
    N, K = map(int, input().split())
    votes = [[i+1] + list(map(int, input().split())) for i in range(N)]
    A = sorted(votes, key=lambda k: -k[1])[:K]
    B = sorted(A, key=lambda k: -k[2])
    print(B[0][0])


if __name__ == "__main__":
    main()
