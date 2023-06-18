def main():
    k, a, b = map(int, input().split())
    if a % k == 0:
        a //= k
    else:
        a = a // k + 1
    chocolate = b // k + 1 - a
    print(chocolate)


if __name__ == "__main__":
    main()
