def main():
    n, a, b = map(int, input().split())
    s, t = map(int, input().split())

    if (1 <= s <= a and 1 <= t <= a) or (b <= s <= n and b <= t <= n):
        print("Outside")
    elif a < s < b and a < t < b:
        print("City")
    else:
        print("Full")


if __name__ == "__main__":
    main()
