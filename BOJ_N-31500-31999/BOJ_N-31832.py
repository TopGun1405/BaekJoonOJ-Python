def main():
    N = int(input())

    for _ in range(N):
        S = input()

        if len(S) > 10:
            continue

        lower, upper = 0, 0
        for c in S:
            if c == "-":
                continue
            elif c.islower():
                lower += 1
            elif c.isupper():
                upper += 1

        if upper > lower:
            continue
        if S.isdigit():
            continue

        print(S)


if __name__ == "__main__":
    main()
