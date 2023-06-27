def main():
    N = int(input())
    f = sorted([list(map(int, input().split())) for _ in range(N)])
    print(sum(f[i][0] * (i + 1) + f[i][1] for i in range(N)))


if __name__ == "__main__":
    main()
