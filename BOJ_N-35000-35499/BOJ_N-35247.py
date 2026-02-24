def main():
    n = int(input())

    x = 1
    while True:
        if n < 2 ** x:
            print(f"{x} {'bit' if x == 1 else 'bits'}")
            break
        x *= 2


if __name__ == "__main__":
    main()
