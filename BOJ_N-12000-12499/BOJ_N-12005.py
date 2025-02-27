def main():
    N, K = map(int, input().split())
    diamonds = [int(input()) for _ in range(N)]

    max_diamonds = 0
    for d1 in diamonds:
        cnt = 0
        for d2 in diamonds:
            if d2 >= d1 and d2 - d1 <= K:
                cnt += 1
        max_diamonds = max(max_diamonds, cnt)

    print(max_diamonds)


if __name__ == "__main__":
    main()
