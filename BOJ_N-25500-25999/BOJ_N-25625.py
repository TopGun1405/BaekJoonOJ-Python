def main():
    x, y = map(int, input().split())
    print(x + y if y <= x else y - x)


if __name__ == "__main__":
    main()
