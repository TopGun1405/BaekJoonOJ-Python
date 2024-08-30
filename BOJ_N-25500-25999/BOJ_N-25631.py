def main():
    N = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    while len(a) > 0:
        tmp_a = set(sorted(a))
        for a_i in tmp_a:
            del a[a.index(a_i)]
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
