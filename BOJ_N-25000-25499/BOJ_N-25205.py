def main():
    N = int(input())
    s = input()

    c = [
        "q", "w", "e", "r", "t",
        "a", "s", "d", "f", "g",
        "z", "x", "c", "v"
    ]

    print(1 if s[-1] in c else 0)


if __name__ == "__main__":
    main()
