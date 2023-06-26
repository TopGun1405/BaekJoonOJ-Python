def main():
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        a, b = (a + b) % 1_000_000_007, a % 1_000_000_007
    print(a)


if __name__ == "__main__":
    main()
