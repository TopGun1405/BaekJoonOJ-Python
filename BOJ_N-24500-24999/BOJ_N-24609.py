def main():
    n = int(input())
    fees, curr = 0, 0
    for _ in range(n):
        t = int(input())
        curr += t
        fees = min(fees, curr)
    print(-fees)


if __name__ == "__main__":
    main()
