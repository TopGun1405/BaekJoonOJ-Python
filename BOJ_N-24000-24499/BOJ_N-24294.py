def main():
    w1, h1 = int(input()), int(input())
    w2, h2 = int(input()), int(input())
    print(2 * max(w1, w2) + 2 * (h1 + h2) + 4)


if __name__ == "__main__":
    main()
