def main():
    n = int(input())
    first = 0
    for _ in range(n):
        if first == 0:
            first = int(input())
        else:
            x = int(input())
            if x % first == 0:
                print(x)
                first = 0


if __name__ == "__main__":
    main()
