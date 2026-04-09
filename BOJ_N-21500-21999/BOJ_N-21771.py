def main():
    R, C = map(int, input().split())
    R_g, C_g, R_p, C_p = map(int, input().split())
    S = [list(input()) for _ in range(R)]

    P = 0
    for r in range(R):
        P += S[r].count("P")

    if P != R_p * C_p:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
