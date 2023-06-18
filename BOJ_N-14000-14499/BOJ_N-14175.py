def main():
    M, N, K = map(int, input().split())
    for _ in range(M):
        S = input()
        newS = ''.join(map(lambda s: s * K, S))
        for _ in range(K):
            print(newS)


if __name__ == "__main__":
    main()
