def main():
    y, m = map(int, input().split())
    cy = (15 if y >= 1 else 0) + (9 if y >= 2 else 0) + ((y - 2) * 4 if y > 2 else 0)
    cm = (m * 15 if y < 1 else 0) + (m * 9 if 1 <= y < 2 else 0) + (m * 4 if y >= 2 else 0)
    print(cy + cm // 12, cm % 12)


if __name__ == "__main__":
    main()
