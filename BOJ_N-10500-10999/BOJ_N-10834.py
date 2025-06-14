def main():
    M = int(input())
    d, n = 0, 1
    for _ in range(M):
        a, b, s = map(int, input().split())
        d, n = (d + s) % 2, int(n * b / a)

    print(d, n)


if __name__ == "__main__":
    main()
