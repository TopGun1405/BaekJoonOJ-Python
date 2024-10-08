def main():
    n = int(input())
    d = list(filter(lambda e: e % 2, [int(input()) for _ in range(n)]))
    print(len(d))


if __name__ == "__main__":
    main()
