def main():
    N = int(input())
    a = list(map(int, input().split()))
    ID = list(map(int, input().split()))

    for _ in range(3):
        temp = [0] * N
        for i in range(N):
            temp[i] = ID[a[i]-1]
        ID = temp

    print(*ID, sep="\n")


if __name__ == "__main__":
    main()
