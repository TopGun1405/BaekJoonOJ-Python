def main():
    N = int(input())
    bids = {}
    for _ in range(N):
        name = input()
        bid = int(input())

        try:
            bids[bid].append(name)
        except KeyError:
            bids[bid] = [name]

    bids = sorted(bids.items(), key=lambda k: k[0])

    print(bids[-1][1][0])


if __name__ == "__main__":
    main()
