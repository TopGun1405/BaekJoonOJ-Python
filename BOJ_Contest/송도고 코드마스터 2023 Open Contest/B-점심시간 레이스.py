def main():
    n, m, k = map(int, input().split())
    winner, d = 0, 1e9
    for i in range(k):
        fi, di = map(int, input().split())
        t = fi + m - di
        if t < d:
            winner, d = i + 1, t
    print(winner)


if __name__ == "__main__":
    main()
