def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        tot = 0
        for _ in range(x):
            name, quantity, price = input().split()
            tot += int(quantity) * float(price)
        print("${:0.2f}".format(tot))


if __name__ == "__main__":
    main()
