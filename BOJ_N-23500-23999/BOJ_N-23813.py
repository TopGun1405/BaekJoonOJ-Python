def main():
    N = input()

    tot = 0
    for _ in range(len(N)):
        tot += int(N)
        N = N[-1] + N[:-1]

    print(tot)


if __name__ == "__main__":
    main()
