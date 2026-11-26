def main():
    K = int(input())
    for x in range(1, K+1):
        n, W, E = map(int, input().split())

        totalHappy = 0
        for _ in range(n):
            L_ww, L_we, L_ew, L_ee = map(int, input().split())
            totalHappy += max(W*L_ww + E*L_ew, W*L_we + E*L_ee)

        print(f"Data Set {x}:")
        print(totalHappy)
        print()


if __name__ == "__main__":
    main()
