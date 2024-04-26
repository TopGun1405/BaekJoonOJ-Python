def main():
    N = int(input())

    N1 = bin(N)[2:].zfill(32)
    N2 = bin((1 << 32) + ~N + 1)[2:]

    cnt = 0
    for n1, n2 in zip(N1, N2):
        if n1 != n2:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
