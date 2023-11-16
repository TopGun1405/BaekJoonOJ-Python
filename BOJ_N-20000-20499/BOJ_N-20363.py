def main():
    x, y = map(int, input().split())
    print(int(x + y + (min(x, y) / 10)))


if __name__ == "__main__":
    main()
