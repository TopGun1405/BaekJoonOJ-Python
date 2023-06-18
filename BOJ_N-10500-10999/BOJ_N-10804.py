def main():
    num = list(range(1, 21))
    for _ in range(10):
        a, b = map(int, input().split())
        num[a - 1:b] = num[a - 1:b][::-1]
    print(*num)


if __name__ == "__main__":
    main()
