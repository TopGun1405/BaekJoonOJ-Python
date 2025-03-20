def main():
    M, N = map(int, input().split())
    planets = [list(map(int, input().split())) for _ in range(M)]

    for _ in range(M):
        for i in range(M):
            sorted_p = sorted(planets[i])
            planets[i] = [sorted_p.index(idx)+1 for idx in planets[i]]

    cnt = 0
    for i in range(M-1):
        for j in range(i+1, M):
            if planets[i] == planets[j]:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
