def main():
    card = {
        'A': [11, 11],
        'K': [4, 4],
        'Q': [3, 3],
        'J': [2, 20],
        'T': [10, 10],
        '9': [0, 14],
        '8': [0, 0],
        '7': [0, 0]
    }

    N, B = map(lambda e: int(e) if e.isdigit() else e, input().split())
    score = 0
    for _ in range(4 * N):
        Ki = input()

        score += card[Ki[0]][Ki[1] == B]

    print(score)


if __name__ == "__main__":
    main()
