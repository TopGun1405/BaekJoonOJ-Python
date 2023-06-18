def main():
    g, p, t = map(int, input().split())
    t1 = g + p * t
    t2 = g * p
    print(1 if t2 < t1 else (2 if t1 < t2 else 0))


if __name__ == "__main__":
    main()
