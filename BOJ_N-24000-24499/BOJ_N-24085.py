def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = {n: 0 for n in set(A)}
    for AN in A:
        cnt[AN] += 1

    cnt = sorted(cnt.items(), key=lambda k: (k[1], k[0]))
    print(cnt[0][0])


if __name__ == "__main__":
    main()
