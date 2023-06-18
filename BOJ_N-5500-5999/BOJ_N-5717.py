def main():
    while True:
        b, g = map(int, input().split())
        if b == g == 0:
            break
        print(b + g)


if __name__ == "__main__":
    main()
