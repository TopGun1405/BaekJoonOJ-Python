def main():
    T = int(input())
    for _ in range(T):
        M = int(input())
        P, curr = 0, 0
        for _ in range(M):
            P1, P2 = map(int, input().split())
            curr = curr - P1 + P2
            P = max(P, curr)

        print(P)


if __name__ == "__main__":
    main()
