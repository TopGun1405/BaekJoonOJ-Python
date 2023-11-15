def main():
    n, m = map(int, input().split())

    node = 1 if m == 2 else 0
    current = 0
    for i in range(1, n):
        if m > node:
            print(0, i)
            node += 1
        else:
            print(current, i)
        current = i


if __name__ == "__main__":
    main()
