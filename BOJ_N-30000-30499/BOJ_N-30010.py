def main():
    def bubble_sort() -> None:
        for i in range(N - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if A[j] > A[j + 1]:
                    tmp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = tmp

    N = int(input())
    A = [N] + list(range(1, N))
    print(*A)


if __name__ == "__main__":
    main()
