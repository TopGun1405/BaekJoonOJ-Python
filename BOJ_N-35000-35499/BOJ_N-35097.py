def main():
    while True:
        n = int(input())

        if n == 0:
            break

        v = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                v += a * b

        print(v)


if __name__ == "__main__":
    main()
