def main():
    n = int(input())
    num, cnt = 1, 2
    for i in range(9, n, 3):
        num, cnt = num + cnt, cnt + 1
    print(num)


if __name__ == "__main__":
    main()
