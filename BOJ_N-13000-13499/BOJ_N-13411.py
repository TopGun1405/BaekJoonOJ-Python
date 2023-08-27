def main():
    N = int(input())
    robots = []
    for n in range(1, N + 1):
        Xi, Yi, Vi = map(int, input().split())
        # S = V * T
        robots.append([n, (Xi**2 + Yi**2)**0.5 / Vi])
    robots.sort(key=lambda k: (k[1], k[0]))

    # for n, t in robots:
    #     print(n)
    print(*map(lambda e: e[0], robots), sep='\n')


if __name__ == "__main__":
    main()
