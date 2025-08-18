def main():
    B, N, M = map(int, input().split())

    items = {}
    for _ in range(N):
        i, p = map(lambda e: int(e) if e.isdigit() else e, input().split())
        items[i] = p

    pay = 0
    for _ in range(M):
        j = input()
        pay += items[j]

    print("acceptable" if pay <= B else "unacceptable")


if __name__ == "__main__":
    main()
