def main():
    N = int(input())
    for _ in range(N):
        print(int(str(sum([int(x[::-1]) for x in input().split()]))[::-1]))


if __name__ == "__main__":
    main()
