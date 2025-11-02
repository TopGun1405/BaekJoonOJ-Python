def main():
    r, f = map(int, input().split())

    s = f / r
    angle = (s * 180) % 360

    print("up" if angle < 90 or 270 < angle < 360 else "down")


if __name__ == "__main__":
    main()
