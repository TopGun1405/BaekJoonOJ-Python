def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    M = int(input())
    B = map(int, input().split())
    for n in B:
        low, high = 0, len(A) - 1
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == n:
                answer = 1
                break
            if A[mid] >= n:
                high = mid - 1
            else:
                low = mid + 1
        print(answer)


if __name__ == "__main__":
    main()
