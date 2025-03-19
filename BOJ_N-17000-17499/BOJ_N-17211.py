def main():
    N, F = map(int, input().split())
    D = list(map(float, input().split()))

    good, bad = 1 if F == 0 else 0, 0 if F == 0 else 1
    gg, gb, bg, bb = D[:4]
    for i in range(N):
        prev = good
        good = good * gg + bad * bg
        bad = prev * gb + bad * bb

    print(int(good * 1_000))
    print(int(bad * 1_000))


if __name__ == "__main__":
    main()
