def main():
    y, c, p = map(int, input().split())

    print(min(y, c//2, p))


if __name__ == "__main__":
    main()
