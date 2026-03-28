def main():
    H, M = map(int, input().split())

    ranges = [
        (390, 540),
        (590, 600),
        (650, 660),
        (710, 720),
        (770, 830),
        (880, 890),
        (940, 950),
        (1000, 1370)
    ]
    t = H * 60 + M

    print("Yes" if any(start <= t <= end for start, end in ranges) else "No")


if __name__ == "__main__":
    main()
