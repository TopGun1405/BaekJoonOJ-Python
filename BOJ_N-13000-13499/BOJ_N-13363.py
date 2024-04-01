def main():
    n1 = int(input())
    n2 = int(input())

    n = n2 - n1
    if n > 180:
        n -= 360
    elif n <= -180:
        n += 360

    print(n)


if __name__ == "__main__":
    main()
