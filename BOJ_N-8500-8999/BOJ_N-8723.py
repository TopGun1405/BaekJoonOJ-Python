def main():
    a, b, c = map(int, input().split())
    print(1 if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2
          else (2 if a == b == c else 0))


if __name__ == "__main__":
    main()
