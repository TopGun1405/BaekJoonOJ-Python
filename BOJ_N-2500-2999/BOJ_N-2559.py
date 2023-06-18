def main():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    m = 0
    for i in range(0, N - K + 1, K):
        temp = 0
        for j in range(i, i + K):
            temp += D[j]
        print(temp)
        if temp > m:
            m = temp
    print(m)


if __name__ == "__main__":
    main()
