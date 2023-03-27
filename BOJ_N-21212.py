def main():
    N = int(input())
    minN = 1e9
    for _ in range(N):
        a, b = map(int, input().split())
        if minN > b // a:
            minN = b // a
    print(minN)


if __name__ == "__main__":
    main()
