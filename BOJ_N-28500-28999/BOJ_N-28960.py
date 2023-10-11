def main():
    h, l, a, b = map(int, input().split())
    print("YES" if (b / 2 <= h and a <= l) or (a / 2 <= h and b <= l) else "NO")


if __name__ == "__main__":
    main()
