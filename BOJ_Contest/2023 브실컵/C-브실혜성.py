def main():
    yyyy, mm, dd = map(int, input().split('-'))
    N = int(input())
    d = (N + dd) % 30
    m = mm + ((N + dd) // 30 - (0 if (N + dd) % 30 else 1))
    y = m // 12 - (0 if m % 12 else 1)
    print('{}-{:02d}-{:02d}'.format(yyyy + y, m % 12 + (0 if m % 12 else 12), d + (0 if d else 30)))


if __name__ == "__main__":
    main()
