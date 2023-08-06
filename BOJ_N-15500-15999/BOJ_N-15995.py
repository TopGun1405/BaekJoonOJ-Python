def main():
    a, m = map(int, input().split())
    n = 1
    while True:
        k = m * n + 1
        if k / a == k // a:
            print(k // a)
            break
        n += 1


if __name__ == "__main__":
    main()
