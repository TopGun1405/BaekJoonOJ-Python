def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_m, i = 1, 0
    while i < N:
        j = i
        while j+1 < N and A[j] < A[j+1]:
            j += 1

        k = j
        while k+1 < N and A[k] > A[k+1]:
            k += 1

        max_m = max(max_m, k-i+1)
        i = j+1

    print(max_m)


if __name__ == "__main__":
    main()
