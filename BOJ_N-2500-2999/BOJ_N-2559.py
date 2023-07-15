def main():
    N, K = map(int, input().split())
    T = list(map(int, input().split()))
    tot = [sum(T[:K])]
    for i in range(N - K):
        tot.append(tot[i] - T[i] + T[K + i])
    print(max(tot))


if __name__ == "__main__":
    main()
