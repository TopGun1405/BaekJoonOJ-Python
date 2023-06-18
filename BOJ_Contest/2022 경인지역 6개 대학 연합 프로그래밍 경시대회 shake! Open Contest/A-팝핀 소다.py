from math import log2


def main():
    N, M, K = map(int, input().split())
    win, low = 0, K - 1
    while low > 0:
        low = (low - 1) // 2
        win += 1
    print(win + M if win + M <= log2(N) else int(log2(N)))


if __name__ == "__main__":
    main()
