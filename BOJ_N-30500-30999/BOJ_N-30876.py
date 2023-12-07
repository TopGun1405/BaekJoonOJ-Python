def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda k: k[1])
    print(*points[0])


if __name__ == "__main__":
    main()
