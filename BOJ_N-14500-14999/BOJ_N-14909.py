def main():
    num = list(map(int, input().split()))
    p = 0
    for n in num:
        if n > 0:
            p += 1
    print(p)


if __name__ == "__main__":
    main()
