def main():
    n = int(input())
    hands = 0
    for l in range(6):
        for r in range(l, 6):
            if l + r == n:
                hands += 1
    print(hands)


if __name__ == "__main__":
    main()
