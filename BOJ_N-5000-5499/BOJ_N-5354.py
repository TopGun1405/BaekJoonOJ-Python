def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("#" * n)
        for i in range(n - 2):
            print("#" + "J" * (n - 2) + "#")
        if n > 1:
            print("#" * n)
        print()


if __name__ == "__main__":
    main()
