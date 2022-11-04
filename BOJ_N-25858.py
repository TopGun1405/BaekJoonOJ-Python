def main():
    n, d = map(int, input().split())
    div = [int(input()) for _ in range(n)]
    tot = sum(div)
    for m in div:
        print(d * m // tot)


if __name__ == "__main__":
    main()
