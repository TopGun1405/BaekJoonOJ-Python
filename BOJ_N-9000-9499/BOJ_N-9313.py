def main():
    while True:
        n = int(input())
        if n == -1:
            break
        print(int(f"{bin(n)[2:]:0>32}"[::-1], 2))


if __name__ == "__main__":
    main()
