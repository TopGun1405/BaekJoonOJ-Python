def main():
    N = int(input())
    A = list(map(int, input().split()))

    sumA = [0]
    for An in A:
        sumA.append(sumA[-1] + An)

    M = int(input())
    for _ in range(M):
        i, j = map(int, input().split())
        print(sumA[j] - sumA[i-1])


if __name__ == "__main__":
    main()
