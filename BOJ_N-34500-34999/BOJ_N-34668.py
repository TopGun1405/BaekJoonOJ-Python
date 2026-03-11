def main():
    Q = int(input())
    for _ in range(Q):
        M = int(input())

        t = 12 * (M // 50) + 6
        HH, MM = 6 + t // 60, t % 60

        if HH >= 24:
            print(-1)
        else:
            print(f"{HH:02d}:{MM:02d}")


if __name__ == "__main__":
    main()
