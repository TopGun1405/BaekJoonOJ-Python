def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        b = list(range(1, n+1))
        for i in range(n):
            if a[i] == b[i]:
                b[i] += 1

            for ii in range(i+1, n):
                if b[ii-1] >= b[ii]:
                    b[ii] += (b[ii-1]-b[ii])+1

        print(b[n-1])


if __name__ == "__main__":
    main()
