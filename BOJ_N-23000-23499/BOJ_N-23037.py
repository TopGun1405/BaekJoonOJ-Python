def main():
    n = list(input())
    tot = 0

    for i in range(len(n)):
        n[i] = int(n[i]) ** 5
        tot += n[i]

    print(tot)


if __name__ == "__main__":
    main()
