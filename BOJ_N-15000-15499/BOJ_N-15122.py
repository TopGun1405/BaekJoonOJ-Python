def main():
    n = int(input())
    while True:
        n += 1
        if "0" not in str(n):
            print(n)
            break


if __name__ == "__main__":
    main()
