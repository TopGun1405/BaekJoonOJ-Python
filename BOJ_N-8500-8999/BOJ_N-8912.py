def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))

        tot = 0
        for i in range(1, n):
            cnt = 0
            for j in range(i):
                if A[j] <= A[i]:
                    cnt += 1
            tot += cnt

        print(tot)


if __name__ == "__main__":
    main()
