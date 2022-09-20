def main():
    N = int(input())
    max_score = 0
    for _ in range(N):
        a, d, g = map(int, input().split())

        score = a * (d + g)
        if a == d + g:
            score *= 2

        if score > max_score:
            max_score = score
    print(max_score)


if __name__ == "__main__":
    main()
