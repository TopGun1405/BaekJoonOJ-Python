def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        print("{} is {}".format(x, "odd" if x % 2 else "even"))


if __name__ == "__main__":
    main()
