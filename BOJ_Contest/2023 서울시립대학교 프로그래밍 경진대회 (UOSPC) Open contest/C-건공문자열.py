def main():
    N, K = map(int, input().split())
    S = list(input())

    for i in range(N-K+1):
        S[i:i+K] = S[i:i+K][::-1]
    print("".join(S))


if __name__ == "__main__":
    main()
