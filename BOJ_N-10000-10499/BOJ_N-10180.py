def main():
    T = int(input())
    for _ in range(T):
        N, D = map(int, input().split())
        ship = 0
        for _ in range(N):
            v, f, c = map(int, input().split())
            ship = ship + (1 if v * f / c >= D else 0)
        print(ship)


if __name__ == "__main__":
    main()
