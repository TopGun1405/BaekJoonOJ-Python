def main():
    h = int(input())
    check = {h == 0: 1, h == 1: 0}
    for c in check:
        if c:
            print(check[c])
            break
    else:
        if h % 2:
            print(4, end='')
        for _ in range(h // 2):
            print(8, end='')


if __name__ == "__main__":
    main()
