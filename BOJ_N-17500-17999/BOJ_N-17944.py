def main():
    N, T = map(int, input().split())

    arms, k = 0, 1
    for _ in range(T):
        arms += k
        if arms == 2 * N:
            k = -1
        if arms == 1:
            k = 1

    print(arms)


if __name__ == "__main__":
    main()
