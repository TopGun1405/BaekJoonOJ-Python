def main() -> None:
    S = int(input())

    res = set()
    s = [lambda a, b: a * 508 + b * 212,
         lambda a, b: a * 508 + b * 305,
         lambda a, b: a * 108 + b * 212,
         lambda a, b: a * 108 + b * 305]
    for n1 in range(201):
        for n2 in range(201):
            for si in s:
                if si(n1, n2) * 4763 == S:
                    res.add((n1, n2))
                    break

    print(len(res))
    if res:
        for e1, e2 in sorted(res, key=lambda k: (k[0], k[1])):
            print(e1, e2)


if __name__ == "__main__":
    main()
