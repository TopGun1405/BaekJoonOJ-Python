def main():
    L = int(input())
    S = sorted(map(int, input().split()))
    n = int(input())

    if n in S:
        print(0)
    else:
        minN, maxN = 0, 0
        for S_i in S:
            if S_i < n:
                minN = S_i
            elif S_i > n and maxN == 0:
                maxN = S_i
        minN += 1
        maxN -= 1

        print((n - minN) * (maxN - n + 1) + (maxN - n))


if __name__ == "__main__":
    main()
