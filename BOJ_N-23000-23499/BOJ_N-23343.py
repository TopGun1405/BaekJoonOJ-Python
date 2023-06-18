def main():
    try:
        x, y = map(int, input().split())
        print(x - y)
    except ValueError:
        print("NaN")


if __name__ == "__main__":
    main()
