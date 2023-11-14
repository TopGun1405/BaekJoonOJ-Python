def main():
    N = int(input())
    # P = [list(map(lambda e: int(e) if e.isdigit() else e, input().split())) for _ in range(N)]
    P = []
    for _ in range(N):
        Si, Ii, Di = map(lambda e: int(e) if e.isdigit() else e, input().split())
        P.append([Si, Ii, Di])
    P.sort(key=lambda k: k[1])

    ISIS = list(map(lambda c: c[0][c[2] - 1].upper(), P))
    print(''.join(ISIS))


if __name__ == "__main__":
    main()
