def main():
    t, s, h = int(input()), int(input()), int(input())

    for _ in range(t):
        print("*" + " " * s + "*" + " " * s + "*")

    print("*" * (2 * s + 3))

    for _ in range(h):
        print(" " * (s + 1) + "*")


if __name__ == "__main__":
    main()
