def main():
    n = int(input())
    x = list(map(int, input().split()))

    x_sum, tot = sum(x), 0
    for xi in x:
        x_sum -= xi
        tot += xi * x_sum
    print(tot)


if __name__ == "__main__":
    main()
