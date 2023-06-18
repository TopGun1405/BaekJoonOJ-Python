def main():
    a, b = map(int, input().split())
    print(b if a // 2 >= b else a // 2)


if __name__ == "__main__":
    main()
