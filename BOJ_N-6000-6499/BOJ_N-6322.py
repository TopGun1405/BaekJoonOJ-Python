def main():
    i = 1
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        if i > 1:
            print()
        print("Triangle #{}".format(i))

        if c == -1:
            print("c = {:0.3f}".format((a ** 2 + b ** 2) ** 0.5))
        elif max(a, b) >= c:
            print("Impossible.")
        elif a == -1:
            print("a = {:0.3f}".format((c ** 2 - b ** 2) ** 0.5))
        elif b == -1:
            print("b = {:0.3f}".format((c ** 2 - a ** 2) ** 0.5))
        i += 1


if __name__ == "__main__":
    main()
