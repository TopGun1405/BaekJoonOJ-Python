def main():
    n = int(input())
    for _ in range(n):
        p = int(input())
        maxPrice, maxName = 0, ''
        for _ in range(p):
            C, name = input().split()
            if int(C) > maxPrice:
                maxPrice, maxName = int(C), name
        print(maxName)


if __name__ == "__main__":
    main()
