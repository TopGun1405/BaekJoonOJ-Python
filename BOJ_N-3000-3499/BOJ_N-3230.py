def main():
    N, M = map(int, input().split())

    rank1 = []
    for n in range(1, N + 1):
        rank1.insert(int(input()) - 1, n)
    rank1 = rank1[:M][::-1]

    rank2 = []
    for rank in rank1:
        rank2.insert(int(input()) - 1, rank)

    print(*rank2[:3], sep='\n')


if __name__ == "__main__":
    main()
