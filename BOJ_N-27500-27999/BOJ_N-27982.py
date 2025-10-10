def main():
    N, M = map(int, input().split())
    cubes = set()
    for _ in range(M):
        i, j, k = map(int, input().split())
        cubes.add((i, j, k))

    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    cnt = 0
    for i, j, k in cubes:
        if all((i+di, j+dj, k+dk) in cubes for di, dj, dk in d):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
