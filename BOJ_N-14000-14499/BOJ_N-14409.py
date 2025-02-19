def main():
    N = int(input())
    X = int(input())

    tuna = 0
    for _ in range(N):
        P1, P2 = map(int, input().split())
        if abs(P1 - P2) <= X:
            tuna += max(P1, P2)
        else:
            P3 = int(input())
            tuna += P3

    print(tuna)


if __name__ == "__main__":
    main()
