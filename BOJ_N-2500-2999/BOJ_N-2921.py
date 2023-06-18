def main():
    N = int(input())
    tot = 0
    for i in range(N + 1):
        for j in range(i, N + 1):
            tot += i + j
    print(tot)


if __name__ == "__main__":
    main()
