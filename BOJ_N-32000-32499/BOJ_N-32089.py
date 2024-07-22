def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))

        maxN = sum(a[:3])
        for i in range(n-2):
            print(a[i])
            maxN = max(maxN, sum(a[i:i+3]))

        print(maxN)


if __name__ == "__main__":
    main()
