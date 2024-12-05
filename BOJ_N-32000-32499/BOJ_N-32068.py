def main():
    T = int(input())

    for _ in range(T):
        L, R, S = map(int, input().split())
        L_D, R_D = S-L, R-S

        print(L_D*2+1 if L_D < R_D else R_D*2)


if __name__ == "__main__":
    main()
