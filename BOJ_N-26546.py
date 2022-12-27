def main():
    n = int(input())
    for _ in range(n):
        s, i, j = input().rstrip().split()
        s = list(s)[:int(i)] + list(s)[int(j):]
        print(''.join(s))


if __name__ == "__main__":
    main()
