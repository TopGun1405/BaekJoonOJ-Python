def main():
    while True:
        try:
            g, y, m, d = input().split()
            y, m, d = int(y), int(m), int(d)
            print(f"? {y - 30} {m} {d}" if (y == 31 and m >= 5 and d >= 1) or y >= 32
                  else f"{g} {y} {m} {d}")
        except ValueError:
            break


if __name__ == "__main__":
    main()
