def main():
    N, K = map(int, input().split())
    obstacle = [list(map(int, input().split())) for _ in range(N)]
    cmd = list(input())

    x, y = 0, 0
    for c_i in cmd:
        if c_i == "U" and [x, y+1] not in obstacle:
            y += 1
        elif c_i == "D" and [x, y-1] not in obstacle:
            y -= 1
        elif c_i == "R" and [x+1, y] not in obstacle:
            x += 1
        elif c_i == "L" and [x-1, y] not in obstacle:
            x -= 1

    print(x, y)


if __name__ == "__main__":
    main()
