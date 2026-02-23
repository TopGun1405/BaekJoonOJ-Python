def main():
    n = int(input())
    t = 0
    for _ in range(n):
        mm, ss = map(int, input().split(":"))
        t += mm * 60 + ss

    HH, MM, SS = t // 3600, t % 3600 // 60, t % 3600 % 60

    print(f"{HH:02d}:{MM:02d}:{SS:02d}")


if __name__ == "__main__":
    main()
