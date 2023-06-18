def main():
    N = int(input())
    X = list(map(int, input().split()))
    # for i in range(N):
    #     num = []
    #     for j in range(1, int(X[i] ** 0.5) + 1):
    #         if X[i] % j == 0:
    #             num.append(j)
    #             if j ** 2 != X[i]:
    #                 num.append(X[i] // j)
    #     print(1 if len(num) % 2 == 1 else 0, end=' ')
    for i in X:
        if i == int(i ** 0.5) ** 2:
            print(1, end=' ')
        else:
            print(0, end=' ')


if __name__ == "__main__":
    main()
