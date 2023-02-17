def main():
    n = int(input())
    fly, k = 0, 1

    while n > 0:
        if n < k:
            k = 1
        n, k, fly = n - k, k + 1, fly + 1
    print(fly)


if __name__ == "__main__":
    main()
