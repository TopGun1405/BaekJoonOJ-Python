def main():
    n, c = map(int, input().split())

    total_sec = 0
    for _ in range(n):
        m, ss = map(int, input().split(":"))
        total_sec += (m * 60) + ss

    total_sec -= max(0, (n - 1) * c)
    hh, rm = divmod(total_sec, 3600)
    mm, ss = divmod(rm, 60)

    print(f"{hh:02}:{mm:02}:{ss:02}")


if __name__ == "__main__":
    main()
