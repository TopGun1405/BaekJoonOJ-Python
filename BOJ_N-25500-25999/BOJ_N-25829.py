def main():
    n = int(input())

    votes1, votes2 = 0, 0
    e1, e2 = 0, 0
    for _ in range(n):
        e, v1, v2 = map(int, input().split())
        votes1 += v1
        votes2 += v2

        if v1 > v2:
            e1 += e
        else:
            e2 += e

    if votes1 > votes2:
        winner_v = 1
    elif votes2 > votes1:
        winner_v = 2
    else:
        winner_v = 0

    if e1 > e2:
        winner_e = 1
    elif e2 > e1:
        winner_e = 2
    else:
        winner_e = 0

    if winner_v == winner_e and winner_v != 0:
        print(winner_v)
    else:
        print(0)


if __name__ == "__main__":
    main()
