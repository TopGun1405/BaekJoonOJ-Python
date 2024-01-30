def main():
    n, x, y = map(int, input().split())
    for _ in range(n):
        a = int(input())
        print(round(a * (y / x)))


if __name__ == "__main__":
    main()
