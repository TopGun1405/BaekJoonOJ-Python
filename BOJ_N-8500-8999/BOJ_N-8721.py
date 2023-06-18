def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt, cn = 0, 1
    for a in A:
        if a == cn:
            cn += 1
        else:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
