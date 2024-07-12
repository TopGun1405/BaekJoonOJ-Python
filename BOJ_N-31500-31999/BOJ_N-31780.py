from math import ceil, floor


def main():
    X, M = map(int, input().split())

    phoenix, tot = [[X]], X
    for _ in range(M):
        phoenix.append([])
        for p in phoenix[-2]:
            phoenix[-1].append(floor(p/2))
            phoenix[-1].append(ceil(p/2))
        tot += sum(phoenix[-1])

    print(tot)


if __name__ == "__main__":
    main()
