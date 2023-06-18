def main():
    x, y = map(int, input().split())
    N = int(input())
    nx = ny = 0
    for _ in range(N):
        tx, ty = map(int, input().split())
        if nx == ny == 0:
            nx, ny = tx, ty
        if abs(tx - x) + abs(ty - y) < abs(nx - x) + abs(ny - y):
            nx, ny = tx, ty
    print(nx, ny)


if __name__ == "__main__":
    main()
