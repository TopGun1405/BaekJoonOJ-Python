def main():
    c = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N, B = map(int, input().split())
    change = []
    while N != 0:
        change.append(c[N % B])
        N //= B
    print(''.join(change[::-1]))


if __name__ == "__main__":
    main()
