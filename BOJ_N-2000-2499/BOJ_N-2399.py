def main():
    n = int(input())
    x = sorted(map(int, input().split()))

    tot, x_t = [0] * n, 0
    for i in range(1, n):
        tot[i] = tot[i-1] + (x[i] - x[i-1]) * i
        x_t += tot[i]

    print(x_t * 2)


if __name__ == "__main__":
    main()
