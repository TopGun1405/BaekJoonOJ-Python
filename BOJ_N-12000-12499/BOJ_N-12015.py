def main():
    N = int(input())
    A = list(map(int, input().split()))
    LIS = [A[0]]

    for Ai in A[1:]:
        if LIS[-1] < Ai:
            LIS.append(Ai)
        else:
            low, high = 0, len(LIS)
            while low < high:
                mid = (low + high) // 2
                if LIS[mid] < Ai:
                    low = mid + 1
                else:
                    high = mid
            LIS[high] = Ai
    # print(LIS)
    print(len(LIS))


if __name__ == "__main__":
    main()
