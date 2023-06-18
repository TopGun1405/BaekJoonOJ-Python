def main():
    n = int(input())
    # 5x + 2y = n
    c5 = n // 5
    while True:
        if (n - 5 * c5) % 2 == 0:
            print(c5 + (n - 5 * c5) // 2)
            break
        elif c5 == 0:
            print(-1)
            break
        c5 -= 1


if __name__ == "__main__":
    main()
