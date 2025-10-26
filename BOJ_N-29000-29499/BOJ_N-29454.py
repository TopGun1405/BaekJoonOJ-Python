def main():
    n = int(input())
    a = list(map(int, input().split()))

    tot = sum(a)
    for i in range(n):
        if tot - a[i] == a[i]:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
