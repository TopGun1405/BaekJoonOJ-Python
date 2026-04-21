def main():
    x = 1
    while True:
        s = int(input())

        if s == 0:
            break

        if x > 1:
            print()

        compressed = (s + 1) // 2
        uuencoded = (compressed * 3 + 1) // 2
        lines = (uuencoded + 61) // 62
        chunks = (lines + 29_999) // 30_000

        print(f"File #{x}")
        print(f"John needs {chunks} floppies.")
        x += 1


if __name__ == "__main__":
    main()
