def main():
    S = int(input())
    tot, i = 0, 1
    while True:
        if tot + i == S:
            print(i)
            break
        elif tot + i > S:
            print(i - 1)
            break
        tot += i
        i += 1


if __name__ == "__main__":
    main()
