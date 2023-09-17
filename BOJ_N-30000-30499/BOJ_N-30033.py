def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for AN, BN in zip(A, B):
        if BN >= AN:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
