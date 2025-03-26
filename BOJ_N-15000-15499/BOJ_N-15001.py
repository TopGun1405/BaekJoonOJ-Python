def main():
    n = int(input())
    x = [int(input()) for _ in range(n)]

    dis = 0
    for i, j in zip(range(n-1), range(1, n)):
        dis += (x[j] - x[i]) ** 2

    print(dis)


if __name__ == "__main__":
    main()
