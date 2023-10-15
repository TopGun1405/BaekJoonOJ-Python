def main():
    n = int(input())
    for _ in range(n):
        a, b = int(input()), int(input())
        if _ != 0:
            print()
        print(f"{a // b}\n{a % b}")


if __name__ == "__main__":
    main()
