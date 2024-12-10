def main():
    n = int(input())
    wine = [int(input()) for _ in range(n)]

    drink = [wine[0]] + [0] * (n - 1)
    if n > 1:
        drink[1] = drink[0] + wine[1]
    if n > 2:
        drink[2] = max(drink[1], wine[1] + wine[2], wine[0] + wine[2])
    for i in range(3, n):
        drink[i] = max(drink[i-1], drink[i-2] + wine[i], drink[i-3] + wine[i-1] + wine[i])

    print(drink)
    print(drink[n-1])


if __name__ == "__main__":
    main()
