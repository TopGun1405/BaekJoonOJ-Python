def main():
    N = int(input())
    a = 0
    while True:
        if a == ((a + 1) ** 2 - 2 * a - a ** 2) ** N:
            break
        a += 1
    # always 1
    print(a)


if __name__ == "__main__":
    main()
