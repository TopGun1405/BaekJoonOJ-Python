def main():
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        print(a // b, a % b, '/', b)


if __name__ == "__main__":
    main()
