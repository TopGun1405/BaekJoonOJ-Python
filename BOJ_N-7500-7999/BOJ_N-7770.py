def main():
    n = int(input())

    k, h = 0, 0
    while k <= n:
        h += 1
        k += (2*h - 1)**2 - 4*(h*(h-1) // 2)

    if k > n:
        h -= 1

    print(h)


if __name__ == "__main__":
    main()
