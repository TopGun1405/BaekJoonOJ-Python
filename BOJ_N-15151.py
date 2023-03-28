def main():
    k, d = map(int, input().split())
    t, c = 2, 0
    while True:
        d -= k * t ** c
        if d >= 0:
            c += 1
        else:
            break
    print(c)


if __name__ == "__main__":
    main()
