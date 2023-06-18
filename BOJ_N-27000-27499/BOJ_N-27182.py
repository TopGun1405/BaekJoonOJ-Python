def main():
    n, m = map(int, input().split())
    days = {14: 28, 15: 29, 16: 30, 17: 31}
    print(n - 7 if n > 7 else days[m - n] - (7 - n))


if __name__ == "__main__":
    main()
