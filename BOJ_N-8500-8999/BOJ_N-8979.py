def main():
    N, K = map(int, input().split())
    medals = [list(map(int, input().split())) for _ in range(N)]
    medals.sort(key=lambda k: (k[1], k[2], k[3]), reverse=True)

    idx = 0
    for i, medal in enumerate(medals):
        if medal[0] == K:
            idx = i

    for i, medal in enumerate(medals):
        if medals[idx][1:] == medal[1:]:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
