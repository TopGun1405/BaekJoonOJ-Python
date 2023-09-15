def main() -> None:
    T = int(input())
    subs = list(map(int, input().split()))
    subs += [0] * (5 - T)

    num = 0
    a, b = subs[0], subs[2]
    if a > b:
        num += (a - b) * 508
    else:
        num += (b - a) * 108

    a, b = subs[1], subs[3]
    if a > b:
        num += (a - b) * 212
    else:
        num += (b - a) * 305

    num += subs[4] * 707

    print(num * 4763)


if __name__ == "__main__":
    main()
