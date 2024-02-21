def main():
    N = int(input())

    rank = []
    for _ in range(N):
        Ai, Bi = map(lambda e: int(e) if e.isdigit() else e, input().split())
        rank.append([Ai, Bi])

    rank.sort(key=lambda k: (-k[1], k[0]))
    print(rank[0][0])


if __name__ == "__main__":
    main()
