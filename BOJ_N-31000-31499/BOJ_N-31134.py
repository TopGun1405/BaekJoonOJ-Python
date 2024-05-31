def main():
    T = int(input())

    res = []
    for _ in range(T):
        x = int(input())
        if x == 1:
            res.append(1)
        else:
            res.append(2*x - 1)

    print(*res, sep="\n")


if __name__ == "__main__":
    main()

