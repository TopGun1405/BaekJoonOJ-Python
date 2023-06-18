def main():
    num = list(input())
    while '0' in num:
        i = num.index('0')
        num[i - 1:i + 1] = [''.join(num[i - 1:i + 1])]
    print(int(num[0]) + int(num[1]))


if __name__ == "__main__":
    main()
