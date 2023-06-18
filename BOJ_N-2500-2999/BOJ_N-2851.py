def main():
    m = [0] * 10
    for i in range(10):
        point = int(input())
        m[i] = m[(0 if i == 0 else i - 1)] + point
    m = sorted(map(lambda e: [abs(100 - e), e], m), key=lambda k: (k[0], -k[1]))
    print(m[0][1])


if __name__ == "__main__":
    main()
