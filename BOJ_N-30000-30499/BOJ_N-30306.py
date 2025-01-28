def main():
    n = int(input())
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))

    res = 0
    for d1_i in d1:
        for d2_i in d2:
            if d1_i > d2_i:
                res += 1
            elif d1_i < d2_i:
                res -= 1

    print("first" if res > 0 else ("second" if res < 0 else "tie"))


if __name__ == "__main__":
    main()
