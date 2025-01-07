def main():
    while True:
        S1, S2 = input().split()

        if S1 == S2 == "#":
            break

        n = int(input())
        p1, p2 = 0, 0
        for _ in range(n):
            c1, c2 = input().split()

            if c1 == c2:
                p1 += 1
            else:
                p2 += 1

        print(f"{S1} {p1} {S2} {p2}")


if __name__ == "__main__":
    main()
