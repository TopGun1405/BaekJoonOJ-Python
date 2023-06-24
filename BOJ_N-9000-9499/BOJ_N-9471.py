def main():
    P = int(input())
    for p in range(1, P + 1):
        N, M = map(int, input().split())

        k = 1
        m1, m2 = 1, 2
        while True:
            if m1 % M == m2 % M == 1:
                break
            k += 1
            m1, m2 = m2, (m1 + m2) % M

        print(f"{p} {k}")


if __name__ == "__main__":
    main()
