def main():
    T = int(input())
    for _ in range(T):
        op = input()

        num = int("".join(list(filter(lambda n: n.isdigit(), op))))
        try:
            i = op.index("0")
        except ValueError:
            i = op.index("1")

        a = op[:i].count("!")
        num = 1 if op[i+1:].count("!") > 0 else num

        if num == 0:
            print(0 if a % 2 == 0 else 1)
        else:
            print(1 if a % 2 == 0 else 0)


if __name__ == "__main__":
    main()
