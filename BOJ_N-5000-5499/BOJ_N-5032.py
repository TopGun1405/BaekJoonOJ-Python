def main():
    e, f, c = map(int, input().split())

    juice, k = e // c, e // c + e % c + f
    while k >= c:
        juice += k // c
        k = (k % c) + (k // c)

    print(juice)


if __name__ == "__main__":
    main()
