def main():
    N, M = map(int, input().split())
    item = {i: N for i in range(1, 5)}
    imp = 0
    for _ in range(M):
        p, x, q, y = map(int, input().split())
        item[p], item[q] = item[p] - 1, item[q] - 1
    print(item[1] * item[2] * item[3] * item[4])
    print(N ** 4)


if __name__ == "__main__":
    main()
