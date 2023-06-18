def main():
    N = int(input())
    A = list(map(int, input().split()))
    LIS, LIS_IDX = [], []

    for Ai in A:
        if not LIS or LIS[-1] < Ai:
            LIS.append(Ai)
            LIS_IDX.append((len(LIS) - 1, Ai))
        else:
            low, high = 0, len(LIS)
            while low < high:
                mid = (low + high) // 2
                if LIS[mid] < Ai:
                    low = mid + 1
                else:
                    high = mid
            LIS[high] = Ai
            LIS_IDX.append((high, Ai))

    res = []
    idx = len(LIS) - 1
    for i in range(len(LIS_IDX) - 1, -1, -1):
        if LIS_IDX[i][0] == idx:
            res.append(LIS_IDX[i][1])
            idx -= 1

    print(len(LIS))
    print(*res[::-1])


if __name__ == "__main__":
    main()
