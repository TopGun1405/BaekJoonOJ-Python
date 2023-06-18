def main():
    N = int(input())
    p = list(input() for _ in range(N))
    c, g = p[0], 2
    for i in range(1, N):
        if p[i] != c:
            c, g = p[i], g + 1
    print(g)


if __name__ == "__main__":
    main()
