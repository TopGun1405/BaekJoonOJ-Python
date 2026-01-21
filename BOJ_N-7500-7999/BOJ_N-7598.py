def main():
    while True:
        p, n = input().split()

        if p == "#" and n == "0":
            break

        seats = int(n)
        while True:
            o, x = input().split()

            if o == "X" and x == "0":
                print(p, seats)
                break

            x = int(x)
            if o == "B":
                if seats + x > 68:
                    continue
                seats += x
            elif o == "C":
                if x > seats:
                    continue
                seats -= x


if __name__ == "__main__":
    main()
