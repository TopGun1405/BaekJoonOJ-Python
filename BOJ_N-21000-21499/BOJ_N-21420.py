def main():
    n = int(input())
    c1, c2 = 0, 0

    for i in range(n):
        x = int(input())
        if x == 1:
            c1 += 1
        else:
            c2 += 1
    print(min(c1, c2))


if __name__ == "__main__":
    main()
