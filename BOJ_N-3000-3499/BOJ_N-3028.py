def main():
    exc = input()
    cups = [0, 1, 1]
    for e in exc:
        if e == 'A':
            cups[0], cups[1] = cups[1], cups[0]
        elif e == 'B':
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[2], cups[0] = cups[0], cups[2]
    print(cups.index(0) + 1)


if __name__ == "__main__":
    main()
