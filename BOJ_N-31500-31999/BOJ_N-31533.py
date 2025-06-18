def main():
    a = int(input())
    m, n = map(int, input().split())

    m, n = min(m, n), max(m, n)
    t = max(m, n / a)
    t = min((m / a) * 2, t)

    print(t)


if __name__ == "__main__":
    main()
