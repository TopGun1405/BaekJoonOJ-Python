def main():

    def cost(x1, y1, x2, y2):
        return ((x2-x1) + (y2-y1)) * 2

    N = int(input())
    a, b, c, d = map(int, input().split())

    print(cost(a, b, c, d))
    for _ in range(N-1):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a, b = min(a, a_i), min(b, b_i)
        c, d = max(c, c_i), max(d, d_i)

        print(cost(a, b, c, d))


if __name__ == "__main__":
    main()
