def main():
    while True:
        c = float(input())
        if c == 0:
            break
        n, k = 2, 0
        while k < c:
            k, n = k + 1/n, n + 1
        print(f"{n - 2} card(s)")


if __name__ == "__main__":
    main()
