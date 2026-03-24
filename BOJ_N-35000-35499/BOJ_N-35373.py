def main():
    n = int(input())
    size = {'S': 0, 'M': 0, 'L': 0}
    for _ in range(n):
        s_i, l_i = map(lambda e: int(e) if e.isdigit() else e, input().split())
        size[s_i] += l_i

    box = size['S'] // 6 + (1 if size['S'] % 6 else 0)
    box += size['M'] // 8 + (1 if size['M'] % 8 else 0)
    box += size['L'] // 12 + (1 if size['L'] % 12 else 0)

    print(box)


if __name__ == "__main__":
    main()
