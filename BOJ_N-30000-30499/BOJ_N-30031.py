def main():
    money = {136: 1_000, 142: 5_000, 148: 10_000, 154: 50_000}
    N = int(input())
    tot = 0
    for _ in range(N):
        w, h = map(int, input().split())
        tot += money[w]
    print(tot)


if __name__ == "__main__":
    main()
