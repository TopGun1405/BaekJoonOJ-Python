def main():
    num = sorted(map(int, input().split()))
    c = list(input())

    for i in c:
        if i == 'A':
            print(num[0], end=' ')
        elif i == 'B':
            print(num[1], end=' ')
        elif i == 'C':
            print(num[2], end=' ')


if __name__ == "__main__":
    main()
