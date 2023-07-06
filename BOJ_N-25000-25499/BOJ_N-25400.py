def main():
    N = int(input())
    A = list(map(int, input().split()))

    k, cnt = 1, 0
    for i in A:
        if i == k:
            k += 1
        else:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
