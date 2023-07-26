def main():
    P = sorted([list(map(int, input().split())) for _ in range(11)])
    tot, pen = 0, 0
    for Di, Vi in P:
        pen += tot + Di
        tot += Di
        pen += 20 * Vi
    print(pen)


if __name__ == "__main__":
    main()
