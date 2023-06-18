def main():
    a, b = map(int, input().split())
    print(1 if a - a * (b / 100) < 100 else 0)


if __name__ == "__main__":
    main()
