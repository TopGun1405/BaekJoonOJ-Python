def main():
    n = int(input())
    for _ in range(n):
        cards = input().split()

        strength = {}
        for c in cards:
            try:
                strength[c[0]] += 1
            except KeyError:
                strength[c[0]] = 1
        maxStrength = max(strength.values())

        print(maxStrength)


if __name__ == "__main__":
    main()
