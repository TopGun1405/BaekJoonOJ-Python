def main():
    while True:
        A, B, C, D = map(int, input().split())

        if A == B == C == D == 0:
            break

        if (A <= C and B <= D) or (A <= D and B <= C):
            print("100%")

        else:
            p1 = min((C * 100) // A, (D * 100) // B)
            p2 = min((C * 100) // B, (D * 100) // A)

            p = max(p1, p2)
            p = 1 if p < 1 else (100 if p > 100 else p)

            print(f"{p}%")


if __name__ == "__main__":
    main()
