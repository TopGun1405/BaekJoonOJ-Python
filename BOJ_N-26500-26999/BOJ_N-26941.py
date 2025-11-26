def main():
    N = int(input())
    h = 1
    while True:
        N -= (2*h-1) ** 2
        if N <= 0:
            h -= 1 if N < 0 else 0
            break
        h += 1

    print(h)


if __name__ == "__main__":
    main()
