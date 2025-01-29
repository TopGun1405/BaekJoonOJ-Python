def main():
    n = 1
    while True:
        p, s = map(int, input().split())

        if p == s == 0:
            break

        print(f"Hole #{n}")

        if s == 1:
            print("Hole-in-one.")
        elif p - s == 3:
            print("Double eagle.")
        elif p - s == 2:
            print("Eagle.")
        elif p - s == 1:
            print("Birdie.")
        elif p - s == 0:
            print("Par.")
        elif p - s == -1:
            print("Bogey.")
        else:
            print("Double Bogey.")
        print()

        n += 1


if __name__ == "__main__":
    main()
