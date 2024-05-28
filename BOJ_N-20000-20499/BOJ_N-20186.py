def main():
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    add = 0
    for i in range(1, K+1):
        add += A[-i] - (i-1)
    print(add)


if __name__ == "__main__":
    main()
