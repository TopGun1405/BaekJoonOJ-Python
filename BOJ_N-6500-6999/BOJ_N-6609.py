def main():
    while True:
        try:
            M, P, L, E, R, S, N = map(int, input().split())

            for i in range(N):
                tot = M
                M = P // S
                P = L // R
                L = tot * E
            
            print(M)

        except EOFError:
            break


if __name__ == "__main__":
    main()
