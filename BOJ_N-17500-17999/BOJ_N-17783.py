def main():
    n = int(input())
    print("Bob" if n & 1 else "Alice\n{}".format(n // 2))


if __name__ == "__main__":
    main()
