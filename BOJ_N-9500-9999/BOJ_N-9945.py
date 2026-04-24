def main():
    caseNum = 1
    while True:
        n = int(input())

        if n < 0:
            break

        x_tot, y_tot, m_tot = 0, 0, 0
        for _ in range(n):
            x_i, y_i, m_i = map(int, input().split())

            x_tot += x_i * m_i
            y_tot += y_i * m_i
            m_tot += m_i

        input()

        a = round(x_tot / m_tot, 2)
        b = round(y_tot / m_tot, 2)

        print(f"Case {caseNum}: {a:.2f} {b:.2f}")

        caseNum += 1


if __name__ == "__main__":
    main()
