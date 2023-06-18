def main():
    num = sorted([int(input()) for _ in range(5)])
    print(sum(num) // 5)
    print(num[2])


if __name__ == "__main__":
    main()
