from itertools import combinations


def main():
    x = list(map(int, input().split()))

    x_d = list(combinations(x, 2))
    x_t = list(combinations(x, 3))

    cnt = 0
    for x_i in x_d:
        if x_i.count(1) > 0:
            cnt += 1

    for x_i in x_t:
        if x_i.count(1) > 0:
            cnt += 1

    print(1 if cnt % 2 else 0)


if __name__ == "__main__":
    main()
