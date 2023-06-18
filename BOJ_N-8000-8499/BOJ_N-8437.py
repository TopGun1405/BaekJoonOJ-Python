def main():
    a, b = int(input()), int(input())
    # a = x + y
    # x - y = b, x - b = y
    # 2x = a + b
    print((a + b) // 2)
    print(a - (a + b) // 2)


if __name__ == "__main__":
    main()
