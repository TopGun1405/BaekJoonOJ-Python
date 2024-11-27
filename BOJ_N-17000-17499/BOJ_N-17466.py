def main():
    N, P = map(int, input().split())
    K = 1
    for i in range(2, N+1):
        K *= i
        K %= P
    print(K % P)


if __name__ == "__main__":
    main()
