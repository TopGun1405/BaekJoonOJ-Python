def main():
    N = int(input())
    pd = input().split()
    ans = set(pd[i][0] for i in range(N))
    print((0, 1)[len(ans) == 1])


if __name__ == "__main__":
    main()
