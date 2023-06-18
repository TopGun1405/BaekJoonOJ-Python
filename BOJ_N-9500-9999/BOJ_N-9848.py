def main():
    n, k = map(int, input().split())
    record = [int(input()) for _ in range(n)]
    print(len(list(filter(lambda r: r[0] - r[1] >= k, zip(record[:-1], record[1:])))))


if __name__ == "__main__":
    main()
