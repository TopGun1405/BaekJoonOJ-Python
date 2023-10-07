def main():
    N, X = map(int, input().split())
    p = list(map(int, input().split()))
    x = 0
    for pi in p:
        if pi % X != 0:
            x += pi
    print(1 if x % X == 0 else 0)


if __name__ == "__main__":
    main()
