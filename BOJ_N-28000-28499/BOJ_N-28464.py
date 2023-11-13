def main():
    N = int(input())
    a = sorted(map(int, input().split()))
    print(sum(a[:N//2]), sum(a[N//2:]))


if __name__ == "__main__":
    main()
