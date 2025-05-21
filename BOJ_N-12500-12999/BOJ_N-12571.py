def main():
    T = int(input())
    for x in range(1, T+1):
        N = int(input())
        P = [list(map(int, input().split())) for _ in range(N)]

        y = 0
        if N > 1:
            A1, B1 = P[0]
            A2, B2 = P[1]

            if (A1 > A2 and B1 < B2) or (A1 < A2 and B1 > B2):
                y += 1

        print(f"Case #{x}: {y}")


if __name__ == "__main__":
    main()
