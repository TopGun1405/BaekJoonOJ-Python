def main():
    n = int(input())
    o, p = 1, 0
    while o * 2**p < n:
        if n % (o * 2**p) == 0:
            if (n // (o * 2**p)) % 2 == 1:
                o = n // (o * 2**p)
                break
        p += 1
    print(f"{o} {p}")


if __name__ == "__main__":
    main()
