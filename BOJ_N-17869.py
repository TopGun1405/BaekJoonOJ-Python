def main():
    n = int(input())
    t = 0
    while n > 1:
        n = n + 1 if n % 2 else n // 2
        t += 1
    print(t)


if __name__ == "__main__":
    main()
