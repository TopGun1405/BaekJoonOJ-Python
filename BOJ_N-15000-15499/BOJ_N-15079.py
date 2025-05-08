def main():
    n = int(input())
    x, y = map(int, input().split())
    for _ in range(n-1):
        direction, d = input().split()
        d = int(d)

        n = ((d ** 2) / 2) ** 0.5
        if direction == "N":
            y += d
        elif direction == "NE":
            x += n
            y += n
        elif direction == "E":
            x += d
        elif direction == "SE":
            x += n
            y -= n
        elif direction == "S":
            y -= d
        elif direction == "SW":
            x -= n
            y -= n
        elif direction == "W":
            x -= d
        elif direction == "NW":
            x -= n
            y += n

    print(f"{x:.06f} {y:.06f}")


if __name__ == "__main__":
    main()
