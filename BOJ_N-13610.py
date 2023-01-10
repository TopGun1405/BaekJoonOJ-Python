def main():
    X, Y = map(int, input().split())
    print(1 + X // (Y - X) + (0 if X % (Y - X) == 0 else 1))


if __name__ == "__main__":
    main()
