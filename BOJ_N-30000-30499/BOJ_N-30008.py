def main():
    N, K = map(int, input().split())
    G = list(map(int, input().split()))

    D = []
    for Gi in G:
        P = Gi * 100 // N
        if 0 <= P <= 4:
            D.append(1)
        elif 4 < P <= 11:
            D.append(2)
        elif 11 < P <= 23:
            D.append(3)
        elif 23 < P <= 40:
            D.append(4)
        elif 40 < P <= 60:
            D.append(5)
        elif 60 < P <= 77:
            D.append(6)
        elif 77 < P <= 89:
            D.append(7)
        elif 89 < P <= 96:
            D.append(8)
        elif 96 < P <= 100:
            D.append(9)

    print(*D)


if __name__ == "__main__":
    main()
