def main():
    m = int(input())
    b = list(map(int, input().split()))

    i, seq = 0, []
    while i < m:
        seq.append(b[i])
        i += b[i]

    print(*seq)


if __name__ == "__main__":
    main()
