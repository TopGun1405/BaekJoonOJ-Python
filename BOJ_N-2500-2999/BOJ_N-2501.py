def main():
    N, K = map(int, input().split())
    k = 0
    for i in range(1, N + 1):
        if N % i == 0:
            k += 1
        if k == K:
            print(i)
            break
    else:
        print(0)


if __name__ == "__main__":
    main()
