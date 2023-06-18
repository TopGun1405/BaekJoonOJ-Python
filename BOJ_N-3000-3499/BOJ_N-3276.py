def main():
    N = int(input())
    r, c = 1, 1
    while r * c < N:
        if r > c:
            c += 1
        else:
            r += 1
    print(r, c)


if __name__ == "__main__":
    main()
