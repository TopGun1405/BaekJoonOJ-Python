def main():
    records = [input().replace(":", " ").split() for _ in range(8)]
    records.sort(key=lambda k: (k[0], k[1], k[2]))

    scores = {'R': 0, 'B': 0}
    rank = [10, 8, 6, 5, 4, 3, 2, 1]
    for i, record in enumerate(records):
        _, _, _, team = record
        scores[team] += rank[i]
    print("Red" if scores['R'] > scores['B'] else "Blue")


if __name__ == "__main__":
    main()
