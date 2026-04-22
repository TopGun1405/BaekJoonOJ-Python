def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]

    def update_prefix(start):
        for idx in range(start, n):
            prefix[idx+1] = prefix[idx] + a[idx]

    for _ in range(m):
        k, l, r = map(int, input().split())
        l -= 1
        if k == 1:
            for i in range(l, r):
                a[i] = a[i]**2 % 2_010
            update_prefix(l)
        else:
            print(sum(a[l:r]))


if __name__ == "__main__":
    main()
