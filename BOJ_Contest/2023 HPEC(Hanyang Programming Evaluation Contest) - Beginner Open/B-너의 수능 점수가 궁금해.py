def main() -> None:
    S = int(input())
    S //= 4763

    res = []
    for n1 in range(201):
        for n2 in range(201):
            res.append([n1 * 508 + n2 * 212, n1, n2])
            res.append([n1 * 508 + n2 * 305, n1, n2])
            res.append([n1 * 108 + n2 * 212, n1, n2])
            res.append([n1 * 108 + n2 * 305, n1, n2])

    res = list(filter(lambda n: n[0] == S, res))
    print(len(res))
    if res:
        for _, e1, e2 in sorted(res, key=lambda k: (k[1], k[2])):
            print(e1, e2)


if __name__ == "__main__":
    main()
