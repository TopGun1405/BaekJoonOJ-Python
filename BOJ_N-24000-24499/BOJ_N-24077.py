def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for Ai in A:
        for Bj in B:
            if Ai <= Bj:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
