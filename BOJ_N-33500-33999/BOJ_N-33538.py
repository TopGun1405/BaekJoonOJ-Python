def main():
    l = int(input())
    n = int(input())
    t = float(input())
    hope = False
    for _ in range(n):
        f, b = map(float, input().split())

        if l/f + l/b < t:
            hope = True

    print("HOPE" if hope else "DOOMED")


if __name__ == "__main__":
    main()
