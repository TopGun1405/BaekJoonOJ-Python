def main():
    D, H, M = map(int, input().split())

    s_sec = 11 * 60 * 24 + 11 * 60 + 11
    r_sec = D * 60 * 24 + H * 60 + M - s_sec
    if r_sec < 0:
        print(-1)
    else:
        print(r_sec)


if __name__ == "__main__":
    main()
