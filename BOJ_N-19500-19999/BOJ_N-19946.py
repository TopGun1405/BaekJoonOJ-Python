def main():
    N = int(input())

    for i in range(65):
        K = 2**i - 1
        for j in range(i+1, 65):
            K *= 2
        if K == N:
            print(i)


if __name__ == "__main__":
    main()
