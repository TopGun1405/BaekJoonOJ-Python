def main():
    A1, A2, A3 = int(input()), int(input()), int(input())
    print(min(A2 * 2 + A3 * 4, A1 * 2 + A3 * 2, A1 * 4 + A2 * 2))


if __name__ == "__main__":
    main()
