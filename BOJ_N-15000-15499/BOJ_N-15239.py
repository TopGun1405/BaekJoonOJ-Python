def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()

        l, u, d, s = 0, 0, 0, 0
        for c in S:
            if c.islower():
                l += 1
            elif c.isupper():
                u += 1
            elif c.isdigit():
                d += 1
            elif c in "+_)(*&^%$#@!./,;{}":
                s += 1

        if l > 0 and u > 0 and d > 0 and s > 0 and N >= 12:
            print("valid")
        else:
            print("invalid")


if __name__ == "__main__":
    main()
