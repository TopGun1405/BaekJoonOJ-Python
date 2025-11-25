def main():
    MM, SS = map(int, input().split(":"))

    t = (MM*3600 + SS*60) - (MM*60 + SS)
    HH, MM_, SS_ = t // 3600, t % 3600 // 60, t % 60

    print(f"{HH:02d}:{MM_:02d}:{SS_:02d}")


if __name__ == "__main__":
    main()
