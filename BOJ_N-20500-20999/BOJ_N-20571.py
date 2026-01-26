def main():
    zone = {
        'residential': {
            f: e for start, end, e in [(1, 1, 0), (2, 5, 1), (6, 10, 2), (11, 15, 3), (16, 20, 4)]
            for f in range(start, end + 1)
        },
        'commercial': {
            f: e for start, end, e in [(1, 1, 0), (2, 7, 1), (8, 14, 2), (15, 20, 3)]
            for f in range(start, end + 1)
        },
        'industrial': {
            f: e for start, end, e in [(1, 1, 0), (2, 4, 1), (5, 8, 2), (9, 12, 3), (13, 16, 4), (17, 20, 5)]
            for f in range(start, end + 1)
        }
    }

    S, N = map(lambda e: int(e) if e.isdigit() else e, input().split())

    print(zone[S][N])


if __name__ == "__main__":
    main()
