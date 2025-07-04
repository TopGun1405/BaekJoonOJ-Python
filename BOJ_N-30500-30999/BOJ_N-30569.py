def main():
    h1, d1, t1 = map(int, input().split())
    h2, d2, t2 = map(int, input().split())

    a = h2 // d1 + (1 if h2 % d1 else 0)
    b = h1 // d2 + (1 if h1 % d2 else 0)

    k1 = (a - 1) * t1 + 0.5
    k2 = (b - 1) * t2 + 0.5

    if k1 < k2:
        print("player one")
    elif k1 > k2:
        print("player two")
    else:
        print("draw")


if __name__ == "__main__":
    main()
