def main():
    n = int(input())
    a = [4]
    f, b = 2, 1
    tot = 0
    for _ in range(1, 16):
        f += b
        tot = f ** 2
        a.append(tot)
        b = b * 2
    print(a[n])


if __name__ == "__main__":
    main()
