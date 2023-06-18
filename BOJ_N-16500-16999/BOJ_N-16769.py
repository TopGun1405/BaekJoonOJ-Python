def main():
    c, m = [0, 0, 0], [0, 0, 0]
    for i in range(3):
        ci, mi = map(int, input().split())
        c[i], m[i] = ci, mi
    for n in range(100):
        i, j = n % 3, (n + 1) % 3
        m[i], m[j] = max(m[i] - (c[j] - m[j]), 0), min(c[j], m[i] + m[j])
    print(*m, sep='\n')


if __name__ == "__main__":
    main()
