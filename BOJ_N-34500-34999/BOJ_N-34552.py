def main():
    M = list(map(int, input().split()))
    N = int(input())
    tot = 0
    for _ in range(N):
        B_i, L_i, S_i = input().split()
        B_i, L_i, S_i = int(B_i), float(L_i), int(S_i)
        if L_i < 2.0 or S_i < 17:
            continue
        tot += M[B_i]

    print(tot)


if __name__ == "__main__":
    main()
